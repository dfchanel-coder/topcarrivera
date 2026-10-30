# Auditoría TOP CAR — 30/10/2026

Revisión local del rediseño bilingüe. No se realizó publicación ni una auditoría del hosting público.

## Lighthouse 13.6.0

Se ejecutó `node tools/audit.mjs` sobre la ruta de proyecto de la vista previa. Chrome headless, configuración predeterminada móvil y preset desktop. Sin excluir categorías o reglas para mejorar resultados.

| Página | Dispositivo | Rendimiento | Accesibilidad | Buenas prácticas | SEO | Agentic browsing |
|---|---|---:|---:|---:|---:|---:|
| Español | Móvil | 99 | 100 | 100 | 100 | 98 |
| Español | Escritorio | 100 | 100 | 100 | 100 | 100 |
| Portugués | Móvil | 99 | 100 | 100 | 100 | 98 |
| Portugués | Escritorio | 100 | 100 | 100 | 100 | 100 |

Móvil: LCP 1,0 s; CLS 0,08; TBT 0 ms. Escritorio: LCP 0,5 s; CLS 0; TBT 30 ms.
Todos los puntajes superan 90. Los resultados son de laboratorio y dependen del entorno. No constituyen certificación WCAG, una calificación GTmetrix ni una garantía de posicionamiento. La categoría Agentic browsing evalúa características técnicas; no mide si un modelo citará el negocio.

Informes locales (ignorados por Git):
- `.cache/lighthouse-es-mobile.report.html` y `.json`
- `.cache/lighthouse-es-desktop.report.html` y `.json`
- `.cache/lighthouse-pt-mobile.report.html` y `.json`
- `.cache/lighthouse-pt-desktop.report.html` y `.json`
- `.cache/audit-summary.json`

## Integridad y funcionamiento

- 10 pruebas de horario aprobadas: medianoche, antes de abrir, apertura, antes del cierre, cierre, viernes, fin de semana, UTC y portugués.
- Dos páginas con un H1, IDs únicos, idioma correcto y enlaces internos válidos.
- 52 referencias locales comprobadas, incluidos archivos, rutas y anclas.
- JSON-LD válido en ambos idiomas, entidad de negocio consistente y seis preguntas por página.
- Sitemap XML válido, dos URLs canónicas y alternates recíprocos en ambas entradas.
- Robots con sintaxis simple y URL absoluta correcta del sitemap. Sin bloqueo de CSS/JS.
- Sin errores detectados en la consola de la vista previa durante las comprobaciones.
- Revisión visual de escritorio y móvil. Sin desborde horizontal de documento en anchos de 320, 390 y 768 px comprobados.
- Menú móvil: abre, actualiza `aria-expanded`, cierra con Escape y devuelve el foco.
- Búsqueda: «No arranca» devuelve electricidad; «embriague» devuelve motor/transmisión; «suspencion» devuelve frenos/suspensión; «nao pega» devuelve electricidad; «barulho ao frear» devuelve freios/suspensão en portugués. Consulta sin coincidencias presenta contacto y permite limpiar.
- Cambio de idioma navega a la página portuguesa; el acordeón muestra su respuesta correspondiente.
- Controles del carrusel revisados; fotografías diferidas con transición y pausa. Reducción de movimiento contemplada en CSS y JavaScript.
- Los enlaces WhatsApp se verificaron como URLs con destinatario y texto; no se enviaron mensajes ni se realizaron llamadas.

## Límite de robots en GitHub Pages

El proyecto se sirve bajo `/topcarrivera/`. El robots con autoridad para el origen vive en `https://dfchanel-coder.github.io/robots.txt`, fuera del alcance de este repositorio. El archivo preparado aquí sirve directamente al conectar un dominio propio; mientras tanto se puede enviar el sitemap del proyecto a Search Console. No se modificó el sitio de usuario ni el Perfil de Empresa de Google.

## Datos pendientes de confirmación

Se conserva el horario heredado de 8:30 a 18:30. El README anterior documentaba discrepancias entre fuentes; confirmar con el taller antes de publicar. Las fotografías son ilustrativas y están identificadas. No se inventaron calificaciones, reseñas, títulos de ingeniería ni marcas de equipamiento.
