(()=>{"use strict";
const KB=window.LIST_KB||[],byId=Object.fromEntries(KB.map(e=>[e.id,e]));
const preview=!!document.querySelector("[data-view]"),H=p=>preview?"#"+p.replace(/\//g,""):"/"+p+"/";
const el=(t,c,x)=>{const n=document.createElement(t);if(c)n.className=c;if(x!=null)n.textContent=x;return n};
const fab=el("button","chatfab");const lg=el("img");lg.src="/assets/img/chat-logo.svg";lg.alt="";lg.width=58;lg.height=23;fab.append(lg);fab.setAttribute("aria-label","Open chat assistant");fab.setAttribute("aria-expanded","false");
const box=el("div","chat");box.setAttribute("role","dialog");box.setAttribute("aria-label","LIST Software assistant");
const hd=el("header");hd.append(el("span",null,"LIST Assistant"));const x=el("button","iconbtn","✕");x.setAttribute("aria-label","Close chat");x.style.cssText="width:32px;height:32px;background:transparent;color:#fff;border:0";hd.append(x);
const msgs=el("div","msgs");msgs.setAttribute("aria-live","polite");
const note=el("div","note","Automated assistant. Answers come from LIST's company information. Please confirm details with our team.");
const form=el("form");const inp=el("input");inp.placeholder="Ask about CUSTODIAN, modules, security…";inp.setAttribute("aria-label","Your question");inp.maxLength=300;const go=el("button","btn sm","Send");go.type="submit";form.append(inp,go);
box.append(hd,msgs,note,form);document.body.append(fab,box);
const hist=[];let started=false;
const fin=w=>{w.classList.remove("typing");return w};
function say(t,who){const m=el("div","m "+who,t);msgs.append(m);msgs.scrollTop=msgs.scrollHeight;return m}
function chips(items){const c=el("div","chips");items.forEach(i=>{if(i.href){const a=el("a",null,i.l);a.href=i.href;c.append(a)}else{const b=el("button",null,i.l);b.type="button";b.addEventListener("click",i.fn);c.append(b)}});msgs.append(c);msgs.scrollTop=msgs.scrollHeight}
function actions(){return [{l:"Book a demo",href:H("contact")},{l:"Request a callback",fn:()=>{box.classList.remove("open");document.getElementById("cb")?.showModal()}}]}
function follow(ids){const it=(ids||[]).map(i=>byId[i]).filter(Boolean).map(e=>({l:e.t,fn:()=>ask(e.t)}));if(it.length)chips(it)}
const norm=s=>s.toLowerCase().replace(/[^a-z0-9+\- ]/g," ");
function local(q){const n=" "+norm(q)+" ";let best=null,bs=0;
for(const e of KB){let s=0;for(const k of e.k){if(n.includes(" "+k+" ")||n.includes(" "+k+"s ")||(k.length>5&&n.includes(k)))s+=(k.includes(" ")?4:3)+(k.length>7?1:0)}
for(const w of norm(e.t).split(" "))if(w.length>3&&w!=="about"&&n.includes(" "+w+" "))s+=1;if(s>bs){bs=s;best=e}}
return bs>=3?best:null}
async function remote(){const c=new AbortController(),t=setTimeout(()=>c.abort(),12000);
try{const r=await fetch("/api/chat",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({messages:hist.slice(-8)}),signal:c.signal});if(!r.ok)return null;const j=await r.json();return j.reply||null}catch{return null}finally{clearTimeout(t)}}
async function ask(q){q=q.trim();if(!q)return;say(q,"u");hist.push({role:"user",content:q});inp.value="";
const wait=say("","b typing");wait.append(el("i"),el("i"),el("i"));const ql=norm(q).trim();
if(/^(hi|hello|hey|namaste|good (morning|afternoon|evening))\b/.test(ql)&&ql.split(" ").length<4){fin(wait).textContent="Hello! I can answer questions about LIST Software, CUSTODIAN core banking and our modules. What would you like to know?";hist.push({role:"assistant",content:wait.textContent});follow(["custodian","modules","security","price"]);return}
let ans=await remote(),e=null;
if(ans){fin(wait).textContent=ans;hist.push({role:"assistant",content:ans});chips(actions());return}
await new Promise(r=>setTimeout(r,550));e=local(q);
if(e){fin(wait).textContent=e.a;hist.push({role:"assistant",content:e.a});follow(e.f);if(e.act)chips(actions())}
else{fin(wait).textContent="I don't have a confident answer to that. Our banking experts can help directly: call +91 95299 23868 or email bankingsales@listspl.co.in.";chips(actions());follow(["modules","custodian"])}}
function open(){box.classList.add("open");fab.setAttribute("aria-expanded","true");if(!started){started=true;say("Hi! I'm LIST's website assistant. Ask me about CUSTODIAN core banking, our add-on modules, security, or how to book a demo.","b");follow(["custodian","modules","security","price"])}inp.focus()}
fab.addEventListener("click",()=>{fab.classList.remove("spin");void fab.offsetWidth;fab.classList.add("spin")});fab.addEventListener("click",()=>box.classList.contains("open")?(box.classList.remove("open"),fab.setAttribute("aria-expanded","false")):open());
x.addEventListener("click",()=>{box.classList.remove("open");fab.setAttribute("aria-expanded","false");fab.focus()});
form.addEventListener("submit",e=>{e.preventDefault();ask(inp.value)});
document.addEventListener("keydown",e=>{if(e.key==="Escape"&&box.classList.contains("open"))x.click()});
})();
