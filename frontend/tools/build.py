#!/usr/bin/env python3
"""Static page generator. Edit content here, run `python3 tools/build.py`, and the HTML pages are rewritten.
Run from the frontend/ folder. Also exports ../backend/data/resources.json."""
import json, os, html

SITE = "https://listspl.co.in"
import time
VER = str(int(time.time()))
PHONE, PHONE_TEL = "+91 95299 23868", "+919529923868"
EMAIL = "bankingsales@listspl.co.in"
ADDR = "Kolhapur: 6th Floor, Elixa Park, C.S.No. 517 A/1, E Ward, Old Pune-Bangalore Highway, Shahupuri, Kolhapur, Maharashtra 416001 · Sangli: Rahul Complex, Opp. Tata Petrol Pump, Guest House Gandhi Nagar, Vishrambag, Sangli, Maharashtra 416415"
HOURS = "Monday–Saturday, 9:00 AM–6:00 PM"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IC = {
 "bank": "M3 10l9-6 9 6M5 10v8M9 10v8M15 10v8M19 10v8M3 20h18",
 "db": "M4 6c0-1.7 3.6-3 8-3s8 1.3 8 3-3.6 3-8 3-8-1.3-8-3zM4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3",
 "chart": "M4 20V4M4 20h16M8 16v-5M12 16V8M16 16v-8",
 "shield": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z",
 "card": "M3 6h18v12H3zM3 10h18M7 15h3",
 "dr": "M20 12a8 8 0 1 1-3-6.2M20 4v5h-5",
 "sliders": "M4 7h10M18 7h2M4 17h2M10 17h10M14 5v4M8 15v4",
 "support": "M4 14v-2a8 8 0 0 1 16 0v2M4 14h3v5H4zM17 14h3v5h-3z",
 "lock": "M6 11h12v10H6zM8 11V7a4 4 0 0 1 8 0v4",
 "log": "M6 3h9l4 4v14H6zM9 12h7M9 16h7",
 "key": "M7 14a4 4 0 1 1 3.9-5H21v3h-3v3h-3v-3h-4.1A4 4 0 0 1 7 14z",
 "spark": "M12 3l2 6 6 2-6 2-2 6-2-6-6-2 6-2z",
 "server": "M3 5h18v6H3zM3 13h18v6H3zM7 8h.01M7 16h.01",
 "link": "M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1",
 "eye": "M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12zM12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6",
 "users": "M16 20v-2a4 4 0 0 0-8 0v2M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8",
 "phone": "M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z",
}
def ic(n): return f'<span class="ico" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="{IC[n]}"/></svg></span>'

NAV = [("Solutions", "/solutions/"), ("CUSTODIAN CBS", "/custodian/"), ("Infrastructure", "/custodian/#infrastructure"),
       ("Security & Compliance", "/security/"), ("Clients", "/clients/"), ("Resources", "/resources/"), ("Contact", "/contact/")]

FAQ = [
 ("What is a browser-less core banking system?", "In CUSTODIAN, the application and the data sit in a central data center. Branches connect to it over secure networks, so there is nothing to maintain in each branch’s web browser and policies stay consistent across the bank."),
 ("How long does implementation take?", "It depends on the number of branches, the data to be migrated and the bank’s configuration needs. After a discovery study we share a realistic timeline for your bank rather than a one-size-fits-all number."),
 ("How is data migration handled?", "Existing data is mapped, migrated and tested before go-live. Our team has experience migrating banks from other core banking software, and the process includes validation with your staff."),
 ("How is security handled?", "CUSTODIAN is designed with role-based access control, encrypted data transmission and audit logs. Data and application stay centralized in a monitored data center instead of being spread across branches."),
 ("Can CUSTODIAN integrate with ATMs?", "Yes. CUSTODIAN supports ATM and EFT switch interfaces, along with other delivery channels such as mobile banking, internet banking, POS and KIOSK. Specific scope is confirmed during consultation."),
 ("What about disaster recovery?", "A central data center makes it practical to plan a disaster-recovery site and business-continuity process. LIST also offers data center and DR infrastructure setup services."),
 ("What support do we receive after go-live?", "Dedicated implementation and support engineers help your teams with training, queries and continuous improvement after go-live."),
 ("How does pricing work?", "Pricing depends on bank size, branches, modules and infrastructure. Book a demo or consultation and we will prepare a quote based on your requirements."),
]
RES = [
 ("Blog", "What is a browser-less core banking system?", "A plain-language introduction for directors and managers."),
 ("Whitepapers", "Centralized banking: benefits and trade-offs", "How a single data center changes control, reporting and risk."),
 ("Compliance updates", "Staying on top of regulatory circulars", "How CBS configuration supports statutory and regulatory reporting."),
 ("Product guides", "CUSTODIAN modules at a glance", "Deposits, loans, NPA, delivery channels and add-on modules."),
 ("Case studies", "Migrating a co-operative bank to CUSTODIAN", "Lessons from branch rollout and training."),
 ("FAQs", "Planning your CBS data migration", "Questions to ask before you switch core banking vendors."),
]
CLIENTS = ["Ichalkaranji Co-op Bank", "Jankalyan Nagari Sahakari Patsanstha, Karad", "Lokmangal Co-operative Bank", "Panchganga Bank", "Manorama Co-operative Bank",
 "Pimpri Chinchwad Sahakari Bank", "Rajapur Urban Co-op Bank", "Samarth Sahakari Bank, Solapur", "Sangli Urban Bank", "Sangola Urban Co-op Bank", "Shiv Daulat Bank",
 "Ajara Urban Co-op Bank", "Mayani Urban Co-op Bank", "DNS Bank, Ambajogai", "Chitnavispura Sahakari Bank, Nagpur"]

def esc(s): return html.escape(s, quote=True)

