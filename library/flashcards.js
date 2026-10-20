document.querySelectorAll('[data-flashcard-deck]').forEach((app) => {
  const cards = Array.from(app.querySelectorAll('.flashcard-item'));
  const currentOutput = app.querySelector('[data-flashcard-current]');
  const totalOutput = app.querySelector('[data-flashcard-total]');
  let order = cards.map((_, index) => index);
  let position = 0;

  const currentCard = () => cards[order[position]];

  const conceal = (card) => {
    card.classList.remove('is-revealed');
    card.setAttribute('aria-expanded', 'false');
    card.querySelector('.flashcard-back').hidden = true;
    card.querySelector('.flashcard-front').hidden = false;
  };

  const show = () => {
    cards.forEach((card) => {
      card.hidden = true;
      conceal(card);
    });
    const card = currentCard();
    card.hidden = false;
    currentOutput.textContent = String(position + 1);
    totalOutput.textContent = String(order.length);
  };

  const reveal = () => {
    const card = currentCard();
    const revealed = !card.classList.contains('is-revealed');
    card.classList.toggle('is-revealed', revealed);
    card.setAttribute('aria-expanded', String(revealed));
    card.querySelector('.flashcard-front').hidden = revealed;
    card.querySelector('.flashcard-back').hidden = !revealed;
  };

  const move = (amount) => {
    position = (position + amount + order.length) % order.length;
    show();
    currentCard().focus();
  };

  const reset = () => {
    order = cards.map((_, index) => index);
    position = 0;
    show();
  };

  app.querySelector('[data-flashcard-action="previous"]').addEventListener('click', () => move(-1));
  app.querySelector('[data-flashcard-action="next"]').addEventListener('click', () => move(1));
  app.querySelector('[data-flashcard-action="shuffle"]').addEventListener('click', () => {
    for (let index = order.length - 1; index > 0; index -= 1) {
      const random = Math.floor(Math.random() * (index + 1));
      [order[index], order[random]] = [order[random], order[index]];
    }
    position = 0;
    show();
  });
  app.querySelector('[data-flashcard-action="reset"]').addEventListener('click', reset);
  cards.forEach((card) => {
    card.addEventListener('click', reveal);
    card.addEventListener('keydown', (event) => {
      if (event.key === ' ' || event.key === 'Enter') {
        event.preventDefault();
        reveal();
      }
    });
  });
  app.addEventListener('keydown', (event) => {
    if (event.target.matches('select, button')) return;
    if (event.key === 'ArrowLeft') move(-1);
    if (event.key === 'ArrowRight') move(1);
  });

  app.classList.add('flashcards-ready');
  show();
  currentCard().focus();
});
