// All interaction stays in the browser. No analytics, storage, or remote requests.
const menuButton = document.querySelector('[data-menu-toggle]');
const mobileMenu = document.querySelector('#mobile-navigation');
if (menuButton && mobileMenu) {
  const closeMenu = () => {
    mobileMenu.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
  };
  menuButton.addEventListener('click', () => {
    const opening = menuButton.getAttribute('aria-expanded') !== 'true';
    mobileMenu.hidden = !opening;
    menuButton.setAttribute('aria-expanded', String(opening));
  });
  mobileMenu.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !mobileMenu.hidden) {
      closeMenu();
      menuButton.focus();
    }
  });
  window.matchMedia('(min-width: 851px)').addEventListener('change', event => {
    if (event.matches) closeMenu();
  });
}

document.querySelectorAll('[data-tabs]').forEach(tabList => {
  const tabs = Array.from(tabList.querySelectorAll('[role="tab"]'));
  const select = tab => {
    tabs.forEach(item => {
      const active = item === tab;
      item.setAttribute('aria-selected', String(active));
      item.tabIndex = active ? 0 : -1;
      const panel = document.getElementById(item.getAttribute('aria-controls'));
      if (panel) panel.hidden = !active;
    });
  };
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => select(tab));
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next === undefined) return;
      event.preventDefault();
      select(tabs[next]);
      tabs[next].focus();
    });
  });
});

// Keep a section selected when switching between the two translated pages.
document.querySelectorAll('[data-language-link]').forEach(link => {
  link.addEventListener('click', () => {
    const target = new URL(link.href);
    target.hash = window.location.hash;
    link.href = target.href;
  });
});