def header(path):
    links = "".join(f'<a href="{u}"{" aria-current=page" if u.rstrip("/") == path.rstrip("/") and "#" not in u else ""}>{esc(n)}</a>' for n, u in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap"><a class="logo" href="/" aria-label="LIST Software home"><b class="mark" role="img" aria-label="LIST"></b><span><small>Software · CUSTODIAN CBS</small></span></a>
<nav class="menu" id="menu" aria-label="Main">{links}</nav>
<button class="iconbtn" id="theme" aria-label="Toggle light or dark theme" style="margin-left:.5rem">◐</button>
<a class="btn sm top" href="/contact/">Book a Demo</a>
<button class="iconbtn burger" id="burger" aria-label="Menu" aria-expanded="false" aria-controls="menu">☰</button></div></header>'''

def footer():
    return f'''<footer><div class="wrap"><div class="grid">
<div><a class="logo" href="/"><b class="mark" role="img" aria-label="LIST"></b><span><small>Software Pvt. Ltd.</small></span></a><p style="margin-top:1rem">Powering secure, intelligent, future-ready banking for India’s co-operative sector.</p>
<p><a href="https://www.linkedin.com/company/list-software-pvt-ltd---india" rel="noopener" target="_blank">LinkedIn</a> · <a href="https://www.facebook.com/listspl/" rel="noopener" target="_blank">Facebook</a></p></div>
<div><h3>Solutions</h3><ul><li><a href="/custodian/">CUSTODIAN CBS</a></li><li><a href="/solutions/">Mobile &amp; Internet Banking</a></li><li><a href="/solutions/">AML &amp; C-KYC</a></li><li><a href="/security/">Security &amp; Compliance</a></li></ul></div>
<div><h3>Company &amp; Resources</h3><ul><li><a href="/clients/">Clients &amp; Case Studies</a></li><li><a href="/resources/">Resources</a></li><li><a href="/careers/">Careers</a></li><li><a href="/news/">News &amp; Milestones</a></li><li><a href="/contact/">Contact</a></li><li><a href="/sitemap.xml">Sitemap</a></li></ul></div>
<div><h3>Contact</h3><ul><li><a href="tel:{PHONE_TEL}">{PHONE}</a></li><li><a href="tel:+912312669164">0231 2669164</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{HOURS}</li></ul></div></div>
<p style="margin-top:2rem;font-size:.9rem">© LIST Software Pvt. Ltd. All rights reserved. · <a href="/privacy/">Privacy Policy</a> · <a href="/terms/">Terms</a> · ISO 9001:2015 certified</p></div></footer>
<div class="float"><a class="btn" href="/contact/">Book a Demo</a><a class="wa" href="https://wa.me/{PHONE_TEL.lstrip("+")}?text=Hello%20LIST%20Software%2C%20I%27d%20like%20a%20CUSTODIAN%20demo" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">WA</a></div>
<dialog id="cb" aria-labelledby="cbt"><h2 id="cbt" style="font-size:1.6rem">Request a callback</h2><p>Share your number and we’ll call you back during working hours.</p>{cbform()}<button class="btn ghost sm" data-close type="button">Close</button></dialog>
<dialog id="invite" aria-labelledby="it"><h2 id="it" style="font-size:1.6rem">See CUSTODIAN in action</h2><p>Get a personalized demo for your bank. No obligation.</p><div class="ctas"><a class="btn" href="/contact/">Get a personalized demo</a><button class="btn ghost" data-close type="button">Not now</button></div></dialog>
<div class="consent" id="consent" role="region" aria-label="Cookie consent"><p>We use privacy-friendly analytics only if you agree. Essential features work without it.</p><button class="btn sm" id="cyes">Accept</button><button class="btn sm ghost" id="cno">Decline</button></div>'''

def cbform():
    return '''<form data-api="/callback" novalidate><div class="field"><label for="cbn">Name</label><input id="cbn" name="name" autocomplete="name" data-v="name"><span class="err" role="alert"></span></div>
<div class="field"><label for="cbp">Phone</label><input id="cbp" name="phone" type="tel" autocomplete="tel" data-v="phone"><span class="err" role="alert"></span></div>
<input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"><button class="btn" type="submit">Request a callback</button><div class="msg" role="status"></div></form>'''

def page(path, title, desc, body, crumbs=None, extra_ld=""):
    url = SITE + path
    org = {"@context": "https://schema.org", "@type": "Organization", "name": "LIST Software Pvt. Ltd.", "url": SITE, "logo": SITE + "/assets/img/favicon.svg",
           "telephone": PHONE, "email": EMAIL, "address": {"@type": "PostalAddress", "streetAddress": "Rahul Complex, Opp. Tata Petrol Pump, Guest House Gandhi Nagar, Vishrambag", "addressLocality": "Sangli", "addressRegion": "Maharashtra", "postalCode": "416415", "addressCountry": "IN"}}
    ld = [org]
    if path == "/custodian/" or path == "/":
        ld.append({"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "CUSTODIAN Core Banking Solution", "applicationCategory": "FinanceApplication", "operatingSystem": "Server-hosted, browser-less client", "publisher": {"@type": "Organization", "name": "LIST Software Pvt. Ltd."}})
    if "FAQ_HERE" in body:
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]})
    bc = ""
    if crumbs:
        items = [("Home", SITE + "/")] + [(n, SITE + u) for n, u in crumbs]
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]})
        bc = f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / {esc(crumbs[-1][0])}</nav>'
    body = body.replace("FAQ_HERE", "").replace("CRUMBS", bc)
    ldtxt = "".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in ld)
    return f'''<!doctype html><html lang="en-IN" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/og.jpg"><meta property="og:locale" content="en_IN"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#060b1a"><link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/css/styles.css?v={VER}">
<script>try{{document.documentElement.dataset.theme=localStorage.getItem("theme")||"light"}}catch(e){{}}</script>{ldtxt}</head>
<body>{header(path)}<main id="main">{body}</main>{footer()}<script src="/assets/js/chatbot-kb.js?v={VER}" defer></script><script src="/assets/js/chatbot.js?v={VER}" defer></script><script src="/assets/js/main.js?v={VER}" defer></script></body></html>'''

def head(eyebrow, h, lead):
    return f'<section class="phero"><div class="wrap">CRUMBS<span class="eyebrow">{esc(eyebrow)}</span><h1>{h}</h1><p class="lead">{esc(lead)}</p></div></section>'

def sec(eyebrow, h, lead="", inner="", center=False, sid=""):
    i = f' id="{sid}"' if sid else ""
    return f'<section{i}><div class="wrap{" center" if center else ""}"><span class="eyebrow">{esc(eyebrow)}</span><h2 class="reveal">{h}</h2>{f"<p class=lead>{esc(lead)}</p>" if lead else ""}<div style="margin-top:2rem">{inner}</div></div></section>'

