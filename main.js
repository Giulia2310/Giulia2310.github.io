// ===================================================
// Portfolio Giulia La Paglia — script principale
// ===================================================

document.addEventListener('DOMContentLoaded', () => {
  /* Menu overlay */
  const toggle = document.querySelector('.menu-toggle');
  const overlay = document.querySelector('.nav-overlay');

  if (toggle && overlay) {
    toggle.addEventListener('click', () => {
      const isOpen = overlay.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(isOpen));
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    overlay.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        overlay.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  /* Hero rotator: "I am a [Web Designer / Graphic Designer / ...]" */
  const rotatorWords = document.querySelectorAll('.hero-rotator span');
  if (rotatorWords.length) {
    let current = 0;
    rotatorWords[current].classList.add('is-active');
    setInterval(() => {
      rotatorWords[current].classList.remove('is-active');
      current = (current + 1) % rotatorWords.length;
      rotatorWords[current].classList.add('is-active');
    }, 2200);
  }
});
