# TOP CAR — Mecánica automotriz en Rivera

Landing estática bilingüe para el taller TOP CAR. HTML, CSS y JavaScript nativos; sin dependencias de ejecución, formularios externos, trackers ni cookies propias.

## Vista previa y edición

```powershell
npm run build
npm test
npm run preview
```

Abrir http://127.0.0.1:8123/topcarrivera/ o http://127.0.0.1:8123/topcarrivera/pt/.
El servidor se limita a localhost y reproduce el subdirectorio de GitHub Pages. Detener con Ctrl+C.

- `tools/build-site.py`: contenido español/portugués, metadatos, JSON-LD, sitemap y robots. `tools/real_photos.py` contiene los textos y metadatos de las fotografías reales y Auxilio BAIA. Es la fuente de edición; no editar a mano los HTML generados.
- `css/styles.css`: diseño responsive, estados de foco y movimiento reducido.
- `js/main.js`: menú, carrusel, búsqueda tolerante, horario y mapa bajo demanda.
- `index.html` y `pt/index.html`: páginas completas indexables sin ejecutar JavaScript.
- `assets/photos/real/`: seis fotografías reales optimizadas, variantes de 480, 800 y hasta 1280 px sin ampliar el original; procedencia en `real/SOURCES.md`. Los originales de WhatsApp se mantienen locales, excluidos por `.gitignore`.
- `assets/fonts/`: fuentes locales reducidas y licencias OFL.
- `tools/validate-site.py`: comprobaciones de archivos, anclas, idioma, metadatos, JSON-LD, sitemap y robots.
- `tools/hours.test.cjs`: pruebas de horarios y zona de Rivera, incluidos apertura, cierre y fin de semana.

Python 3 para regenerar contenido; Node 22.12+ para las herramientas de auditoría. El hosting solo necesita servir los archivos estáticos, sin Python ni Node.

## Diseño y comportamiento

Identidad grafito, blanco cálido y rojo. Tipografía Barlow Condensed e Inter. Portada fotográfica, seis grupos de servicios, explicación del diagnóstico, proceso, auxilio 24 hs, frontera, ubicación y preguntas frecuentes.

El carrusel cambia cada 6,5 segundos con fundido. Tiene controles anterior/siguiente y pausa; se pausa al recibir foco, al pasar el mouse, fuera de pantalla y con la pestaña oculta. Respeta `prefers-reduced-motion`. Solo cambian las fotografías: los textos y enlaces permanecen estables.

El buscador normaliza tildes y acepta sinónimos españoles/portugueses, variantes locales y un error de edición en palabras largas. Casos comprobados: `embriague`, `suspencion`, `nao pega`, `barulho ao frear`. No diagnostica: filtra servicios. Los alias viven en la lógica de búsqueda, no como texto SEO oculto.

Sin JavaScript se mantienen servicios, menús, enlaces, preguntas y la primera foto. El mapa de Google se carga solo al solicitarlo; el enlace «Cómo llegar» funciona también sin JavaScript.

## SEO local, GEO y LLMO

- Páginas independientes en español de Uruguay y portugués de Brasil.
- Canonical propio por idioma y `hreflang` recíproco `es-UY`, `pt-BR`, `x-default`.
- Dirección, contacto y horarios consistentes entre contenido visible, datos estructurados y `llms.txt`.
- JSON-LD `AutoRepair`, catálogo de servicios, `WebSite`, `WebPage` y `FAQPage`, sin valoraciones ni certificaciones inventadas.
- Preguntas por síntomas y términos naturales: frenos/freios, embrague/embreagem, mantenimiento/revisão y auxilio/socorro.
- Distinción explícita: local en Rivera, Uruguay; visitantes de Livramento pueden consultar. La cobertura del auxilio se confirma según la ubicación, sin inventar servicio en Brasil.
- Metadatos sociales, textos alternativos y enlaces rastreables.
- No se agregan faltas artificiales a los textos ni páginas repetidas para captar variantes de una misma búsqueda.

`llms.txt` es un resumen complementario. No garantiza que buscadores o asistentes lo utilicen, ni asegura citas. Para las funciones de IA de Google siguen siendo relevantes las prácticas fundamentales de SEO y el contenido útil. El marcado de FAQ tampoco garantiza resultados enriquecidos.