def cards(items, cols="g3"):
    return f'<div class="grid {cols}">' + "".join(f'<article class="card reveal">{ic(i)}<h3>{esc(t)}</h3><p>{esc(d)}</p></article>' for i, t, d in items) + '</div>'

def net_svg(label="VPN"):
    nodes = [(90, 70, "Branch"), (510, 70, "ATM"), (60, 230, "Mobile users"), (540, 230, "Reports & MIS"), (110, 390, "Branch"), (490, 390, "Internet banking")]
    lines = "".join(f'<line class="ln" x1="300" y1="230" x2="{x}" y2="{y}"/>' for x, y, _ in nodes)
    nds = "".join(f'<g><rect class="nd" x="{x-55}" y="{y-24}" width="110" height="48" rx="14"/><text x="{x}" y="{y+5}">{n}</text></g>' for x, y, n in nodes)
    return f'''<svg class="net" viewBox="0 0 600 460" role="img" aria-label="Diagram: a secure central data center connected to bank branches, ATMs, mobile users and reporting systems over {label}">
<defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3b82ff"/><stop offset=".6" stop-color="#22d3ee"/><stop offset="1" stop-color="#8b5cf6"/></linearGradient></defs>
{lines}<circle class="pulse" cx="300" cy="230" r="46"/><circle class="dc" cx="300" cy="230" r="46"/>
<text x="300" y="226" style="fill:#fff">Secure</text><text x="300" y="244" style="fill:#fff">Data Center</text>{nds}
<text class="linklabel" x="300" y="440" style="fill:var(--cyan)">{label}</text></svg>'''

def hero():
    return f'''<section class="hero"><div class="wrap"><div><span class="eyebrow">Browser-less core banking · ISO 9001:2015 certified</span>
<h1>Future-Ready <span class="grad">Core Banking</span> for Co-operative Banks</h1>
<p class="lead">CUSTODIAN helps banks modernize operations, centralize data, improve compliance, and serve customers securely—at every branch.</p>
<div class="ctas"><a class="btn" href="/contact/">Book a Free Demo</a><a class="btn ghost" href="/custodian/">Explore CUSTODIAN</a></div>
<div class="trust"><div><b>✓</b> Serving 100+ banks</div><div><b>✓</b> 800+ branches</div><div><b>✓</b> Serving banks since 1997</div><div><b>✓</b> ISO 9001:2015 certified</div></div></div>
<div>{net_svg()}</div></div></section>'''

def challenges():
    ch = [("link", "Fragmented branch systems", "Data and processes differ from branch to branch."), ("log", "Manual processes", "Paper-heavy work slows teams and invites errors."),
          ("shield", "Compliance pressure", "Regulatory and statutory reporting keeps growing."), ("eye", "Limited real-time visibility", "Management waits for reports instead of seeing the bank today."),
          ("dr", "Disaster-recovery risk", "Scattered servers make continuity hard to plan."), ("users", "Rising customer expectations", "Customers expect digital channels and fast service.")]
    left = '<ul>' + "".join(f"<li><strong>{esc(t)}</strong> — {esc(d)}</li>" for _, t, d in ch) + '</ul>'
    ben = [("db", "One centralized core", "Application and data hosted at a central data center."), ("chart", "Real-time reporting", "Consistent MIS available from the center."),
           ("shield", "Compliance support", "Designed to support statutory and regulatory reporting."), ("dr", "Continuity planning", "Centralization makes DR practical to plan.")]
    return sec("Challenge to solution", 'Banking is evolving. <span class="grad">Your core systems should too.</span>', "", f'<div class="vs"><div class="card bad"><h3>Today’s common challenges</h3>{left}</div><div>{cards(ben, "g2")}</div></div>')

def product(full=False):
    inner = f'''<div class="arch"><div><ol><li><strong>Central data center</strong> hosts the application and the data.</li><li><strong>Branches connect securely</strong> through VPN, RF, MPLS or leased lines.</li><li><strong>Centralized policies,</strong> reporting and delivery channels.</li><li><strong>Configurable workflows</strong> for each bank.</li></ol>
<p>Choose a connection type to explore:</p><div class="tabs" role="group" aria-label="Connectivity options"><button data-link="VPN" aria-pressed="true">VPN</button><button data-link="RF" aria-pressed="false">RF</button><button data-link="MPLS" aria-pressed="false">MPLS</button><button data-link="Leased line" aria-pressed="false">Leased line</button></div>
<p id="linkdesc" aria-live="polite">{esc("Encrypted VPN tunnels give each branch a private path to the data center.")}</p></div><div>{net_svg()}</div></div>'''
    return sec("CUSTODIAN", 'A centralized, browser-less <span class="grad">core banking platform</span>', "Designed for co-operative banks and credit societies, with every branch working from the same data center.", inner, sid="infrastructure")

def capabilities():
    c = [("bank", "Core Banking Operations", "Savings, fixed, recurring and pigmy deposits, term loans, NPA identification and provisioning."), ("link", "Centralized Data & Branch Connectivity", "One data center, every branch connected over secure networks."),
         ("chart", "Real-Time Reporting & MIS", "Reports generated directly from the center for faster decisions."), ("shield", "Regulatory & Statutory Compliance Support", "Designed to support statutory and regulatory requirements."),
         ("card", "ATM and Delivery-Channel Integration", "ATM switch, internet and mobile banking, POS and KIOSK."), ("dr", "Disaster Recovery & Business Continuity", "Centralized setup that supports DR planning."),
         ("sliders", "Parameterized Bank Configuration", "Configure products and workflows to each bank’s needs."), ("support", "Implementation, Training & Support", "Engineers who guide rollout and stay after go-live.")]
    return sec("Key capabilities", 'Everything your bank needs, <span class="grad">from one core</span>', "", cards(c, "g4"))

def ai():
    a = [("spark", "AI-assisted MIS insights and anomaly alerts", "Roadmap"), ("chart", "Predictive dashboards for deposits, loans, NPAs and branch performance", "Roadmap"),
         ("users", "Intelligent customer-service workflows", "Roadmap"), ("log", "Digital onboarding and paperless processes", "Available through consultation"),
         ("eye", "Advanced fraud-risk signals and audit trails", "Roadmap"), ("link", "API-ready integrations for payments, KYC, credit bureaus and third-party services", "Available through consultation")]
    return sec("What’s next", 'Built for the <span class="grad">next era of banking</span>', "Optional, future-ready modules. Each is labelled so you always know what is available today.",
        '<div class="grid g3">' + "".join(f'<article class="card reveal">{ic(i)}<span class="tag">{s}</span><h3 style="font-size:1.1rem">{esc(t)}</h3></article>' for i, t, s in a) + '</div>')

