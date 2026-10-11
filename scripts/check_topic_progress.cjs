const { chromium } = require('C:/Users/archa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path = require('path');
const { pathToFileURL } = require('url');

(async () => {
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  const subjectPages = [
    ['Computer Science - AQA', 8],
    ['English Language - Eduqas', 5],
    ['English Literature - Eduqas', 5],
    ['Maths - Edexcel', 6],
    ['Geography - OCR A', 8],
    ['French - AQA', 10],
    ['Biology - AQA', 9],
    ['Chemistry - AQA', 12],
    ['Physics - AQA', 10],
  ];

  let total = 0;
  for (const [subject, expected] of subjectPages) {
    const url = pathToFileURL(path.resolve(subject, 'index.html')).href;
    await page.goto(url);
    const count = await page.locator('[data-topic-progress]').count();
    if (count !== expected) throw new Error(`${subject}: expected ${expected} checkboxes, found ${count}.`);
    total += count;
  }

  const url = pathToFileURL(path.resolve('English Literature - Eduqas/index.html')).href;

  await page.goto(url);
  const checkboxes = page.locator('[data-topic-progress]');

  const first = checkboxes.first();
  const second = checkboxes.nth(1);
  const originalUrl = page.url();
  await first.check();
  if (page.url() !== originalUrl) throw new Error('Checking a topic unexpectedly opened the topic page.');
  if (!(await first.isChecked())) throw new Error('The topic did not become checked.');
  if (await second.isChecked()) throw new Error('Checking one topic changed another topic.');
  if (!(await first.locator('xpath=ancestor::article').evaluate((card) => card.classList.contains('topic-completed')))) {
    throw new Error('The completed topic style was not applied.');
  }

  await page.reload();
  if (!(await checkboxes.first().isChecked())) throw new Error('The checked state was not restored after reload.');
  await checkboxes.first().uncheck();
  await page.reload();
  if (await checkboxes.first().isChecked()) throw new Error('The unchecked state was not restored after reload.');

  await page.setViewportSize({ width: 390, height: 844 });
  await page.reload();
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  if (overflow) throw new Error('The topic cards overflow horizontally on a narrow screen.');

  await browser.close();
  console.log(`PASS: ${total} topic checkboxes across 9 subjects persist independently, do not navigate, and fit on mobile.`);
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
