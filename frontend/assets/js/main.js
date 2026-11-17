(()=>{"use strict";
const CONFIG={analyticsDomain:"listspl.co.in",plausibleSrc:"https://plausible.io/js/script.js",api:"/api"};
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const store={get:k=>{try{return localStorage.getItem(k)}catch{return null}},set:(k,v)=>{try{localStorage.setItem(k,v)}catch{}}};
const root=document.documentElement;root.dataset.theme=store.get("theme")||"light";
$("#theme")?.addEventListener("click",()=>{root.dataset.theme=root.dataset.theme==="dark"?"light":"dark";store.set("theme",root.dataset.theme)});
$("#burger")?.addEventListener("click",e=>{const o=$("#menu").classList.toggle("open");e.currentTarget.setAttribute("aria-expanded",o)});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;e.target.classList.add("in");io.unobserve(e.target);if(e.target.dataset.count)(window.rollNum||count)(e.target)}),{threshold:.25});
$$(".reveal,[data-count],.steps li").forEach(el=>io.observe(el));
function count(el){const t=+el.dataset.count,s=el.dataset.suffix||"";if(matchMedia("(prefers-reduced-motion: reduce)").matches){el.textContent=t+s;return}
const t0=performance.now();(function f(n){const p=Math.min((n-t0)/1600,1);el.textContent=Math.round(t*(1-Math.pow(1-p,3)))+(p===1?s:"");if(p<1)requestAnimationFrame(f)})(t0)}
const LINKS={VPN:"Encrypted VPN tunnels give each branch a private path to the data center.",RF:"Radio-frequency links can reach branches where wired options are limited.",MPLS:"MPLS offers carrier-managed, predictable connectivity between branches and the data center.","Leased line":"Dedicated leased lines provide a private, always-on link for high-volume branches."};
$$("[data-link]").forEach(b=>b.addEventListener("click",()=>{$$("[data-link]").forEach(x=>x.setAttribute("aria-pressed","false"));b.setAttribute("aria-pressed","true");const k=b.dataset.link;$$(".linklabel").forEach(t=>t.textContent=k);const d=$("#linkdesc");if(d)d.textContent=LINKS[k]}));
const rs=$("#rsearch"),cat=$("#rcats");let cur="all";
function filt(){const q=(rs?.value||"").toLowerCase();let n=0;$$("[data-res]").forEach(c=>{const ok=(cur==="all"||c.dataset.cat===cur)&&c.textContent.toLowerCase().includes(q);c.hidden=!ok;n+=ok});const e=$("#rempty");if(e)e.hidden=n>0}
rs?.addEventListener("input",filt);cat?.addEventListener("click",e=>{const b=e.target.closest("button");if(!b)return;cur=b.dataset.cat;$$("button",cat).forEach(x=>x.setAttribute("aria-pressed",x===b));filt()});
$$("[data-open]").forEach(b=>b.addEventListener("click",e=>{e.preventDefault();$("#"+b.dataset.open)?.showModal()}));$$("[data-close]").forEach(b=>b.addEventListener("click",()=>b.closest("dialog").close()));
const rules={name:v=>v.trim().length>1||"Please enter your name.",bank:v=>v.trim().length>1||"Please enter your bank or society name.",email:v=>/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)||"Enter a valid email.",phone:v=>/^[+\d][\d\s-]{7,15}$/.test(v.trim())||"Enter a valid phone number.",branches:v=>v===""||(+v>=1&&+v<=2000)||"Enter a number between 1 and 2000.",requirement:v=>v.trim().length>5||"Tell us briefly what you need."};
$$("form[data-api]").forEach(f=>{f.dataset.t=Date.now();f.addEventListener("submit",async e=>{e.preventDefault();let ok=true;
$$("[data-v]",f).forEach(i=>{const r=rules[i.dataset.v](i.value),er=i.parentElement.querySelector(".err");if(er)er.textContent=r===true?"":r;if(r!==true)ok=false});
const m=$(".msg",f);if(!ok){m.className="msg bad";m.textContent="Please fix the highlighted fields.";return}
const d=Object.fromEntries(new FormData(f));d.elapsed=Date.now()-f.dataset.t;const btn=$("button[type=submit]",f);btn.disabled=true;
try{const r=await fetch(CONFIG.api+f.dataset.api,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d)});const j=await r.json();if(!r.ok)throw new Error(j.error||"Failed");m.className="msg ok";m.textContent="Thank you! Our banking-software team will contact you shortly.";f.reset()}
catch(x){m.className="msg bad";m.textContent=(x.message||"Something went wrong")+" You can also call +91 95299 23868."}finally{btn.disabled=false}})});
const cb=$("#consent");function loadA(){if($("#an"))return;const s=document.createElement("script");s.id="an";s.defer=true;s.dataset.domain=CONFIG.analyticsDomain;s.src=CONFIG.plausibleSrc;document.head.append(s)}
const c=store.get("consent");if(c==="yes")loadA();else if(!c)cb?.classList.add("show");
$("#cyes")?.addEventListener("click",()=>{store.set("consent","yes");cb.classList.remove("show");loadA()});$("#cno")?.addEventListener("click",()=>{store.set("consent","no");cb.classList.remove("show")});
const inv=$("#invite");let shown=false;try{shown=!!sessionStorage.getItem("inv")}catch{}
function showInv(){if(shown||!inv||$("dialog[open]"))return;shown=true;try{sessionStorage.setItem("inv","1")}catch{}inv.showModal()}
addEventListener("scroll",()=>{if(scrollY/(document.body.scrollHeight-innerHeight)>.7)showInv()},{passive:true});document.addEventListener("mouseleave",e=>{if(e.clientY<=0&&matchMedia("(pointer:fine)").matches)showInv()});
})();