def security(full=False):
    s = [("key", "Role-based access control", "Staff see and do only what their role allows."), ("lock", "Encrypted data transmission", "Branch-to-center traffic travels over secure networks."), ("log", "Audit logs", "Track who did what, and when."),
         ("dr", "Disaster recovery", "A path to restore operations after disruption."), ("shield", "RBI-aligned compliance support", "Designed to support regulatory reporting needs."), ("server", "Data-center hosting", "Application and data kept in one managed location.")]
    return sec("Security & compliance", 'Security, continuity, and <span class="grad">compliance at the core</span>', "Your banking data and application remain centralized, monitored, and recoverable.", cards(s))

def why():
    w = [("bank", "In operation since 1997", "Focused on co-operative banking."), ("users", "100+ banks and credit societies served", "Across India."), ("link", "800+ branches supported", "Connected to central data centers."),
         ("support", "Dedicated implementation and support engineers", "Your point of contact."), ("spark", "Customer-first service approach", "Long-term relationships."), ("dr", "Migration and modernization experience", "Banks have moved to CUSTODIAN from other software."), ("shield", "ISO 9001:2015 certified", "Quality-managed processes.")]
    return sec("Why LIST Software", 'A partner that <span class="grad">understands co-operative banking</span>', "", cards(w))

from clients import CLIENT_LOGOS

def logo_items():
    return "".join(f'<span><img src="/assets/img/clients/{f}" data-remote="https://listspl.co.in/img/clients/{f}" alt="{esc(n)}" loading="lazy" height="44"></span>' for n, f in CLIENT_LOGOS) + "<span><b>and 85+ more banks</b></span>"

def metrics():
    m = [(1997, "", "Serving Banks Since"), (75, "+", "Skilled Employees"), (100, "+", "Bank Clients"), (800, "+", "Branches Served")]
    return '<section class="metrics"><div class="wrap"><div class="grid g4">' + "".join(f'<div class="card"><div class="num grad" data-count="{n}" data-suffix="{s}">0</div><p>{l}</p></div>' for n, s, l in m) + '</div></div></section>'

def testimonials(marq=True):
    t = [("We are using Distributed Core Banking System developed and supplied by LIST Software Pvt Ltd Sangli. We also have a setup of 6 ATMs with national connectivity to the banks’ network. The systems are working satisfactorily.", "Samarth Sahakari Bank Ltd.", "Solapur", "6 ATMs with national connectivity"),
         ("We recently migrated to LIST Software’s Custodian Core Banking Solution in all four branches and Head Office. The results of this migration are very good and have helped us achieve a fine level of automation. LIST has a very good implementation strategy and satisfactory service support.", "Pimpri-Chinchwad Sahakari Bank Maryadit", "Pimpri", "Migrated 4 branches + Head Office")]
    q = '<div class="grid g2">' + "".join(f'<blockquote class="card q reveal"><p>“{esc(x)}”</p><cite>{esc(b)}</cite><small>{esc(l)} · {esc(m)}</small></blockquote>' for x, b, l, m in t) + '</div>'
    mq = logo_items()
    return sec("Client success", 'Trusted by <span class="grad">100+ banks</span>', "", q + (f'<div class="marq" aria-label="Client banks"><div>{mq}{mq}</div></div>' if marq else ''))

def cases():
    c = [("Rajapur Urban Bank", "Needed a dependable core banking platform for its branches.", "CUSTODIAN with a central data center and secure branch connectivity.", "Centralized operations and reporting."),
         ("Samarth Bank, Solapur", "Operating several branches and ATMs on a connected network.", "Distributed core banking with ATM connectivity.", "6 ATMs on national connectivity; system working satisfactorily.")]
    return sec("Case studies", 'Real results from <span class="grad">real banks</span>', "", '<div class="grid g2">' + "".join(f'<article class="card reveal"><h3>{esc(n)}</h3><p><strong>Challenge:</strong> {esc(a)}</p><p><strong>Solution:</strong> {esc(b)}</p><p><strong>Outcome:</strong> {esc(d)}</p><p style="margin-top:1rem"><a class="btn sm ghost" href="/contact/?topic=case-study">Read case study</a></p></article>' for n, a, b, d in c) + '</div>')

def journey():
    s = [("Discovery & requirement study", "We learn your branches, products and goals."), ("Solution configuration", "CUSTODIAN is parameterized to your bank."), ("Data migration & testing", "Your data is migrated and validated."),
         ("Branch rollout & training", "Staff are trained branch by branch."), ("Go-live, support & continuous improvement", "We stay with you after launch.")]
    return sec("Implementation journey", 'Five steps from <span class="grad">first call to go-live</span>', "", '<ol class="steps">' + "".join(f"<li><strong>{esc(t)}</strong>{esc(d)}</li>" for t, d in s) + '</ol>')

def resources(limit=None):
    cats = ["All", "Blog", "Whitepapers", "Compliance updates", "Product guides", "Case studies", "FAQs"]
    btns = "".join(f'<button class="btn sm ghost" data-cat="{"all" if c == "All" else esc(c)}" aria-pressed="{str(c == "All").lower()}" type="button">{c}</button>' for c in cats)
    items = RES[:limit] if limit else RES
    cs = "".join(f'<article class="card" data-res data-cat="{esc(c)}"><span class="tag">{esc(c)}</span><h3>{esc(t)}</h3><p>{esc(d)}</p><p style="margin-top:1rem"><a href="/contact/?topic=resource">Request this resource →</a></p></article>' for c, t, d in items)
    return sec("Resources", 'Guides and updates for <span class="grad">banking leaders</span>', "", f'<div class="search"><label class="sr" for="rsearch" style="position:absolute;left:-9999px">Search resources</label><input id="rsearch" type="search" placeholder="Search resources…"></div><div id="rcats" class="tabs" role="group" aria-label="Categories">{btns}</div><div class="grid g3">{cs}</div><p id="rempty" hidden>No resources match your search.</p>')

