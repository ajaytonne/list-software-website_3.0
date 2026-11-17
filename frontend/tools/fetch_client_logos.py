"""Downloads the client bank logos (and your brand logos) from the live site into assets/img/.
Needs internet. Run once:  python tools/fetch_client_logos.py   then:  python tools/build.py"""
import os, urllib.request
from clients import CLIENT_LOGOS
BASE = "https://listspl.co.in"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "img")

def get(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with open(dest, "wb") as fh:
            fh.write(urllib.request.urlopen(req, timeout=30).read())
        print("ok  ", url)
    except Exception as e:
        print("FAIL", url, e)

for _, f in CLIENT_LOGOS:
    get(f"{BASE}/img/clients/{f}", os.path.join(ROOT, "clients", f))
for f in ("logo-primary.png", "logo-secondary-white.png"):
    get(f"{BASE}/brand/{f}", os.path.join(ROOT, "brand", f))
