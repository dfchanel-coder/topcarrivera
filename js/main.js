/* Workshop hours use the shop's time zone, regardless of the visitor's zone. */
function workshopStatus(date, pt = false) {
  const parts = new Intl.DateTimeFormat('en-US', { timeZone:'America/Montevideo', weekday:'short', hour:'2-digit', minute:'2-digit', hourCycle:'h23' }).formatToParts(date);
  const part = type => parts.find(p => p.type === type)?.value;
  const day = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(part('weekday'));
  const time = Number(part('hour')) + Number(part('minute')) / 60;
  const working = day >= 1 && day <= 5;
  const open = working && time >= 8.5 && time < 18.5;
  let text;
  if (open) text = pt ? 'Aberto agora · fecha às 18h30' : 'Abierto ahora · cierra 18:30';
  else if (working && time < 8.5) text = pt ? 'Fechado · abre hoje às 8h30' : 'Cerrado · abre hoy 8:30';
  else {
    const tomorrow = (day >= 1 && day <= 4) || day === 0;
    text = pt ? `Fechado · abre ${tomorrow ? 'amanhã' : 'segunda'} às 8h30` : `Cerrado · abre ${tomorrow ? 'mañana' : 'lunes'} 8:30`;
  }
  return { open, text };
}
if (typeof module !== 'undefined') module.exports = { workshopStatus };

