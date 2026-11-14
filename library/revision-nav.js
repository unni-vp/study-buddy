/* Native disclosure on narrow screens; keep the current entry visible in long lists. */
(() => {
 const sidebar=document.querySelector('.revision-sidebar');
 if(!sidebar)return;
 const toc=sidebar.querySelector('.revision-toc');
 const list=sidebar.querySelector('.revision-sections-list');
 const narrow=window.matchMedia('(max-width:720px)');
 function revealCurrent() {
  if(!toc.open)return;
  const active=list.querySelector('[aria-current="page"]');
  if(!active)return;
  const scroller=narrow.matches?list:sidebar;
  const row=active.getBoundingClientRect(),box=scroller.getBoundingClientRect();
  const group=active.closest(".revision-nav-group");
  if(group){
   const parent=group.getBoundingClientRect();
   if(parent.height<=box.height-24){
    if(parent.top<box.top||parent.bottom>box.bottom)scroller.scrollTop+=parent.top-box.top-12;
    return;
   }
  }
  if(row.top<box.top||row.bottom>box.bottom)scroller.scrollTop+=row.top-box.top-(box.height-row.height)/2;
 }
 function resize() {
  toc.open=!narrow.matches;
  revealCurrent();
 }
 narrow.addEventListener('change',resize);
 toc.addEventListener('toggle',revealCurrent);
 resize();
})();
