(() => {
  'use strict';
  const controls = document.querySelector('[data-calendar-controls]');
  if (!controls) return;
  const months = [...document.querySelectorAll('[data-calendar-month]')];
  const choices = [...document.querySelectorAll('[data-select-month]')];
  const previous = document.querySelector('[data-previous-month]');
  const next = document.querySelector('[data-next-month]');
  const title = document.querySelector('[data-active-month]');
  let active = Math.max(0, months.findIndex(month => month.dataset.calendarMonth === '5'));

  function show(index) {
    if (index < 0 || index >= months.length) return;
    active = index;
    months.forEach((month, i) => { month.hidden = i !== active; });
    choices.forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.selectMonth === months[active].dataset.calendarMonth));
    });
    title.textContent = months[active].querySelector('h2').textContent;
    previous.disabled = active === 0;
    next.disabled = active === months.length - 1;
  }
  choices.forEach(button => button.addEventListener('click', () => {
    show(months.findIndex(month => month.dataset.calendarMonth === button.dataset.selectMonth));
  }));
  previous.addEventListener('click', () => show(active - 1));
  next.addEventListener('click', () => show(active + 1));
  const print = document.querySelector('[data-print-timetable]');
  if (print) {
    print.hidden = false;
    print.addEventListener('click', () => window.print());
  }
  document.querySelector('.exam-calendar').classList.add('calendar-enhanced');
  controls.hidden = false;
  show(active);
})();
