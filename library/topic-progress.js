document.querySelectorAll('[data-topic-progress]').forEach((checkbox) => {
  const storageKey = `study-buddy:topic-completed:${checkbox.dataset.topicProgress}`;
  const card = checkbox.closest('.topic-card');

  const showState = (completed) => {
    checkbox.checked = completed;
    card?.classList.toggle('topic-completed', completed);
  };

  try {
    showState(localStorage.getItem(storageKey) === 'true');
  } catch {
    showState(false);
  }

  checkbox.addEventListener('change', () => {
    showState(checkbox.checked);
    try {
      localStorage.setItem(storageKey, String(checkbox.checked));
    } catch {
      // The checkbox still works for this visit if storage is unavailable.
    }
  });
});