def faq():
    return sec("FAQ", 'Questions bank leaders <span class="grad">often ask</span>', "", "FAQ_HERE" and ("".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in FAQ)) + "FAQ_HERE")

def cta():
    return f'''<section><div class="wrap"><div class="cta"><h2>Ready to modernize your bank’s core banking?</h2><p class="lead" style="margin-inline:auto">Get a personalized demo, or speak to a banking-software expert.</p>
<div class="ctas"><a class="btn" href="/contact/">Book a Demo</a><button class="btn ghost" data-open="cb" type="button">Talk to a Banking Expert</button></div>
<p><a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div></section>'''

def contact_form():
    f = lambda i, l, t="text", v="", req=True, ph="": f'<div class="field"><label for="{i}">{l}{" *" if req else ""}</label><input id="{i}" name="{i}" type="{t}" {f"data-v={v}" if v else ""} placeholder="{ph}"><span class="err" role="alert"></span></div>'
    form = f'''<form class="card" data-api="/leads" novalidate>
{f("name", "Full name", v="name")}{f("bank", "Bank / credit society name", v="bank")}
<div class="field"><label for="role">Role</label><select id="role" name="role"><option>Director / Chairman</option><option>CEO / General Manager</option><option>IT Head</option><option>Branch Manager</option><option>Compliance / Audit</option><option>Other</option></select></div>
{f("email", "Email", "email", "email")}{f("phone", "Phone", "tel", "phone")}{f("branches", "Number of branches", "number", "branches", False)}{f("software", "Current banking software", req=False)}
<div class="field"><label for="requirement">Main requirement *</label><textarea id="requirement" name="requirement" rows="4" data-v="requirement"></textarea><span class="err" role="alert"></span></div>
<div class="field"><label for="demo_time">Preferred demo time</label><input id="demo_time" name="demo_time" type="datetime-local"></div>
<input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn" type="submit">Get a personalized demo</button><div class="msg" role="status"></div><p style="font-size:.85rem;margin-top:1rem">By submitting you agree to be contacted about CUSTODIAN. See our <a href="/privacy/">Privacy Policy</a>.</p></form>'''
    info = f'''<div><div class="card"><h3>Speak to a banking-software expert</h3><p><a href="tel:{PHONE_TEL}">{PHONE}</a></p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p><a href="https://wa.me/{PHONE_TEL.lstrip("+")}" target="_blank" rel="noopener">Chat on WhatsApp</a></p><p><strong>Hours:</strong> {HOURS}</p><p><strong>Office:</strong> {ADDR}</p><button class="btn ghost" data-open="cb" type="button">Request a Callback</button></div></div>'''
    return f'<section><div class="wrap"><div class="grid g2" style="align-items:start">{form}{info}</div></div></section>'

def solutions_list():
    s = [("bank", "CUSTODIAN Core Banking", "Deposits, loans, NPA, run from one data center."), ("phone", "Mobile Banking", "Balance, mini statement, fund transfer and more."), ("shield", "Anti-Money Laundering", "Name screening and FIU-IND reporting support."),
         ("users", "C-KYC", "Upload to CERSAI and fetch records by CKYC ID."), ("chart", "Credit Appraisal", "Analyse borrower risk before disbursement."), ("link", "CTS Interface", "Cheque truncation system integration."),
         ("log", "Audit Module", "Support for audit workflows."), ("card", "APBS / DBTL / NACH", "Direct benefit and mandate processing."), ("users", "Agency Banking", "Doorstep banking through agents."),
         ("lock", "Internet Banking", "24x7 online banking services."), ("log", "Loan Document Printing", "Standardized loan documents."), ("support", "e-Passbook & Statement on Email", "Digital statements for customers.")]
    return cards(s)


def serve():
    items = [("bank", "Urban co-operative banks", "Run every branch from one data center, with RBI statements, audit and delivery channels built in."),
             ("users", "Credit societies", "Deposit, pigmy and loan management with member records, C-KYC and statutory reports."),
             ("db", "Nagari sahakari patsansthas", "Highly parameterized products and light system load, so you can start simple and add modules later.")]
    return sec("Who we serve", 'Built for <span class="grad">every kind of co-operative institution</span>', "", cards(items))

def life():
    g = [("life-team", "The LIST family at our office"), ("life-puja", "Starting together with a puja at the office"), ("life-decor", "Festive decoration at LIST")]
    ph = "".join(f'<figure class="shot reveal"><button type="button" data-zoom="/assets/img/life/{n}.jpg" aria-label="Enlarge photo: {c}"><img src="/assets/img/life/{n}.jpg" alt="{c}" loading="lazy" width="800" height="600"></button><figcaption>{c}</figcaption></figure>' for n, c in g)
    ph = ""
    vid = '<figure class="shot vid reveal"><video controls playsinline preload="none" poster="/assets/img/life/life-video.jpg"><source src="/assets/img/life/life-video.mp4" type="video/mp4"></video><figcaption>A moment from life at LIST</figcaption></figure>'
    pts = [("users", "A team of 75+", "Software professionals and support engineers who work with co-operative banks every day."),
           ("shield", "Recognised for people practices", "Best HR Practices Award by TLC (2014)."),
           ("chart", "Support that stays", "Support engineers on standby, and most customers who moved to LIST have stayed with us.")]
    return sec("Life at LIST", 'The people <span class="grad">behind CUSTODIAN</span>', "We build and support banking software for co-operative banks. Join us if that sounds like work worth doing.", f'<div>' + cards(pts) + '</div><p style="margin-top:1.5rem"><a class="btn" href="/careers/">See careers</a></p>')

import re as _re
def alogo(uid, cls=""):
    svg = open(ROOT + "/assets/img/list-logo-full.svg", encoding="utf-8").read()
    vb = _re.search(r'viewBox="([^"]+)"', svg).group(1); d = _re.search(r' d="([^"]+)"', svg).group(1)
    return (f'<svg class="alogo {cls}" viewBox="{vb}" role="img" aria-label="LIST – Empowering Business"><defs><linearGradient id="{uid}" spreadMethod="repeat" x1="0" y1="0" x2=".6" y2="0"><stop offset="0" stop-color="#2563eb"/><stop offset=".35" stop-color="#22d3ee"/><stop offset=".7" stop-color="#8b5cf6"/><stop offset="1" stop-color="#2563eb"/><animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="0.6 0" dur="7s" repeatCount="indefinite"/></linearGradient></defs><path pathLength="1" fill="url(#{uid})" stroke="url(#{uid})" fill-rule="evenodd" d="{d}"/></svg>')

