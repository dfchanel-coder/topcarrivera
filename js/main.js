/* =========================================================
   TOP CAR — One-page | JS
   Sin dependencias. Vanilla JS.
   ========================================================= */
(function () {
  "use strict";

  const header = document.getElementById("siteHeader");
  const navToggle = document.getElementById("navToggle");
  const mainNav = document.getElementById("mainNav");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Guardia: si el script fallara en cualquier punto, el contenido jamás debe
  // quedar oculto detrás de las animaciones de entrada.
  window.addEventListener("error", () => {
    document.querySelectorAll(".reveal").forEach((el) => el.classList.add("is-visible"));
  });

  /* ---------- Año dinámico en el footer ---------- */
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* ---------- Header con fondo al hacer scroll ---------- */
  const onScroll = () => {
    if (!header) return;
    header.classList.toggle("scrolled", window.scrollY > 12);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Menú móvil ---------- */
  if (navToggle && mainNav) {
    const setMenu = (open) => {
      mainNav.classList.toggle("open", open);
      navToggle.setAttribute("aria-expanded", String(open));
      navToggle.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
    };

    navToggle.addEventListener("click", () => {
      setMenu(navToggle.getAttribute("aria-expanded") !== "true");
    });

    mainNav.addEventListener("click", (e) => {
      if (e.target.closest("a")) setMenu(false);
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") setMenu(false);
    });

    window.addEventListener("resize", () => {
      if (window.innerWidth > 860) setMenu(false);
    });
  }

  /* ---------- Reveal on scroll ---------- */
  const revealEls = Array.from(document.querySelectorAll(".reveal"));
  const revealAll = () => revealEls.forEach((el) => el.classList.add("is-visible"));
  const revealInViewport = (factor) =>
    revealEls.forEach((el) => {
      if (el.getBoundingClientRect().top < window.innerHeight * factor) {
        el.classList.add("is-visible");
      }
    });

  if (!reduceMotion && "IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((entry, i) => {
          if (!entry.isIntersecting) return;
          // Pequeño stagger para elementos que entran juntos
          setTimeout(() => entry.target.classList.add("is-visible"), i * 70);
          obs.unobserve(entry.target);
        });
      },
      { threshold: 0.14, rootMargin: "0px 0px -8% 0px" }
    );
    revealEls.forEach((el) => revealObserver.observe(el));

    // Red de seguridad 1: lo que ya está en pantalla al cargar se muestra sí o sí.
    revealInViewport(1.1);

    // Red de seguridad 2: pestañas abiertas en segundo plano no reciben callbacks.
    // Al volver a primer plano, repasamos lo que quedó a la vista.
    document.addEventListener("visibilitychange", () => {
      if (!document.hidden) revealInViewport(1.25);
    });
  } else {
    revealAll();
  }

  /* ---------- Link activo según sección visible ---------- */
  const navLinks = Array.from(mainNav ? mainNav.querySelectorAll('a[href^="#"]') : []);
  const sections = navLinks
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);

  if ("IntersectionObserver" in window && sections.length) {
    const sectionObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          navLinks.forEach((link) => {
            link.classList.toggle(
              "active",
              link.getAttribute("href") === "#" + entry.target.id
            );
          });
        });
      },
      { rootMargin: "-45% 0px -50% 0px" }
    );
    sections.forEach((s) => sectionObserver.observe(s));
  }

  /* ---------- Estado abierto / cerrado (hora de Rivera) ---------- */
  const statusEl = document.getElementById("openStatus");
  if (statusEl) {
    const SCHEDULE = [
      null,              // 0 domingo
      [8.5, 18.5],       // 1 lunes
      [8.5, 18.5],       // 2 martes
      [8.5, 18.5],       // 3 miércoles
      [8.5, 18.5],       // 4 jueves
      [8.5, 18.5],       // 5 viernes
      null               // 6 sábado
    ];
    const DAY_NAMES = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];

    const fmtHour = (h) => {
      const hh = Math.floor(h);
      const mm = h % 1 ? "30" : "00";
      return hh + ":" + mm;
    };

    const getLocalNow = () => {
      try {
        const parts = new Intl.DateTimeFormat("es-UY", {
          timeZone: "America/Montevideo",
          weekday: "short",
          hour: "2-digit",
          minute: "2-digit",
          hour12: false
        }).formatToParts(new Date());
        const get = (type) => parts.find((p) => p.type === type)?.value || "";
        const dayMap = { dom: 0, lun: 1, mar: 2, mié: 3, jue: 4, vie: 5, sáb: 6 };
        const day = dayMap[get("weekday").toLowerCase().replace(".", "")];
        const hour = parseInt(get("hour"), 10) % 24;
        const minute = parseInt(get("minute"), 10);
        return { day, time: hour + minute / 60 };
      } catch (err) {
        const now = new Date();
        return { day: now.getDay(), time: now.getHours() + now.getMinutes() / 60 };
      }
    };

    const updateStatus = () => {
      const { day, time } = getLocalNow();
      const today = SCHEDULE[day];

      if (today && time >= today[0] && time < today[1]) {
        statusEl.textContent = "Abierto ahora · cierra " + fmtHour(today[1]);
        statusEl.classList.add("is-open");
        statusEl.classList.remove("is-closed");
      } else {
        let nextDay = day;
        for (let i = 1; i <= 7; i++) {
          const d = (day + i) % 7;
          if (SCHEDULE[d]) { nextDay = d; break; }
        }
        const label =
          nextDay === day
            ? "hoy"
            : nextDay === (day + 1) % 7
            ? "mañana"
            : DAY_NAMES[nextDay];
        statusEl.textContent = "Cerrado · abre " + label + " " + fmtHour(SCHEDULE[nextDay][0]);
        statusEl.classList.add("is-closed");
        statusEl.classList.remove("is-open");
      }
    };

    updateStatus();
    setInterval(updateStatus, 60 * 1000);
  }

  /* ---------- Cierre suave del menú al hacer clic en anclas ---------- */
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (e) => {
      const id = link.getAttribute("href");
      if (!id || id === "#") return;
      const target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      const offset = (header ? header.offsetHeight : 0) + 8;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: reduceMotion ? "auto" : "smooth" });
      history.replaceState(null, "", id);
    });
  });
})();
