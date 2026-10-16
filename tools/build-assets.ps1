<#
  build-assets.ps1 — Genera los activos raster de TOP CAR a partir de las fuentes SVG/HTML.
  Usa Microsoft Edge en modo headless (Chromium) como renderizador. No requiere dependencias externas.

  Uso:  powershell -ExecutionPolicy Bypass -File tools\build-assets.ps1
#>
$ErrorActionPreference = 'Stop'

$root   = Split-Path -Parent $PSScriptRoot
$assets = Join-Path $root 'assets'
$edge   = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

if (-not (Test-Path $edge)) {
  $edge = "C:\Program Files\Microsoft\Edge\Application\msedge.exe"
}
if (-not (Test-Path $edge)) {
  throw "No se encontro Microsoft Edge. Instalalo o ajusta la ruta en este script."
}

function Convert-ToFileUri([string]$path) {
  return 'file:///' + ($path -replace '\\', '/')
}

function Render-Png {
  param([string]$Url, [string]$Out, [int]$W, [int]$H)
  if (Test-Path $Out) { Remove-Item $Out -Force }
  $args = @(
    '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run',
    '--force-device-scale-factor=1', '--virtual-time-budget=6000',
    "--screenshot=$Out", "--window-size=$W,$H", $Url
  )
  # Edge escribe warnings en stderr aunque el render sea correcto: no debe detener el script.
  $prev = $ErrorActionPreference
  $ErrorActionPreference = 'Continue'
  & $edge @args *> $null
  $ErrorActionPreference = $prev
  for ($i = 0; $i -lt 60; $i++) { if (Test-Path $Out) { break }; Start-Sleep -Milliseconds 250 }
  if (-not (Test-Path $Out)) { throw "No se pudo renderizar: $Out" }
}

function Get-Dims([string]$path) {
  Add-Type -AssemblyName System.Drawing
  $img = [System.Drawing.Image]::FromFile($path)
  $d = "$($img.Width)x$($img.Height)"
  $img.Dispose()
  return $d
}

# ---------- 1. Imagen social (Open Graph / Twitter) ----------
# Se renderiza a PNG en un archivo temporal y se convierte a JPEG (mucho mas liviano),
# que es lo unico que se publica en el repositorio.
Write-Host "-> og-image.jpg (1200x630, JPEG q88)"
$ogTemp = Join-Path $env:TEMP 'topcar-og.png'
Render-Png -Url (Convert-ToFileUri (Join-Path $assets 'og-source.html')) -Out $ogTemp -W 1200 -H 630

Add-Type -AssemblyName System.Drawing
$srcImg = [System.Drawing.Image]::FromFile($ogTemp)
$jpgPath = Join-Path $assets 'og-image.jpg'
$jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$encParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
$encParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]88)
$bmp = New-Object System.Drawing.Bitmap($srcImg.Width, $srcImg.Height)
$gfx = [System.Drawing.Graphics]::FromImage($bmp)
$gfx.Clear([System.Drawing.Color]::FromArgb(10, 11, 13))
$gfx.DrawImage($srcImg, 0, 0, $srcImg.Width, $srcImg.Height)
$gfx.Dispose()
$bmp.Save($jpgPath, $jpegCodec, $encParams)
$bmp.Dispose()
$srcImg.Dispose()
Remove-Item $ogTemp -Force -ErrorAction SilentlyContinue

# ---------- 2. Apple touch icon + iconos del manifest ----------
Write-Host "-> iconos cuadrados (180 / 192 / 512)"
$squareUrl = Convert-ToFileUri (Join-Path $assets 'icon-square.svg')
Render-Png -Url $squareUrl -Out (Join-Path $assets 'apple-touch-icon.png') -W 180 -H 180
Render-Png -Url $squareUrl -Out (Join-Path $assets 'icon-192.png')        -W 192 -H 192
Render-Png -Url $squareUrl -Out (Join-Path $assets 'icon-512.png')        -W 512 -H 512

# ---------- 3. favicon.ico multi-resolucion (16/32/48, PNG embebido) ----------
Write-Host "-> favicon.ico (16/32/48)"
$favUrl = Convert-ToFileUri (Join-Path $assets 'favicon.svg')
$sizes = @(16, 32, 48)
$tmpPngs = @()
foreach ($s in $sizes) {
  $p = Join-Path $env:TEMP "topcar-fav-$s.png"
  Render-Png -Url $favUrl -Out $p -W $s -H $s
  $tmpPngs += ,@($s, $p)
}

$ms = New-Object System.IO.MemoryStream
$bw = New-Object System.IO.BinaryWriter($ms)
$bw.Write([UInt16]0)                 # reserved
$bw.Write([UInt16]1)                 # type = icon
$bw.Write([UInt16]$tmpPngs.Count)    # image count
$offset = 6 + (16 * $tmpPngs.Count)
$blobs = @()
foreach ($t in $tmpPngs) { $blobs += ,[System.IO.File]::ReadAllBytes($t[1]) }
for ($i = 0; $i -lt $tmpPngs.Count; $i++) {
  $dim = [int]$tmpPngs[$i][0]
  $data = $blobs[$i]
  $bw.Write([Byte]($dim % 256))      # width  (0 => 256)
  $bw.Write([Byte]($dim % 256))      # height
  $bw.Write([Byte]0)                 # color palette
  $bw.Write([Byte]0)                 # reserved
  $bw.Write([UInt16]1)               # color planes
  $bw.Write([UInt16]32)              # bits per pixel
  $bw.Write([UInt32]$data.Length)    # size in bytes
  $bw.Write([UInt32]$offset)         # offset
  $offset += $data.Length
}
foreach ($b in $blobs) { $bw.Write($b) }
$bw.Flush()
[System.IO.File]::WriteAllBytes((Join-Path $assets 'favicon.ico'), $ms.ToArray())
$bw.Close(); $ms.Close()
foreach ($t in $tmpPngs) { Remove-Item $t[1] -Force -ErrorAction SilentlyContinue }

# ---------- 4. Reporte ----------
Write-Host ""
Write-Host "Activos generados:"
Get-ChildItem $assets -File | Where-Object { $_.Extension -in '.png', '.ico', '.jpg' } | Sort-Object Name | ForEach-Object {
  $extra = ''
  if ($_.Extension -in '.png', '.jpg') { $extra = " ($(Get-Dims $_.FullName))" }
  Write-Host ("  {0,-24} {1,7} KB{2}" -f $_.Name, [math]::Round($_.Length / 1KB, 1), $extra)
}
