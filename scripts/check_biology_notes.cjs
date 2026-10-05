const {chromium}=require('C:/Users/archa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
(async()=>{const browser=await chromium.launch({channel:'msedge',headless:true});try{
 const page=await browser.newPage({viewport:{width:1440,height:1000}});
 const topic=process.argv[2]||'02 - Organisation';const root=path.join('Biology - AQA',topic);
 await page.goto(pathToFileURL(path.resolve(root,'index.html')).href);
 await page.getByRole('link',{name:'Revision notes',exact:true}).click();
 const groups=await page.locator('.revision-group').evaluateAll(a=>a.map(x=>x.href));
 if(groups.length<2)throw Error('Missing notes groups');
 for(const url of groups){await page.goto(url);await page.locator('.reading').waitFor();
  await page.locator('.reading img').evaluateAll(imgs=>Promise.all(imgs.map(i=>i.decode())));
  await page.setViewportSize({width:390,height:844});
  if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2))throw Error('Mobile overflow: '+url);
  await page.setViewportSize({width:1440,height:1000});
 }
 const diagrams=path.join(root,'Diagrams');if(fs.existsSync(diagrams))for(const f of fs.readdirSync(diagrams).filter(x=>x.endsWith('.svg'))){
  await page.setContent('<style>body{margin:0}</style>'+fs.readFileSync(path.join(diagrams,f),'utf8'));
  const errors=await page.evaluate(()=>{const ts=[...document.querySelectorAll('text')].map(e=>({t:e.textContent,b:e.getBoundingClientRect()}));const bad=[];for(let i=0;i<ts.length;i++)for(let j=i+1;j<ts.length;j++){const a=ts[i],b=ts[j];if(Math.min(a.b.right,b.b.right)-Math.max(a.b.left,b.b.left)>1&&Math.min(a.b.bottom,b.b.bottom)-Math.max(a.b.top,b.b.top)>1)bad.push([a.t,b.t]);}return bad});
  if(errors.length)throw Error(f+': '+JSON.stringify(errors));
  await page.locator('body>svg').screenshot({path:'tmp/'+topic.slice(0,2)+'-'+f+'.png'});
 }
 console.log('PASS '+topic+': '+groups.length+' notes groups, images load, no mobile overflow or diagram text collisions');
}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
