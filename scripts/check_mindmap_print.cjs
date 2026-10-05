const {chromium}=require('C:/Users/archa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'), path=require('path'), {pathToFileURL}=require('url');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1000}});
  const maps=fs.readdirSync('Biology - AQA/01 - Cell biology/Mind Maps').filter(f=>f.endsWith('.svg'));
  fs.mkdirSync('tmp/pdfs',{recursive:true});
  for(const name of maps){
   const slug=name.slice(0,-4);
   await page.goto(pathToFileURL(path.resolve('library/resources/biology-aqa-cell-biology-'+slug+'.html')).href);
   await page.locator('.mindmap-view img').evaluate(i=>i.decode());
   await page.emulateMedia({media:'print'});
   const size=await page.locator('.mindmap-view img').boundingBox();
   if(Math.abs(size.width-277*96/25.4)>1)throw Error('Incorrect printed width: '+slug);
   await page.pdf({path:'tmp/pdfs/'+slug+'-reader.pdf',preferCSSPageSize:true,printBackground:true});
   await page.emulateMedia({media:'screen'});
   await page.locator('main .mindmap-open').click();
   await page.locator('#mindmap-full-image').evaluate(i=>i.decode());
   await page.emulateMedia({media:'print'});
   await page.pdf({path:'tmp/pdfs/'+slug+'-modal.pdf',preferCSSPageSize:true,printBackground:true});
   await page.emulateMedia({media:'screen'});
   console.log('Printed reader and modal: '+slug);
  }
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