Referencias oficiales:
- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/essentials/spam-policies#keyword-stuffing
- https://support.google.com/business/answer/7091
- https://developers.google.com/search/docs/specialty/international/localized-versions

## Sitemap y robots.txt

`tools/build-site.py` genera ambos archivos con la misma URL base que los canonical y los identificadores de la entidad.

El sitemap incluye solo las dos páginas canónicas indexables y, dentro de ellas, las seis imágenes reales mediante la extensión de imágenes. No incluye anclas, herramientas, fotos ilustrativas como páginas, prioridades inventadas ni frecuencias sin fundamento. Ambas entradas tienen los mismos alternates recíprocos. `lastmod` corresponde a la fecha de esta revisión de contenido; actualizarlo cuando cambie sustancialmente el contenido, no cada vez que se ejecute el generador.

`robots.txt` permite rastrear el contenido público y los recursos CSS/JS. El grupo `User-agent: *` también cubre crawlers de IA que respeten robots; no hace falta duplicar docenas de grupos equivalentes. Incluye la URL absoluta del sitemap. Permitir rastreo no garantiza indexación ni regula por sí solo los usos posteriores del contenido.

**Dominio actual:** https://topcarrivera.com/ está conectado a GitHub Pages mediante CNAME. robots.txt y sitemap.xml se sirven en la raíz del dominio. Canonical, hreflang, Open Graph y datos estructurados usan el mismo dominio.

Referencia: https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt

Al cambiar de dominio, modificar `BASE` en `tools/build-site.py`, regenerar y actualizar la URL base esperada en el validador. Crear/configurar CNAME y DNS en el hosting por separado.

## Auditorías reproducibles

```powershell
npm install
npm test
# En otra terminal, con npm run preview activo:
npm run audit
```

`npm run audit` ejecuta Lighthouse en ambas páginas, móvil y escritorio. Exige más de 90 puntos en todas las categorías devueltas y guarda los informes HTML/JSON en `.cache/`. En otra plataforma, definir `CHROME_PATH` con la ruta de Chrome.

Los puntajes son mediciones de laboratorio sobre localhost. Deben repetirse sobre HTTPS en producción; latencia, caché del hosting y dispositivo pueden cambiar el rendimiento. El resultado de accesibilidad automatizado no sustituye una revisión humana ni constituye certificación WCAG.

La última ejecución y las comprobaciones manuales se documentan en `AUDIT.md`.

## Publicación y pendientes del negocio

La URL pública es https://topcarrivera.com/. GitHub Pages publica la rama `main`; los cambios enviados al remoto disparan el despliegue. Mantener `node_modules`, `.cache` y los reportes de auditoría fuera del despliegue. `.nojekyll` permite servir archivos estáticos en GitHub Pages.

Desde el 02/11/2026 la portada, la sección técnica y el bloque de auxilio utilizan fotografías reales. Una galería de cuatro imágenes permite ampliarlas en un diálogo con controles, teclado y retorno del foco. Sin JavaScript los enlaces abren las imágenes. El nombre Auxilio BAIA aparece junto a TOP CAR en el bloque de asistencia, FAQ, metadatos, catálogo estructurado y llms.txt.

Para regenerar las copias con los originales presentes: `python tools/prepare-photos.py` (requiere Pillow). Después ejecutar `npm run build`. La compilación habitual no necesita los JPEG originales ni Pillow: utiliza las variantes y el manifiesto ya incluidos. No subir automáticamente el llavero, capturas de WhatsApp o videos; agregar nuevas imágenes solo tras una selección. Los archivos antiguos de stock permanecen como material histórico y no se cargan en las páginas.

El horario de 8:30 a 18:30 proviene de la versión anterior y sigue pendiente de confirmación por el taller (el README anterior registraba fuentes externas en conflicto). Confirmar también feriados y cobertura del auxilio. Si cambia el horario, actualizar el contenido bilingüe, JSON-LD y `workshopStatus` y sus pruebas. No se afirma disponibilidad por feriados.

Para completar el posicionamiento local fuera de la web: mantener el Perfil de Empresa de Google verificado, su categoría y servicios correctos, el mismo nombre/dirección/teléfono, fotos reales y reseñas genuinas. El sitio por sí solo no puede garantizar una posición en Google Maps ni en respuestas de IA.

Diseño y desarrollo: FB Informática — https://www.fbinformaticauy.com