def brand():
    v = [("shield", "Reliable", "ISO 9001:2015 certified software, built to run banks every day."),
         ("users", "Close to our customers", "Support engineers on standby for co-operative banks."),
         ("bank", "Built for co-operatives", "Made for urban co-operative banks, credit societies and patsansthas."),
         ("chart", "Experienced", "Building core banking software since 1997.")]
    return sec("Our brand", 'What the <span class="grad">LIST name</span> stands for', "", alogo("lgb", "brand-logo") + cards(v))

def roadmap():
    r = [("phone", "Loan and recovery reminders", "Planned: SMS and WhatsApp reminders for instalments due and overdue, linked to NPA identification."),
         ("users", "Grievance management", "Planned: log, assign and track customer complaints with escalation and reports."),
         ("chart", "Customer engagement messages", "Planned: FD maturity, recurring deposit and statement notices on the customer's preferred channel.")]
    return sec("On our roadmap", 'What we are <span class="grad">building next</span>', "Tell us which would help your bank most.", cards(r) + '<p style="margin-top:1.5rem"><a class="btn ghost" href="/contact/">Register interest</a></p>')

def careers_form():
    fld = lambda i, l, v="", req=True, t="text": f'<div class="field"><label for="{i}">{l}{" *" if req else ""}</label><input id="{i}" name="{i}" type="{t}" {f"data-v={v}" if v else ""}><span class="err" role="alert"></span></div>'
    return f'''<section><div class="wrap" style="max-width:720px"><form class="card" data-api="/careers" novalidate>
{fld("name","Full name","name")}{fld("email","Email","email",True,"email")}{fld("phone","Phone","phone",True,"tel")}{fld("role","Role you are interested in",req=False)}{fld("cv","Link to your CV (Google Drive, LinkedIn)",req=False)}
<div class="field"><label for="requirement">About you *</label><textarea id="requirement" name="requirement" rows="5" data-v="requirement"></textarea><span class="err" role="alert"></span></div>
<input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn" type="submit">Send application</button><div class="msg" role="status"></div></form></div></section>'''

def news_body():
    ms = [("1997", "LIST Software starts operations"), ("2014", "Best HR Practices Award by TLC"), ("2017", "Best Financial Management Award by TLC"), ("Award", "Business Excellence Award by TLC"), ("Certified", "ISO 9001:2015 certification")]
    return sec("Milestones", 'Our journey <span class="grad">so far</span>', "", '<div class="card"><ul>' + "".join(f"<li><strong>{a}</strong> — {b}</li>" for a, b in ms) + '</ul></div>')

def arch():
    import math
    cx,cy=350,170; br=[]; ln=""
    names=["Branch 1","Branch 2","Branch 3","Branch 4","Branch 5","Branch 6"]; links=["VPN","MPLS","Leased line","RF","VPN","MPLS"]
    for i,(n,l) in enumerate(zip(names,links)):
        a=math.pi*2*i/6-math.pi/2; x=cx+250*math.cos(a); y=cy+120*math.sin(a)
        ln+=f'<line class="al" x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" style="animation-delay:{i*.25}s"/><circle class="ap" r="4"><animateMotion dur="2.4s" begin="{i*.4}s" repeatCount="indefinite" path="M{x:.0f},{y:.0f} L{cx},{cy}"/></circle>'
        br.append(f'<g class="ab" style="animation-delay:{i*.15}s"><rect x="{x-46:.0f}" y="{y-17:.0f}" width="92" height="34" rx="9"/><text x="{x:.0f}" y="{y-1:.0f}" text-anchor="middle">{n}</text><text class="s" x="{x:.0f}" y="{y+11:.0f}" text-anchor="middle">{l}</text></g>')
    svg=f'<svg class="arch" viewBox="0 0 700 340" role="img" aria-label="Branches connected to one central data center">{ln}<g class="ac"><circle cx="{cx}" cy="{cy}" r="44"/><text x="{cx}" y="{cy-2}" text-anchor="middle">Data</text><text x="{cx}" y="{cy+14}" text-anchor="middle">Center</text></g>{"".join(br)}</svg>'
    return sec("How it works", 'One data center. <span class="grad">Every branch connected.</span>', "Data and application stay in one place. Branches connect over VPN, RF, MPLS or leased line, and need no browser setup.", f'<div class="card" data-mr-h>{svg}</div>')

def demo():
    tabs=[("Account opening",[("Customer name","Sample Customer"),("Product","Savings account"),("C-KYC ID","Fetched from CERSAI"),("Branch","Main branch")]),
          ("Loan sanction",[("Borrower","Sample Borrower"),("Product","Term loan"),("Credit appraisal","Risk analysed"),("Status","Ready for sanction")]),
          ("NPA & reports",[("Report","NPA identification"),("Provisioning","Calculated"),("Statement","RBI return"),("Audit log","Recorded")])]
    b="".join(f'<button type="button" role="tab" aria-selected="{str(i==0).lower()}" data-d="{i}">{t}</button>' for i,(t,_) in enumerate(tabs))
    pn="".join(f'<div class="dp" role="tabpanel" data-p="{i}"{"" if i==0 else " hidden"}>'+"".join(f'<div class="dr"><span>{k}</span><b>{v}</b></div>' for k,v in rows)+'<div class="dbtn">Submit</div></div>' for i,(t,rows) in enumerate(tabs))
    return sec("See it in action","A quick look at <span class=\"grad\">CUSTODIAN workflows</span>","Illustrative screens with sample data. Book a demo to see the real software.",f'<div class="demo"><div class="dt" role="tablist">{b}</div><div class="dw"><div class="dbar"><i></i><i></i><i></i><span>CUSTODIAN</span></div>{pn}</div></div><p style="margin-top:1rem"><a class="btn" href="/contact/">Book a live demo</a></p>')

