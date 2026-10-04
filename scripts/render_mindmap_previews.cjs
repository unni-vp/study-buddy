const {chromium}=require('C:/Users/archa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');
(async()=>{const browser=await chromium.launch({channel:'msedge',headless:true});
const page=await browser.newPage({viewport:{width:2400,height:1840},deviceScaleFactor:1});
for(const file of process.argv.slice(2)){await page.setContent('<!doctype html><style>html,body{margin:0}svg{display:block}</style>'+fs.readFileSync(file,'utf8'));await page.evaluate(()=>document.fonts.ready);await page.evaluate(()=>scrollTo(0,0));await page.locator('body > svg').screenshot({path:file.replace(/\.svg$/,'.png')});console.log(file.split(/[\\/]/).at(-1));}
await browser.close();})().catch(e=>{console.error(e);process.exit(1)});
