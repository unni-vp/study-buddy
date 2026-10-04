// Printing shows every answer, then restores the student's open/closed choices.
(() => {
  const answers = [...document.querySelectorAll('details.qa-answer')];
  document.querySelectorAll('[data-qa-action]').forEach(button => {
    button.addEventListener('click', () => {
      const expand = button.dataset.qaAction === 'expand';
      answers.forEach(answer => { answer.open = expand; });
    });
  });
  let previousState = null;
  function showAnswersForPrint() {
    if (previousState !== null) return;
    previousState = answers.map(answer => answer.open);
    answers.forEach(answer => { answer.open = true; });
  }
  function restoreAnswers() {
    if (previousState === null) return;
    answers.forEach((answer, index) => { answer.open = previousState[index]; });
    previousState = null;
  }
  window.addEventListener('beforeprint', showAnswersForPrint);
  window.addEventListener('afterprint', restoreAnswers);
  window.matchMedia('print').addEventListener('change', event => {
    if (event.matches) showAnswersForPrint();
    else restoreAnswers();
  });
})();
