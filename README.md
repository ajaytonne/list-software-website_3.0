# LIST Software Pvt. Ltd. – Website

```
frontend/   Static site (HTML, CSS, JS) – what visitors see
  assets/css, assets/js, assets/img
  tools/build.py   Edit text/pages here, then run: python3 tools/build.py
backend/    Node.js (Express) – serves the site, saves demo/callback leads, optional email alerts
  src/server.js, data/resources.json, .env.example
```

## Run locally
```
cd backend
cp .env.example .env     # set ADMIN_TOKEN and (optionally) SMTP details
npm install
npm start                # http://localhost:3000
```
Pages use root-relative links (`/solutions/`), so open the site through the server, not by double-clicking the HTML files.

## Update content
Edit `frontend/tools/build.py` (FAQ, resources, clients, testimonials, page text), run `python3 tools/build.py`, refresh. It also regenerates `backend/data/resources.json`.

## Chatbot
A chat assistant ("Ask LIST") appears on every page. Its knowledge comes from the LIST Corporate Deck and website: edit `frontend/tools/kb_data.py`, then run `python3 tools/build.py`.
- Works out of the box by matching questions to that knowledge (no key needed).
- For free-form AI answers grounded in the same knowledge, set `ANTHROPIC_API_KEY` in `backend/.env` (endpoint: `POST /api/chat`).
- It never quotes prices or timelines; it points buyers to a demo or callback.

## Leads
Saved to `backend/data/leads.jsonl`; emailed to `MAIL_TO` if SMTP is set. Download via `GET /api/admin/leads` with header `x-admin-token`.
Spam protection: honeypot field, minimum fill time, rate limiting, input sanitising.

## Before going live – please verify
0. **Numbers differ between your sources**: the deck says "30+ years" and "1000+ branches" with phone 9971556323; the website and brief say 20+/23 years and 800+ branches with +91 95299 23868. The chatbot avoids these figures; decide one set and update the site and deck.
1. **Address, phone, years**: this site uses the Sangli address, +91 95299 23868 and "20+ years" from your brief. The current listspl.co.in shows a Kolhapur office, 0231 2669164 and "23 years".
2. **Case studies**: only the bank names exist on the old site; challenge/solution/outcome text is drafted from the testimonials. Replace with approved facts.
3. **Resources** are placeholders that link to the contact form; replace with real articles.
4. **Privacy Policy / Terms** are placeholders: add reviewed legal text.
5. Add `frontend/og.png` (1200×630) and client logos (use WebP, `loading="lazy"`). Client names currently appear as text chips.
6. Analytics: Plausible loads only after cookie consent; change `CONFIG` at the top of `assets/js/main.js` (or swap for GA).
7. Deploy behind HTTPS (e.g. Nginx + PM2, or any Node host). WhatsApp button uses the +91 95299 23868 number.

## Deploy on Render
1. Upload this whole folder to a new GitHub repository (keep `frontend/`, `backend/` and `render.yaml` at the top level).
2. In Render: New → Blueprint → select the repo. It reads `render.yaml` and creates the web service.
3. Fill the prompted variables: `SMTP_*` (so every demo request is emailed to you) and optionally `ANTHROPIC_API_KEY` (AI chatbot answers).
4. Open the `https://list-software-website.onrender.com`-style link Render gives you; later add your own domain under Settings → Custom Domains.
Notes: the free plan sleeps after inactivity (first visit is slow). Leads are also written to `backend/data/leads.jsonl`, which Render wipes on each redeploy, so rely on the email (or add a persistent disk).

## Added in this update
- Home: stat strip moved under the hero, Who we serve, Life at LIST. Solutions: roadmap section (planned items, confirm before publishing).
- New pages: /careers/ (form posts to /api/careers) and /news/. Both are in the sitemap and footer.
- Lead dashboard at /admin (enter ADMIN_TOKEN). Set SHEET_WEBHOOK_URL so leads also go to a Google Sheet and survive redeploys; HR_MAIL_TO routes career applications.

- Life at LIST (cards only; staff photos and video removed) in assets/img/life/. og.jpg (link-preview image) is cut from the team photo. Hero headline rotates, scroll progress bar, back-to-top button and card glow added.

- Brand: the LIST logo (traced to assets/img/list-logo.svg) is the header and footer mark, an animated logo in the 'Our brand' section, and three faint floating logos in the page background (injected by main.js, move with the cursor).

- Client logos: tools/clients.py lists the 15 client banks. Run `python tools/fetch_client_logos.py` (needs internet) to download their logos from listspl.co.in into assets/img/clients/, then `python tools/build.py`. A bank without a logo file shows its name instead. Numbers in the stats row now roll like an odometer when scrolled into view.

- Client logos load from assets/img/clients/ if present, otherwise straight from https://listspl.co.in/img/clients/ (allowed in the CSP), otherwise the bank name is shown. For best reliability run tools/fetch_client_logos.py so they are served from your own site.

## Update: new logo and clean-up
- New LIST logo (lowercase wordmark + tagline, from LIST_New_Logo.docx) traced to assets/img/list-logo.svg (+ list-logo-full.svg), used in the header, footer, background, brand section, chat button and favicon; og.jpg is regenerated with it.
- Contact: both offices (Kolhapur, Sangli) and the 0231 2669164 landline. Years shown as 'since 1997' everywhere.
- Privacy Policy and Terms now have real draft text. Have your legal adviser review them before launch.
- CSS/JS links carry a build version (?v=...) so visitors never see stale files. The Render URL sends noindex.
- .github/workflows/keepalive.yml pings /api/health every 10 minutes to reduce Render cold starts (GitHub may delay runs).
