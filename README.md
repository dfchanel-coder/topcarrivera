# TOP CAR — One Page | Taller Mecánico en Rivera, Uruguay

Sitio de una sola página para **TOP CAR — Mecánica Automotriz** (Rivera, Uruguay).
HTML + CSS + JavaScript vanilla, sin build ni dependencias: se sube a cualquier hosting estático y se apunta el dominio.

---

## 📁 Estructura

```
TopCar/
├── index.html          # Página única (todo el contenido y el SEO)
├── css/
│   └── styles.css      # Estilos (tema oscuro, responsive, animaciones)
├── js/
│   └── main.js         # Menú, scroll, sección activa y estado abierto/cerrado
└── assets/
    ├── logo.svg
    ├── favicon.svg
    └── og-cover.svg    # Imagen para compartir en redes (Open Graph)
```

## ▶️ Ver en local

No hace falta nada más que un servidor estático. Por ejemplo:

```powershell
# Con Python
python -m http.server 8080

# Con Node
npx serve .
```

Abrí <http://localhost:8080> (o el puerto que corresponda).

## 🚀 Publicar (gratis)

Opción A — **GitHub Pages**:
1. `git init && git add . && git commit -m "Sitio TOP CAR"`
2. Creá el repo en GitHub y `git push`
3. En *Settings → Pages → Deploy from a branch* elegí `main` / raíz.

Opción B — **Netlify o Cloudflare Pages**: conectás el repo y publica solo.

## 🌐 Dominio

- Comprás el dominio (ej. `topcar.uy`) en cualquier registrador.
- En Netlify: *Domain settings → Add custom domain* → te da los DNS a configurar.
- En Cloudflare Pages: igual, y además te sirve de proxy/CDN y certificado SSL automático.
- En GitHub Pages: *Settings → Pages → Custom domain* + un registro CNAME.

El HTTPS se emite automáticamente en los tres casos.

## ✏️ Qué actualizar con datos confirmados

Los datos reales actuales están tomados de Google Maps, 1122 y el Instagram del taller.
Verificá y ajustá en `index.html`:

| Dónde | Qué | Valor actual |
|---|---|---|
| `index.html` (schema + sección Ubicación + mapa) | Dirección | Paysandú 255, Rivera |
| `index.html` (schema + sección Ubicación) | Horario | Lunes a viernes 8:30–18:30 |
| `index.html` (schema) | E-mail | jonahiggie@gmail.com |
| `js/main.js` → `SCHEDULE` | Horario (para el cartel "Abierto/Cerrado") | `[8.5, 18.5]` |
| `index.html` | Enlace canónico `https://topcar.uy/` | reemplazar por el dominio real |

> El horario tiene dos fuentes en conflicto (Google dice 8:00–18:30, el 1122 indica apertura 9:00): **confirmar con el taller**.
> Se quitó la coordenada `geo` del JSON-LD al cambiar la dirección: si querés, pasame las coordenadas exactas de Paysandú 255 y las vuelvo a agregar.

## 🔁 Reemplazar los placeholders por material propio

- **Fotos:** crear `assets/foto-taller.webp` y `assets/foto-portada.webp`, y usarlas en la sección *El taller* (`<img>` en `.about-img`) y en el hero.
- **Logo:** reemplazar `assets/logo.svg` y los bloques inline del `<header>` y del footer.
- Todas las imágenes actuales son SVG/CSS generados: no hay fotos de stock ni licencias que pagar.

## 🧾 Incluido por defecto

- Diseño responsive (mobile-first), tema oscuro con paleta roja automotriz.
- Sección destacada de **Auxilio 24 hs** (autos, camionetas y camiones pequeños) con CTA directo a WhatsApp/teléfono.
- Hero con **disco de freno girando** y **auto de perfil** con barrido de luz y camino en movimiento (SVG animado, sin imágenes externas).
- SEO on-page: title, description, canonical, Open Graph y **JSON-LD `AutoRepair`** con dirección, horarios y rating de Google.
- `robots.txt` y `sitemap.xml` listos (actualizar el dominio cuando se compre).
- Botón flotante de WhatsApp + enlaces a Instagram y Facebook.
- Accesibilidad: `prefers-reduced-motion`, `:focus-visible`, skip-link, landmarks ARIA.
- Indicador en vivo "Abierto ahora / Cerrado" calculado con la hora de Rivera (`America/Montevideo`).
- Auditoría Lighthouse sobre el sitio: **Accesibilidad 100 · SEO 100 · Buenas prácticas 100**, sin fallos.

## ⚠️ Pendiente: imagen para compartir en redes

`assets/og-cover.svg` funciona bien en la mayoría de los navegadores, pero
**WhatsApp, Facebook e Instagram ignoran los SVG**. Antes de publicar:
hacer una captura PNG de 1200×630 del hero (o pedirme el archivo) y cambiar
`<meta property="og:image" content="assets/og-cover.svg">` por esa imagen.
