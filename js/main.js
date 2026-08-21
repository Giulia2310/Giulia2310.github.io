/* Giulia La Paglia — Portfolio
   Small vanilla-JS helpers: slide-in menu + scroll reveal.
   No dependencies. */

(function () {
  "use strict";

  /* Flip on the reveal/fade-in styles only once we know JS is actually
     running — see the "html.js .reveal" rules in style.css. */
  document.documentElement.classList.add("js");

  /* ---------- Slide-in menu ---------- */
  var toggle = document.querySelector("[data-menu-toggle]");
  var backdrop = document.querySelector("[data-menu-backdrop]");
  var panel = document.querySelector("[data-menu-panel]");

  function openMenu() {
    document.body.classList.add("menu-open");
    if (toggle) toggle.setAttribute("aria-expanded", "true");
  }
  function closeMenu() {
    document.body.classList.remove("menu-open");
    if (toggle) toggle.setAttribute("aria-expanded", "false");
  }
  function toggleMenu() {
    document.body.classList.contains("menu-open") ? closeMenu() : openMenu();
  }

  if (toggle) toggle.addEventListener("click", toggleMenu);
  if (backdrop) backdrop.addEventListener("click", closeMenu);

  if (panel) {
    panel.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", closeMenu);
    });
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeMenu();
  });

  /* ---------- Services accordion (click a row to see its skills) ---------- */
  document.querySelectorAll(".service-row__head").forEach(function (head) {
    head.addEventListener("click", function () {
      var row = head.closest(".service-row");
      var open = row.classList.toggle("is-open");
      head.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  /* ---------- Ticker: position follows page scroll instead of
     auto-animating on a timer. Mouse-wheel scrolling and touch swipes
     on mobile/tablet both fire the same native "scroll" event, so one
     listener covers every input device. ---------- */
  var tickers = [];
  document.querySelectorAll(".ticker__track").forEach(function (track) {
    var group = track.querySelector(".ticker__group");
    if (group) tickers.push({ track: track, group: group, unitWidth: group.offsetWidth || 0 });
  });

  /* Falls back to a generous fixed width if the real viewport can't be
     read yet (e.g. this script runs before layout has settled), so the
     ticker never ends up under-filled with a visible gap. */
  function viewportWidth() {
    var w = Math.max(window.innerWidth || 0, document.documentElement.clientWidth || 0);
    return w > 0 ? w : 1600;
  }

  function fillTickers() {
    var vw = viewportWidth();
    tickers.forEach(function (t) {
      // Re-measure from the original template group each time: web fonts
      // that finish loading after first paint can change its width.
      t.unitWidth = t.group.offsetWidth || t.unitWidth;
      if (!t.unitWidth) return;
      var safety = 0;
      while (t.track.offsetWidth < vw + t.unitWidth && safety < 200) {
        t.track.appendChild(t.group.cloneNode(true));
        safety++;
      }
    });
  }

  if (tickers.length) {
    fillTickers();
    window.addEventListener("load", fillTickers);
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(fillTickers).catch(function () {});
    }

    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      var tickerTicking = false;
      var updateTickers = function () {
        var y = window.scrollY || window.pageYOffset;
        tickers.forEach(function (t) {
          var offset = ((y * 0.4) % t.unitWidth + t.unitWidth) % t.unitWidth;
          t.track.style.transform = "translateX(-" + offset + "px)";
        });
        tickerTicking = false;
      };
      window.addEventListener("scroll", function () {
        if (!tickerTicking) {
          requestAnimationFrame(updateTickers);
          tickerTicking = true;
        }
      }, { passive: true });
      updateTickers();
    }

    var tickerResizeTimer;
    window.addEventListener("resize", function () {
      clearTimeout(tickerResizeTimer);
      tickerResizeTimer = setTimeout(fillTickers, 200);
    });
  }

  /* ---------- Scroll reveal ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in-view");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -60px 0px" }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in-view"); });
  }
})();
