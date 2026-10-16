# TOP CAR — One Page | Taller Mecánico en Rivera, Uruguay

Sitio de una sola página para **TOP CAR — Mecánica Automotriz** (Rivera, Uruguay).
HTML + CSS + JavaScript vanilla, sin build ni dependencias: se sube a cualquier hosting estático y se apunta el dominio.

**Producción:** <https://dfchanel-coder.github.io/topcarrivera/>

---

## 📁 Estructura

```
TopCar/
├── index.html              # Página única (contenido + SEO + datos estructurados)
├── css/
│   └── styles.css          # Estilos (responsive, secciones claras/oscuras, animaciones)
├── js/
│   └── main.js             # Menú, scroll, sección activa, estado abierto/cerrado
├── assets/
│   ├── icon-square.svg     # Fuente del icono cuadrado (apple-touch + manifest)
│   ├── favicon.svg         # Fuente del favicon (pestaña del navegador)
│   ├── logo.svg
│   ├── og-source.html      # Fuente de la imagen social (1200×630)
│   ├── favicon.ico         # Generado · 16/32/48 px
│   ├── apple-touch-icon.png# Generado · 180×180
│   ├── icon-192.png        # Generado · manifest
│   ├── icon-512.png        # Generado · manifest
│   └── og-image.jpg        # Generado · 1200×630 (og:image)
├── tools/
│   └── build-assets.ps1    # Regenera los PNG/ICO a partir de los SVG/HTML fuente
├── robots.txt              # Incluye permisos explícitos para crawlers de IA
├── sitemap.xml
├── llms.txt                # Resumen estructurado para motores generativos (GEO/LLMO)
└── site.webmanifest
```

## ▶️ Ver en local

No hace falta nada más que un servidor estático. Por ejemplo:

```powershell
# Con Node
npx serve -l 8099 .

# Con Python
python -m http.server 8080
```

Abrí <http://localhost:8099> (o el puerto que corresponda).

## 🎨 Regenerar imágenes e iconos

Los PNG y el `.ico` se generan desde las fuentes SVG/HTML con **Microsoft Edge en modo headless**
(no requiere ImageMagick, Inkscape ni dependencias de npm):

```powershell
powershell -ExecutionPolicy Bypass -File tools\build-assets.ps1
```

Qué regenera:

| Salida | Fuente |
|---|---|
| `assets/og-image.jpg` (1200×630) | `assets/og-source.html` |
| `assets/apple-touch-icon.png` (180×180) | `assets/icon-square.svg` |
| `assets/icon-192.png`, `assets/icon-512.png` | `assets/icon-square.svg` |
| `assets/favicon.ico` (16/32/48) | `assets/favicon.svg` |

## 🚀 Publicar (gratis)

Opción A — **GitHub Pages** (es la que está activa hoy):
1. `git push` a `main`.
2. *Settings → Pages → Deploy from a branch* → rama `main` / raíz.

Opción B — **Netlify o Cloudflare Pages**: conectás el repo y publica solo.

## 🌐 Dominio propio

El sitio funciona hoy en la URL de GitHub Pages (proyecto). Cuando se compre el dominio
definitivo, hay que reemplazar la base en **estos archivos** (es el único cambio necesario):

| Archivo | Dónde |
|---|---|
| `index.html` | `canonical`, `og:url`, `twitter:url` y los `url`/`@id`/`image`/`logo` del JSON-LD |
| `robots.txt` | línea `Sitemap:` |
| `sitemap.xml` | `<loc>` y `<image:loc>` |
| `llms.txt` | "Sitio web" y "Cómo citar este sitio" |

En el `<head>` de `index.html` hay un comentario `DOMINIO:` que recuerda exactamente esto.

- Netlify / Cloudflare Pages: *Domain settings → Add custom domain*.
- GitHub Pages: *Settings → Pages → Custom domain* + registro CNAME.

El HTTPS se emite automáticamente en los tres casos.

> **Nota sobre `robots.txt` y `sitemap.xml` en GitHub Pages:** en un sitio de proyecto
> (`usuario.github.io/repo/`) estos archivos se sirven bajo el subdirectorio, y los buscadores
> sólo leen `robots.txt` en la raíz del dominio. Es decir: **quedan plenamente efectivos al
> conectar un dominio propio** (o al desplegar en Netlify/Cloudflare, donde viven en la raíz).

## ✏️ Qué actualizar con datos confirmados

Los datos reales actuales están tomados de Google Maps, 1122 y el Instagram del taller.
Verificá y ajustá en `index.html`:

| Dónde | Qué | Valor actual |
|---|---|---|
| `index.html` (schema + Ubicación + mapa) | Dirección | Paysandú 255, Rivera |
| `index.html` (schema + Ubicación + FAQ) | Horario | Lunes a viernes 8:30–18:30 |
| `index.html` (schema + footer) | E-mail | jonahiggie@gmail.com |
| `js/main.js` → `SCHEDULE` | Horario (cartel "Abierto/Cerrado") | `[8.5, 18.5]` |