def timeline():
    ev=[("1997","LIST Software begins building co-operative banking software"),("2014","Best HR Practices Award by TLC"),("2017","Best Financial Management Award by TLC"),("ISO 9001:2015","Quality management certification"),("Today","100+ banks served with CUSTODIAN")]
    return sec("Our journey","Growing with co-operative banks <span class=\"grad\">since 1997</span>","","<ol class=\"tl\">"+"".join(f'<li class="reveal"><b>{y}</b><span>{t}</span></li>' for y,t in ev)+"</ol>")

def home2():
    hero_ = f'''<section class="hero"><div class="wrap"><div>{alogo("lgh", "hero-logo")}<span class="eyebrow">ISO 9001:2015 certified</span>
<h1>Looking for <span class="grad" id="rot" data-words="Core Banking Software?|Mobile Banking?|AML and C-KYC?|a Reliable Banking Partner?">Core Banking Software?</span></h1>
<p class="lead" data-mr="तुम्ही पहिल्यांदाच कोअर बँकिंग सॉफ्टवेअर शोधत असाल किंवा सध्याच्या सेवेवर समाधानी नसाल, तर आमच्याशी बोला. आम्हाला मदत करायला आनंद होईल.">If you are looking for Core Banking Software for the first time, or you are not happy with your current provider, talk to us. We will be happy to help.</p>
<div class="ctas"><a class="btn" href="/contact/"data-mr="डेमो मागवा">Request a Demo</a><a class="btn ghost" href="tel:{PHONE_TEL}">Call {PHONE}</a></div>
<div class="trust"><div><b>✓</b> 100+ banks served</div><div><b>✓</b> 800+ branches</div><div><b>✓</b> Since 1997</div><div><b>✓</b> Support engineers on standby</div></div></div>
<div>{net_svg()}</div></div></section>'''
    names = logo_items()
    trusted = f'<section style="padding:2rem 0"><div class="wrap center"><span class="eyebrow">Trusted by 100+ banks</span><div class="marq" aria-label="Client banks"><div>{names}{names}</div></div></div></section>'
    suite = [("bank", "CUSTODIAN Core Banking", "Savings, fixed, recurring and pigmy deposits. Term loans. NPA identification and provisioning. All run from one data center.", "/custodian/"),
             ("phone", "Mobile Banking", "Balance enquiry, mini statement, fund transfer, cheque book request, recharge and bill payment, 24x7.", "/solutions/"),
             ("shield", "Anti-Money Laundering", "Name screening and FIU-IND reports.", "/solutions/"),
             ("users", "C-KYC", "Uploads to CERSAI and fetches records by CKYC ID.", "/solutions/"),
             ("chart", "Credit Appraisal", "Analyses borrower risk before a loan is disbursed.", "/solutions/")]
    cs = "".join(f'<article class="card">{ic(i)}<h3>{t}</h3><p>{d}</p><p style="margin-top:1rem"><a href="{u}">Learn more →</a></p></article>' for i, t, d, u in suite)
    more = "".join(f"<span class='tag' style='color:var(--mut);border-color:var(--line)'>{x}</span> " for x in ["CTS Interface", "Audit Module", "APBS / DBTL / NACH", "Agency Banking", "Internet Banking", "Loan Document Printing", "Statement on Email", "e-Passbook"])
    s1 = sec("Solutions", "One suite for every <span class='grad'>co-operative banking need</span>", "", f'<div class="grid g3">{cs}</div><p style="margin-top:1.5rem"><strong>Also in the suite:</strong> {more}</p>')
    steps = [("db", "One data center", "All your data and the application sit in one data center. Every branch uses the same one."), ("link", "Every branch connected", "Branches connect over VPN, RF, MPLS or leased line."), ("chart", "Run from the center", "Policies, reports and delivery channels are managed centrally.")]
    s2 = sec("CUSTODIAN", "Core banking software, <span class='grad'>made for co-operative banks</span>", "No browser needed at the branch. Everything runs from your data center.", cards(steps) + '<p style="margin-top:1.5rem"><a class="btn ghost" href="/custodian/">See how it works</a></p>')
    ch = "".join(f"<span class='tag' style='font-size:.95rem;color:var(--ink);border-color:var(--line)'>{x}</span> " for x in ["ATM (EFT switch interface)", "Internet Banking", "Mobile Banking", "POS", "KIOSK", "Doorstep Banking"])
    s3 = sec("Delivery channels", "More delivery channels. <span class='grad'>One core.</span>", "ATM, Internet, Mobile, POS and KIOSK channels help you serve customers better and reach new ones, at a sensible cost.", f"<p>{ch}</p>")
    about = sec("About LIST", "Over two decades of <span class='grad'>co-operative banking software</span>", "LIST Software is an ISO 9001:2015 certified company, in operation since 1997, serving co-operative banks and credit societies. Our support engineers are always on standby, and most customers who moved to us have stayed with us.", "")
    sv = [("server", "CUSTODIAN CBS Implementation", "Browser-less CBS with data and application at a data center, configured to your bank."), ("dr", "Data Center & Disaster Recovery Setup", "Planning, building and managing your CBS data center, DR site and connectivity.")]
    s4 = sec("Services", "Implementation and infrastructure, <span class='grad'>handled for you</span>", "", cards(sv, "g2"))
    aw = "<ul><li>Best Financial Management Award by TLC (2017)</li><li>Best HR Practices Award by TLC (2014)</li><li>Business Excellence Award by TLC</li><li>ISO 9001:2015 certification</li></ul>"
    s5 = sec("Recognition", "Recognised <span class='grad'>for how we work</span>", "", f'<div class="card">{aw}</div>')
    return hero_ + trusted + metrics() + s1 + serve() + s2 + arch() + demo() + s3 + about + timeline() + brand() + life() + s4 + testimonials(False) + cases() + s5 + faq() + cta()

