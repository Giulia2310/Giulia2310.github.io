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
