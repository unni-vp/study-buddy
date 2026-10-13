const { chromium } = require('C:/Users/archa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const { pathToFileURL } = require('url');
const fs = require('fs');
const path = require('path');

function slugify(value) {
  return value.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

const decks = fs.readdirSync('.', { withFileTypes: true })
  .filter((entry) => entry.isDirectory() && / - (AQA|Edexcel|Eduqas|OCR A)$/.test(entry.name))
  .flatMap((subject) => fs.readdirSync(subject.name, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && /^\d+ - /.test(entry.name))
    .flatMap((topic) => {
      const topicPath = path.join(subject.name, topic.name);
      const deckFolder = path.join(topicPath, 'Flash Cards');
      if (!fs.existsSync(deckFolder)) return [];
      return fs.readdirSync(deckFolder)
        .filter((name) => name.endsWith('Flash Cards.json'))
        .map((name) => ({
          topic: topicPath,
          json: path.join(deckFolder, name),
          slug: `${slugify(subject.name)}-${slugify(topic.name.replace(/^\d+ - /, ''))}`,
        }));
    }));

(async () => {
  fs.mkdirSync('tmp', { recursive: true });
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const pageErrors = [];
  page.on('pageerror', (error) => pageErrors.push(error.message));
  let totalCards = 0;

  for (const deck of decks) {
    const source = JSON.parse(fs.readFileSync(deck.json, 'utf8'));
    const expectedCount = source.cards.length;
    totalCards += expectedCount;
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.goto(pathToFileURL(path.resolve(deck.topic, 'index.html')).href);
    const flashCardLink = page.getByRole('link', { name: 'Flash cards', exact: true });
    if (await flashCardLink.count() !== 1) throw new Error(`${deck.topic} should have one Flash cards resource button.`);
    const coveragePath = path.join(deck.topic, 'resource-coverage.json');
    const coverage = fs.existsSync(coveragePath) ? JSON.parse(fs.readFileSync(coveragePath, 'utf8')) : {};
    const expectedButtons = Array.isArray(coverage.mindmaps) && coverage.mindmaps.length === 0 ? 3 : 4;
    if (await page.locator('.resource-actions > *').count() !== expectedButtons) {
      throw new Error(`${deck.topic} should have ${expectedButtons} resource buttons.`);
    }
    await flashCardLink.click();

    if (!(await page.locator('[data-flashcard-deck]').evaluate((app) => app.classList.contains('flashcards-ready')))) {
      throw new Error(`${deck.topic}: flash-card script did not initialise: ${pageErrors.join('; ') || 'no browser error reported'}`);
    }
    const cards = page.locator('.flashcard-item');
    if (await cards.count() !== expectedCount) throw new Error(`${deck.topic}: expected ${expectedCount} cards, found ${await cards.count()}.`);
    if (await page.locator('.flashcard-item:visible').count() !== 1) throw new Error(`${deck.topic}: exactly one card should be visible.`);

    const first = page.locator('.flashcard-item:visible');
    if (await first.locator('.flashcard-back').isVisible()) throw new Error(`${deck.topic}: first answer should be hidden initially.`);
    await first.click();
    if (!(await first.locator('.flashcard-back').isVisible())) throw new Error(`${deck.topic}: selecting the card did not reveal its answer.`);
    await page.screenshot({ path: `tmp/${deck.slug}-flashcards-desktop.png`, fullPage: true });

    if (await page.getByRole('button', { name: 'Reveal answer', exact: true }).count()) throw new Error(`${deck.topic}: redundant reveal button found.`);
    if (await page.locator('[data-flashcard-category]').count()) throw new Error(`${deck.topic}: study-group selector found.`);
    if (await page.getByText('RETRIEVAL PRACTICE', { exact: true }).count()) throw new Error(`${deck.topic}: redundant retrieval-practice heading found.`);

    await page.getByRole('button', { name: 'Next →' }).click();
    if ((await page.locator('[data-flashcard-current]').textContent()) !== '2') throw new Error(`${deck.topic}: Next did not advance the deck.`);
    if (await page.locator('.flashcard-item:visible .flashcard-back').isVisible()) throw new Error(`${deck.topic}: a new card should start on its question.`);
    await page.locator('.flashcard-item:visible').press('Space');
    if (!(await page.locator('.flashcard-item:visible .flashcard-back').isVisible())) throw new Error(`${deck.topic}: Space did not reveal the answer.`);

    await page.setViewportSize({ width: 390, height: 844 });
    await page.reload();
    if (await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth)) {
      throw new Error(`${deck.topic}: page overflows horizontally on mobile.`);
    }
    await page.screenshot({ path: `tmp/${deck.slug}-flashcards-mobile.png`, fullPage: true });

    await page.emulateMedia({ media: 'print' });
    const printShowsAll = await page.locator('.flashcard-item').nth(1).evaluate((card) => getComputedStyle(card).display !== 'none');
    const printShowsAnswer = await page.locator('.flashcard-back').first().evaluate((answer) => getComputedStyle(answer).display !== 'none');
    if (!printShowsAll || !printShowsAnswer) throw new Error(`${deck.topic}: print should show every question and answer.`);
    await page.emulateMedia({ media: 'screen' });
  }

  // Choose an actual topic without a deck: completed science topics now all have cards.
  const config=JSON.parse(fs.readFileSync('project-config.json','utf8'));
  const topicWithoutDeck=Object.entries(config.subjects).flatMap(([subject,course])=>course.topics.map((item,index)=>path.join(subject,String(index+1).padStart(2,'0')+' - '+item.title))).find((topic)=>{
    const folder=path.join(topic,'Flash Cards');
    return !fs.existsSync(folder)||!fs.readdirSync(folder).some((name)=>name.endsWith('Flash Cards.json'));
  });
  if (topicWithoutDeck) {
  await page.goto(pathToFileURL(path.resolve(topicWithoutDeck,'index.html')).href);
  if (await page.getByRole('link', { name: 'Flash cards', exact: true }).count()) {
    throw new Error('A topic without a flash-card deck should not show an empty Flash cards button.');
  }
  }

  await browser.close();
  console.log(`PASS: ${totalCards} flash cards across ${decks.length} topics reveal, navigate, print, and fit desktop/mobile layouts.`);
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