/* TOP CAR: progressive enhancement, forgiving search and accessible carousel. */
(() => {
  'use strict';
  if (typeof document === 'undefined') return;
  const pt = document.documentElement.lang === 'pt-BR';
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  document.documentElement.classList.add('js');
  document.getElementById('year').textContent = new Date().getFullYear();
  const menu = document.querySelector('.menu-toggle');
  const nav = document.getElementById('mainNav');
  menu.hidden = false;
  const setMenu = (open, restore = false) => {
    nav.classList.toggle('is-open', open);
    menu.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-label', pt ? (open ? 'Fechar menu' : 'Abrir menu') : (open ? 'Cerrar menú' : 'Abrir menú'));
    if (restore) menu.focus();
  };
  menu.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
  nav.addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && nav.classList.contains('is-open')) setMenu(false, true); });
  document.addEventListener('click', e => { if (!e.target.closest('.site-header')) setMenu(false); });
  matchMedia('(min-width: 761px)').addEventListener('change', () => setMenu(false));
  document.querySelector('main').addEventListener('focusin', () => setMenu(false));

  // Only photos rotate, never the headings or links. Autoplay pauses offscreen.
  const carousel = document.querySelector('.hero-media');
  const slides = [...carousel.querySelectorAll('.hero-slide')];
  const pause = carousel.querySelector('[data-carousel="pause"]');
  const count = carousel.querySelector('.slide-count');
  carousel.querySelector('.carousel-controls').hidden = false;
  let active = 0, timer = null, paused = motion.matches, hover = false, focused = false, visible = true, request = 0;
  function updatePause() {
    pause.setAttribute('aria-label', paused ? pause.dataset.play : pause.dataset.pause);
    pause.firstElementChild.textContent = paused ? '▶' : 'Ⅱ';
  }
  function schedule() {
    clearTimeout(timer);
    if (!paused && !hover && !focused && visible && !document.hidden) timer = setTimeout(() => show(active + 1), 6500);
  }
  async function show(index) {
    const token = ++request;
    const next = (index + slides.length) % slides.length;
    const img = slides[next].querySelector('img');
    if (img.dataset.src) { img.srcset = img.dataset.srcset; img.src = img.dataset.src; delete img.dataset.src; }
    try { await img.decode(); } catch { schedule(); return; }
    if (token !== request) return;
    slides.forEach((slide, i) => { slide.classList.toggle('is-active', i === next); slide.setAttribute('aria-hidden', String(i !== next)); });
    active = next;
    count.innerHTML = `0${active + 1} <span>/ 02</span>`;
    schedule();
  }
  carousel.addEventListener('click', e => {
    const button = e.target.closest('[data-carousel]');
    if (!button) return;
    if (button.dataset.carousel === 'pause') { paused = !paused; updatePause(); schedule(); }
    else { paused = true; updatePause(); show(active + (button.dataset.carousel === 'next' ? 1 : -1)); }
  });
  carousel.addEventListener('mouseenter', () => { hover = true; schedule(); });
  carousel.addEventListener('mouseleave', () => { hover = false; schedule(); });
  carousel.addEventListener('focusin', () => { focused = true; schedule(); });
  carousel.addEventListener('focusout', e => { focused = carousel.contains(e.relatedTarget); schedule(); });
  document.addEventListener('visibilitychange', schedule);
  motion.addEventListener('change', () => { paused = motion.matches; updatePause(); schedule(); });
  if ('IntersectionObserver' in window) new IntersectionObserver(entries => { visible = entries[0].isIntersecting; schedule(); }).observe(carousel);
  updatePause();
  window.addEventListener('load', schedule, { once: true });

  // Search-only aliases; no hidden SEO keywords or duplicated doorway content.
  const aliases = {
    diagnostico: 'diagnostico computarizado escaner scanner scaner automotriz inyeccion injecao injeccion injeção eletronica electronica sensores bobinas inyectores bicos check engine luz motor tablero painel perde fuerza pierde forca falhando falha falla tironea ratea consumo gasolina nafta',
    frenos: 'frenos freios freio freno pastillas pastilhas discos amortiguadores amortecedores suspension suspensao bujes buchas rotulas pivôs ruido frenar barulho frear chilla chirrido golpes pozos rangido',
    motor: 'motor mecanica mecanico geral taller oficina embrague embriague embreagem embreague embriage caja cambios cambio marchas transmissao transmision correa correia distribucion distribuicao junta reparacion conserto pierde fuerza perde forca falha falla',
    mantenimiento: 'aceite oleo óleo filtros filtro service servis servise mantenimiento manutencao revisao revision troca cambio preventivo viagem viaje ruta estrada',
    electricidad: 'no arranca nao pega no prende nao liga bateria electrica eletrica electricidad alternador arranque partida carga calienta esquenta aquecimento temperatura refrigeracion arrefecimento radiador agua termostato aire ar condicionado aire acondicionado no enfria nao gela calefaccion',
    alineacion: 'alineacion alineamiento alinhamento balanceo balanceamento pneus neumaticos cubiertas ruedas rodas volante vibra vibracion vibracao vai lado va lado puxa lado desgaste'
  };
  const normalize = s => s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9\s]/g, ' ').replace(/\s+/g, ' ').trim();
  const stop = new Set('mi meu me el la los las un una o a os as um uma de del do da en em que se al ao con com para por le lo esta y e muy muito hace faz eu tengo estou tiene ta no nao'.split(' '));
  function distanceOne(a, b) {
    if (Math.abs(a.length - b.length) > 1) return false;
    let i = 0, j = 0, changes = 0;
    while (i < a.length && j < b.length) {
      if (a[i] === b[j]) { i++; j++; continue; }
      if (++changes > 1) return false;
      if (a.length >= b.length) i++;
      if (b.length >= a.length) j++;
    }
    return changes + (i < a.length || j < b.length ? 1 : 0) <= 1;
  }
  const cards = [...document.querySelectorAll('[data-service]')];
  const words = new Map(cards.map(card => [card, normalize(card.textContent + ' ' + aliases[card.dataset.service]).split(' ')]));
  const field = document.getElementById('service-query');
  const status = document.getElementById('search-status');
  const empty = document.querySelector('.no-results');
  document.querySelector('.service-search').hidden = false;
  document.querySelector('.search-note').hidden = false;
  function search() {
    const tokens = normalize(field.value).split(' ').filter(w => w.length > 1 && !stop.has(w));
    let found = 0;
    for (const card of cards) {
      const list = words.get(card);
      const matches = !tokens.length || tokens.every(t => list.some(w => w === t || (t.length >= 4 && w.startsWith(t)) || (t.length >= 5 && distanceOne(t, w))));
      card.hidden = !matches;
      if (matches) found++;
    }
    empty.hidden = found > 0;
    document.querySelector('.service-grid').hidden = !found;
    document.querySelector('.service-grid').classList.toggle('is-filtered', tokens.length > 0);
    status.textContent = pt ? `${found} serviços encontrados.` : `${found} servicios encontrados.`;
  }
  let searchTimer;
  field.addEventListener('input', () => { clearTimeout(searchTimer); searchTimer = setTimeout(search, 120); });
  document.querySelectorAll('[data-query]').forEach(button => button.addEventListener('click', () => { field.value = button.dataset.query; search(); }));
  document.getElementById('clear-search').addEventListener('click', () => { field.value = ''; search(); field.focus(); });

  const statusEl = document.getElementById('openStatus');
  function updateStatus() {
    const {open, text} = workshopStatus(new Date(), pt);
    statusEl.classList.toggle('is-open', open);
    statusEl.textContent = text;
    statusEl.title = pt ? 'Horário habitual; consulte sobre feriados.' : 'Horario habitual; consultá por feriados.';
  }
  updateStatus();
  setInterval(updateStatus, 60000);
  // Third-party map is loaded only on request.
  const mapButton = document.querySelector('.map-load');
  mapButton.hidden = false;
  mapButton.addEventListener('click', () => {
    const frame = document.createElement('iframe');
    frame.title = mapButton.dataset.title;
    frame.src = 'https://www.google.com/maps?q=Paysand%C3%BA%20255%2C%20Rivera%2C%20Uruguay&output=embed';
    frame.referrerPolicy = 'no-referrer-when-downgrade';
    frame.allowFullscreen = true;
    frame.tabIndex = 0;
    document.getElementById('map-slot').replaceChildren(frame);
    document.querySelector('.map-card').classList.add('map-loaded');
    mapButton.hidden = true;
    frame.focus();
  }, { once:true });
})();