(()=>{"use strict";if(!matchMedia("(pointer:fine)").matches||matchMedia("(prefers-reduced-motion: reduce)").matches)return;
const r=document.documentElement;let tx=.5,ty=.3,x=tx,y=ty,run=false;
function f(){x+=(tx-x)*.08;y+=(ty-y)*.08;const s=r.style;s.setProperty("--mx",(x*100).toFixed(2)+"%");s.setProperty("--my",(y*100).toFixed(2)+"%");s.setProperty("--px",(x-.5).toFixed(3));s.setProperty("--py",(y-.5).toFixed(3));
if(Math.abs(tx-x)<.0005&&Math.abs(ty-y)<.0005){run=false;return}requestAnimationFrame(f)}
addEventListener("pointermove",e=>{tx=e.clientX/innerWidth;ty=e.clientY/innerHeight;r.classList.add("cursor-bg");if(!run){run=true;requestAnimationFrame(f)}},{passive:true});
document.addEventListener("pointerleave",()=>r.classList.remove("cursor-bg"));
})();

(()=>{"use strict";const $=s=>document.querySelector(s),rm=matchMedia("(prefers-reduced-motion: reduce)").matches;
const bar=document.createElement("div");bar.className="sp";const up=document.createElement("button");up.className="totop iconbtn";up.textContent="↑";up.setAttribute("aria-label","Back to top");document.body.append(bar,up);
function sc(){const m=document.documentElement.scrollHeight-innerHeight;bar.style.transform="scaleX("+(m>0?scrollY/m:0)+")";up.classList.toggle("show",scrollY>600)}addEventListener("scroll",sc,{passive:true});sc();up.onclick=()=>scrollTo({top:0,behavior:rm?"auto":"smooth"});
const r=$("#rot");if(r&&!rm){const w=r.dataset.words.split("|");let i=0;setInterval(()=>{r.classList.add("out");setTimeout(()=>{i=(i+1)%w.length;r.textContent=w[i];r.classList.remove("out")},350)},2600)}
document.addEventListener("pointermove",e=>{const c=e.target.closest&&e.target.closest(".card");if(!c)return;const b=c.getBoundingClientRect();c.style.setProperty("--cx",e.clientX-b.left+"px");c.style.setProperty("--cy",e.clientY-b.top+"px")},{passive:true});
const z=$("#zoom");if(z){document.querySelectorAll("[data-zoom]").forEach(b=>b.addEventListener("click",()=>{z.querySelector("img").src=b.dataset.zoom;z.showModal()}));z.addEventListener("click",e=>{if(e.target===z)z.close()})}
})();

(()=>{if(document.querySelector(".bgl"))return;const d=document.createElement("div");d.className="bgl";d.setAttribute("aria-hidden","true");d.innerHTML="<i></i><i></i><i></i>";document.body.prepend(d)})();

window.rollNum=function(el){const t=el.dataset.count,s=el.dataset.suffix||"";el.setAttribute("aria-label",t+s);
if(matchMedia("(prefers-reduced-motion: reduce)").matches){el.textContent=t+s;return}
el.textContent="";el.classList.add("odo");
[...t].forEach((c,i)=>{const d=document.createElement("span");d.className="d";d.setAttribute("aria-hidden","true");const st=document.createElement("span");st.className="st";st.innerHTML=[..."01234567890123456789"].map(n=>"<b>"+n+"</b>").join("");d.append(st);el.append(d);st.style.transitionDelay=i*140+"ms";requestAnimationFrame(()=>requestAnimationFrame(()=>{st.style.transform="translateY(-"+(10+ +c)*5+"%)"}))});
if(s){const x=document.createElement("span");x.textContent=s;x.setAttribute("aria-hidden","true");el.append(x)}};
document.querySelectorAll(".marq img").forEach(i=>{const f=()=>{if(i.dataset.remote&&!i.dataset.tried){i.dataset.tried=1;i.src=i.dataset.remote}else i.replaceWith(Object.assign(document.createElement("b"),{textContent:i.alt}))};i.addEventListener("error",f);if(i.complete&&i.naturalWidth===0)f()});
document.getElementById("menu")?.addEventListener("click",e=>{if(e.target.closest("a")){e.currentTarget.classList.remove("open");document.getElementById("burger")?.setAttribute("aria-expanded","false")}});

(()=>{const L=document.querySelectorAll(".alogo");if(!L.length)return;if(matchMedia("(prefers-reduced-motion: reduce)").matches)L.forEach(l=>l.querySelectorAll("animateTransform").forEach(a=>a.remove()));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("go");io.unobserve(e.target)}}),{threshold:.35});L.forEach(l=>io.observe(l))})();

;(()=>{const t=document.querySelectorAll(".demo");t.forEach(d=>{const b=d.querySelectorAll("[data-d]"),p=d.querySelectorAll("[data-p]");b.forEach(x=>x.onclick=()=>{b.forEach(y=>y.setAttribute("aria-selected",y===x));p.forEach(y=>y.hidden=y.dataset.p!==x.dataset.d)})});
const th=document.getElementById("theme");if(!th)return;const L=document.createElement("button");L.className="langbtn";L.type="button";L.textContent="मराठी";th.after(L);
const els=document.querySelectorAll("[data-mr]");els.forEach(e=>e.dataset.en=e.textContent);let mr=false;try{mr=localStorage.lang==="mr"}catch{}
function ap(){els.forEach(e=>e.textContent=mr?e.dataset.mr:e.dataset.en);L.textContent=mr?"English":"मराठी";document.documentElement.lang=mr?"mr":"en"}
L.onclick=()=>{mr=!mr;try{localStorage.lang=mr?"mr":"en"}catch{}ap()};ap()})();
