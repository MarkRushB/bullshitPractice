(() => {
  const tiles = [...document.querySelectorAll('[data-photo]')];
  const dialog = document.querySelector('.lightbox');
  const image = document.querySelector('#large-photo');
  let current = 0;
  const visible = () => tiles.filter(tile => !tile.hidden);
  const show = index => {
    const list = visible();
    if (!list.length) return;
    current = (index + list.length) % list.length;
    const tile = list[current];
    image.src = tile.dataset.photo;
    image.alt = tile.dataset.caption;
    document.querySelector('#photo-caption').textContent = tile.dataset.caption;
    document.querySelector('#photo-counter').textContent = `${current + 1} / ${list.length}`;
    document.querySelector('#original-photo').href = tile.dataset.original;
  };
  tiles.forEach(tile => tile.addEventListener('click', event => {
    event.preventDefault(); show(visible().indexOf(tile)); dialog.showModal();
  }));
  document.querySelector('#close-photo').addEventListener('click', () => dialog.close());
  document.querySelector('.photo-prev').addEventListener('click', () => show(current - 1));
  document.querySelector('.photo-next').addEventListener('click', () => show(current + 1));
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft') { event.preventDefault(); show(current - 1); }
    if (event.key === 'ArrowRight') { event.preventDefault(); show(current + 1); }
  });
})();