LEGAL_TXT = {
 "Privacy Policy": [("Who we are", "LIST Software Pvt. Ltd. (“LIST”, “we”) builds CUSTODIAN core banking software for co-operative banks and credit societies. This policy explains how we handle personal information collected through this website."),
  ("What we collect", "Details you submit in our forms or chat: name, bank or organisation, phone, email, number of branches, current software, your message, and for career applications the details and CV link you send. If you accept analytics cookies we also measure page visits in aggregate."),
  ("Why we use it", "To reply to enquiries, arrange demos and callbacks, handle job applications, improve this website and meet legal obligations. We do not sell your personal information."),
  ("Who sees it", "Our sales, support and HR teams, and service providers that help us run the website (hosting, email, spreadsheets). They may use it only to provide those services. We may disclose information where the law requires it."),
  ("How long we keep it", "Only as long as needed for the purpose it was collected, after which it is deleted or anonymised."),
  ("Your rights", "You may ask us to access, correct or delete your personal information, withdraw consent, or raise a grievance, as provided under India’s Digital Personal Data Protection Act, 2023. Write to bankingsales@listspl.co.in."),
  ("Cookies", "Essential storage is used for site features such as your theme choice. Analytics runs only if you accept it in the cookie banner."),
  ("Changes", "We may update this policy; the date below shows the latest version."),],
 "Terms of Use": [("Use of this website", "This website gives information about LIST Software Pvt. Ltd. and its products. By using it you agree to these terms."),
  ("Information", "We take care to keep the information accurate but it is provided for general information and may change. Product features, services and availability are confirmed only in a written agreement with LIST."),
  ("Intellectual property", "The website content, the LIST name and logo, and the CUSTODIAN name belong to LIST Software Pvt. Ltd. Client names and logos belong to their owners and are shown with their consent. Do not copy or reuse them without permission."),
  ("Acceptable use", "Do not misuse the website, attempt to disrupt or gain unauthorised access to it, or submit false or unlawful information."),
  ("Links and chat assistant", "Links to other websites are provided for convenience and we are not responsible for their content. The chat assistant gives general information and does not give quotations, prices or commitments."),
  ("Liability", "To the extent permitted by law, LIST is not liable for losses arising from use of, or inability to use, this website."),
  ("Governing law", "These terms are governed by the laws of India."),
  ("Contact", "Questions about these terms: bankingsales@listspl.co.in."),]}
def LEGAL(t):
    return f'<section><div class="wrap" style="max-width:780px"><h1>{t}</h1><p>Last updated: November 2026</p>' + "".join(f"<h2>{h}</h2><p>{b}</p>" for h, b in LEGAL_TXT[t]) + '</div></section>'

def write(path, html_):
    d = ROOT + path
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html_)

pages = {
 "/": ("Core Banking Software for Co-operative Banks | LIST Software", "CUSTODIAN is browser-less core banking software from LIST Software for co-operative banks and credit societies. ISO 9001:2015 certified, 100+ banks.", home2(), None),
 "/solutions/": ("Banking Software Solutions | LIST Software", "CBS, mobile banking, AML, C-KYC, credit appraisal and more for co-operative banks.", head("Solutions", 'One suite, built for every <span class="grad">co-operative banking need</span>', "Modules that work together around a single CUSTODIAN core.") + sec("Suite", "Solutions", "", solutions_list()) + ai() + roadmap() + cta(), [("Solutions", "/solutions/")]),
 "/custodian/": ("CUSTODIAN Core Banking Software | LIST Software", "Browser-less core banking for co-operative banks: central data center, secure branch connectivity, MIS and delivery channels.", head("CUSTODIAN CBS", 'The browser-less <span class="grad">core banking platform</span>', "Application and data in one data center. Every branch connected.") + product() + capabilities() + journey() + faq() + cta(), [("CUSTODIAN CBS", "/custodian/")]),
 "/security/": ("Security & Compliance | LIST Software", "Role-based access, encrypted transmission, audit logs and disaster recovery for co-operative banks.", head("Security & Compliance", 'Security, continuity and compliance <span class="grad">at the core</span>', "Designed so your data stays centralized, monitored and recoverable.") + security() + cta(), [("Security & Compliance", "/security/")]),
 "/clients/": ("Clients & Case Studies | LIST Software", "Co-operative banks that trust LIST Software and CUSTODIAN.", head("Clients", 'Trusted by <span class="grad">100+ banks</span>', "Co-operative banks and credit societies across India.") + testimonials() + metrics() + cases() + cta(), [("Clients", "/clients/")]),
 "/resources/": ("Resources | LIST Software", "Blog, whitepapers, compliance updates, product guides and FAQs for co-operative banks.", head("Resources", 'Insights for <span class="grad">banking leaders</span>', "Search by topic and filter by type.") + resources() + faq() + cta(), [("Resources", "/resources/")]),
 "/contact/": ("Book a Demo | LIST Software", "Request a personalized CUSTODIAN demo or callback from LIST Software, Sangli.", head("Contact", 'See CUSTODIAN <span class="grad">in action</span>', "Tell us about your bank and we will arrange a personalized demo.") + contact_form(), [("Contact", "/contact/")]),
 "/privacy/": ("Privacy Policy | LIST Software", "Privacy policy of LIST Software Pvt. Ltd.", LEGAL("Privacy Policy"), [("Privacy Policy", "/privacy/")]),
 "/terms/": ("Terms | LIST Software", "Terms of use of LIST Software Pvt. Ltd.", LEGAL("Terms of Use"), [("Terms", "/terms/")]),
}
pages["/careers/"] = ("Careers | LIST Software", "Join the LIST Software team building core banking software for co-operative banks.", head("Careers", 'Build banking software <span class="grad">that banks rely on</span>', "Send us your details and we will contact you when a suitable role opens.") + careers_form(), [("Careers", "/careers/")])
pages["/news/"] = ("News & Milestones | LIST Software", "Milestones, awards and certifications of LIST Software Pvt. Ltd.", head("News & Milestones", 'Awards and <span class="grad">milestones</span>', "A short history of LIST Software.") + news_body() + cta(), [("News & Milestones", "/news/")])
for p, (t, d, b, c) in pages.items():
    write(p, page(p, t, d, b, c))
open(ROOT + "/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}{p}</loc></url>" for p in pages) + "</urlset>")
open(ROOT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
os.makedirs(ROOT + "/../backend/data", exist_ok=True)
json.dump([{"category": c, "title": t, "summary": d} for c, t, d in RES], open(ROOT + "/../backend/data/resources.json", "w"), indent=2)
print("built", len(pages), "pages")

import sys, json as _j
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kb_data
open(ROOT + "/assets/js/chatbot-kb.js", "w", encoding="utf-8").write("window.LIST_KB=" + _j.dumps(kb_data.KB, ensure_ascii=False) + ";")
_j.dump(kb_data.KB, open(ROOT + "/../backend/data/knowledge.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("chatbot knowledge:", len(kb_data.KB), "topics")