> ⚠️ **El horario tiene dos fuentes en conflicto** (Google dice 8:00–18:30, el 1122 indica apertura 9:00).
> Confirmar con el taller y actualizar en los **cuatro** lugares de la tabla.
>
> Se quitó la coordenada `geo` del JSON-LD al cambiar la dirección: si pasás las coordenadas exactas
> de Paysandú 255, se vuelven a agregar.

## 🔁 Reemplazar los placeholders por material propio

- **Fotos:** crear `assets/foto-taller.webp` y `assets/foto-portada.webp`, y usarlas en la sección
  *El taller* (`<img>` en `.about-img`) y en el hero.
- **Logo:** reemplazar `assets/logo.svg` y los bloques inline del `<header>` y del footer.
- Todas las imágenes actuales son SVG/CSS generados: no hay fotos de stock ni licencias que pagar.

## 🔎 SEO

- `<title>` de 51 caracteres y `meta description` de 159, dentro de los límites de Google.
- `canonical`, `robots` (`index, follow, max-image-preview:large`), Open Graph y Twitter Cards completos.
- Datos estructurados JSON-LD (`@graph`): **WebSite**, **AutoRepair** (dirección, horarios, teléfono,
  `areaServed`, `sameAs`, `contactPoint` y **catálogo de los 11 servicios**) y **FAQPage**.
- Jerarquía de encabezados correcta (un `h1`, sin saltos de nivel) y **FAQ con acordeón nativo**
  (`<details>`), que respalda el schema `FAQPage`.
- `sitemap.xml` (con extensión de imagen) y `robots.txt`.

## 🤖 GEO / LLMO (motores generativos)

- **`llms.txt`** en la raíz: resumen en Markdown con NAP, horarios, servicios, FAQ y sugerencia de cita,
  para que ChatGPT, Perplexity, Gemini y AI Overviews puedan leer y citar el negocio sin ambigüedad.
- **`robots.txt`** con permisos explícitos para `GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `ClaudeBot`,
  `PerplexityBot`, `Google-Extended`, `Applebot-Extended`, `Bingbot`, `Amazonbot`, `meta-externalagent`, `CCBot`.
- Datos **consistentes** entre texto visible, JSON-LD y `llms.txt` (mismo nombre, dirección, teléfono,
  horario y servicios en los tres lugares) — clave para que los modelos citen información correcta.

## 🔗 Presentación al compartir el link

- `og:image` apunta a **`assets/og-image.jpg`** (1200×630, JPEG) — WhatsApp, Facebook, X, Telegram e
  Instagram **ignoran los SVG**, por eso la imagen es raster.
- `og:image:width`, `og:image:height`, `og:image:type` y `og:image:alt` declarados; `twitter:card`
  en `summary_large_image`.
- Íconos completos: `favicon.ico` (16/32/48), `favicon.svg`, `apple-touch-icon.png` (180×180) y
  `site.webmanifest` (192/512, `theme_color` rojo de marca).

> Al cambiar la imagen social, algunos servicios guardan caché: se refresca desde el
> [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/) (también reindexa WhatsApp).

## 🧾 Incluido por defecto

- Diseño responsive (mobile-first), paleta roja y ritmo editorial de secciones claras/oscuras.
- Tipografía **Montserrat** (títulos 800/900) + **Inter** (texto), micro-etiquetas con línea roja.
- Sección destacada de **Auxilio 24 hs** (autos, camionetas y camiones pequeños) con CTA a WhatsApp/teléfono.
- Hero con **disco de freno girando** en SVG animado (sin imágenes externas ni stock).
- Botón flotante de WhatsApp + enlaces a Instagram y Facebook.
- Accesibilidad: `prefers-reduced-motion`, `:focus-visible`, skip-link, landmarks ARIA,
  acordeón nativo y contraste verificado (0 fallos).
- Indicador en vivo "Abierto ahora / Cerrado" con la hora de Rivera (`America/Montevideo`).
- Firma discreta **FB Informática** en el footer (según identidad de marca).

## 📊 Auditoría (última corrida)

| Chequeo | Resultado |
|---|---|
| Lighthouse — Accesibilidad | **100** |
| Lighthouse — Buenas prácticas | **100** |
| Lighthouse — SEO | **100** |
| Errores de consola | 0 |
| Contraste AA (escaneo propio elemento por elemento) | 0 fallos |
| IDs duplicados | 0 |
| Scroll horizontal en 375 px y 1000 px | No |
| JSON-LD | Válido (WebSite · AutoRepair · FAQPage) |
| Peso total del sitio | ~295 KB (incluye fuentes de imagen y assets generados) |

---

Desarrollado por **[FB Informática](https://www.fbinformaticauy.com)**.
