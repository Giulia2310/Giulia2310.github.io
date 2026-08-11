document.addEventListener('DOMContentLoaded', () => {

  /* ---------- Menu overlay ---------- */
  const toggle = document.querySelector('.menu-toggle');
  const overlay = document.querySelector('.nav-overlay');

  if (toggle && overlay) {
    toggle.addEventListener('click', () => {
      const isOpen = overlay.classList.toggle('is-open');
      toggle.classList.toggle('is-active', isOpen);
      toggle.setAttribute('aria-expanded', String(isOpen));
      document.body.classList.toggle('menu-open', isOpen);
    });

    overlay.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        overlay.classList.remove('is-open');
        toggle.classList.remove('is-active');
        document.body.classList.remove('menu-open');
      });
    });
  }

  /* ---------- Marquee: duplica il contenuto per lo scroll infinito ---------- */
  document.querySelectorAll('.marquee-track').forEach(track => {
    track.innerHTML += track.innerHTML;
  });

  /* ---------- Hero: rotazione dei ruoli ---------- */
  const roles = document.querySelectorAll('.hero-roles h1');
  if (roles.length > 1) {
    let current = 0;
    roles.forEach((el, i) => el.classList.toggle('is-current', i === 0));

    setInterval(() => {
      const prev = current;
      current = (current + 1) % roles.length;
      roles[prev].classList.remove('is-current');
      roles[prev].classList.add('is-prev');
      roles[current].classList.add('is-current');
      setTimeout(() => roles[prev].classList.remove('is-prev'), 650);
    }, 2200);
  }

});
