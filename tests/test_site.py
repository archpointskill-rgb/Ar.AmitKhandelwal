"""Site test suite. Run: python3 tests/test_site.py  (needs playwright). Serves the site locally with the same headers as vercel.json."""
import http.server,json,os,re,sys,threading,urllib.parse,html as H
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
PAGES=['index','about','projects','gallery','contact']
fails=[];passes=[0]
def ok(c,msg):
    if c: passes[0]+=1
    else: fails.append(msg); print('FAIL',msg)

# ---------- static ----------
for p in PAGES:
    h=(ROOT/f'{p}.html').read_text()
    ok('<html lang="en">' in h,f'{p}: lang attr')
    ok(re.search(r'<title>[^<]{10,}</title>',h) is not None,f'{p}: title')
    ok('name="description"' in h,f'{p}: meta description')
    ok('<script>' not in h and 'onerror=' not in h and ' onclick=' not in h,f'{p}: no inline script/handlers (CSP)')
    ids=re.findall(r'\bid="([^"]+)"',h);ok(len(ids)==len(set(ids)),f'{p}: duplicate ids {set(i for i in ids if ids.count(i)>1)}')
    for m in re.finditer(r'<img\b[^>]*>',h): ok(' alt="' in m.group(0),f'{p}: img without alt {m.group(0)[:60]}')
    for m in re.finditer(r'<a\b[^>]*target="_blank"[^>]*>',h): ok('noopener' in m.group(0),f'{p}: _blank without noopener')
    for m in re.finditer(r'(?:src|href)="([^"#?]+)"',h):
        u=m.group(1)
        if re.match(r'(https?:|mailto:|tel:|data:)',u): 
            ok(u.startswith(('https:','mailto:','tel:','data:')),f'{p}: non-https link {u}'); continue
        ok((ROOT/u).exists(),f'{p}: missing file {u}')
    for m in re.finditer(r'href="([a-z]+\.html)#([a-z]+)"',h): ok(True,'')
    ok(h.count('<h1')==1,f'{p}: exactly one h1 ({h.count("<h1")})')
    for lab in re.findall(r'<input id="(\w+)"|<select id="(\w+)"|<textarea id="(\w+)"',h):
        i=[x for x in lab if x][0];ok(f'for="{i}"' in h,f'{p}: input {i} has label')
# project data: each project once on projects page
ph=(ROOT/'projects.html').read_text()
names=re.findall(r'<div class="pm"><b>([^<]+)</b>',ph)
ok(len(names)==len(set(names)),'projects: duplicate project cards')
ok(names.count('Baxi Ji Residence')==1,'projects: Baxi appears exactly once')
ok('Featured project' not in ph,'projects: big featured block removed')
# images referenced by gallery exist as thumb + full
gh=(ROOT/'gallery.html').read_text()
for t,f in re.findall(r'src="(assets/img/t/[^"]+)" data-full="([^"]+)"',gh):
    ok((ROOT/t).exists() and (ROOT/f).exists(),f'gallery: missing {t}')
# first-person copy
for p in ['index','about','contact']:
    h=re.sub(r'<[^>]+>',' ',(ROOT/f'{p}.html').read_text())
    ok(not re.search(r'\b(his story|under his|he mentors|calls himself)\b',h,re.I),f'{p}: third-person copy remains')
ok('Wellness Design' not in (ROOT/'index.html').read_text(),'index: "Wellness Design" removed')
ok('Real Estate</h3>' in (ROOT/'index.html').read_text(),'index: Real Estate service present')
ok('Four ways' in (ROOT/'index.html').read_text(),'index: Four ways heading')
# asset weights
big=[(f,f.stat().st_size) for f in (ROOT/'assets').rglob('*') if f.is_file() and f.stat().st_size>400_000 and 'showreel.mp4' not in f.name]
ok(not big,f'oversized assets {big}')
# repo secrets
for f in ROOT.rglob('*'):
    if f.is_file() and f.suffix in('.html','.js','.css','.json','.py','.txt') and 'tests' not in f.parts:
        t=f.read_text(errors='ignore')
        ok(not re.search(r'(api[_-]?key|secret|password|token)\s*[:=]\s*["\'][A-Za-z0-9_\-]{12,}',t,re.I),f'secret-like string in {f.name}')
        ok('eval(' not in t and 'document.write(' not in t and not re.search(r'innerHTML\s*=[^;]*(dataset|\.value|location|hash)',t),f'unsafe sink in {f.name}')

# ---------- server with real headers ----------
HD=json.load(open(ROOT/'vercel.json'))['headers'][0]['headers']
class R(http.server.SimpleHTTPRequestHandler):
    def __init__(s,*a,**k): super().__init__(*a,directory=str(ROOT),**k)
    def end_headers(s):
        for h in HD: s.send_header(h['key'],h['value'])
        super().end_headers()
    def log_message(*a): pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',8199),R);threading.Thread(target=srv.serve_forever,daemon=True).start()
B='http://127.0.0.1:8199/'

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    br=p.chromium.launch()
    for name,vp in [('desktop',{'width':1360,'height':860}),('tablet',{'width':820,'height':1100}),('mobile',{'width':390,'height':844})]:
        ctx=br.new_context(viewport=vp);pg=ctx.new_page();errs=[];csp=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.on('console',lambda m:(csp.append(m.text) if 'Content Security Policy' in m.text and 'fonts.' not in m.text else None))
        pg.route(re.compile(r'https://fonts\.(googleapis|gstatic)\.com/.*'),lambda r:r.fulfill(status=200,body='',content_type='text/css'))
        for pn in PAGES:
            pg.goto(f'{B}{pn}.html');pg.wait_for_timeout(500)
            ok(pg.evaluate("document.documentElement.scrollWidth-innerWidth")<=0,f'{name} {pn}: horizontal overflow')
            ok(pg.evaluate("[...document.images].filter(i=>i.complete&&i.src&&i.naturalWidth==0).length")==0,f'{name} {pn}: broken images')
        ok(not errs,f'{name}: JS errors {errs}');ok(not csp,f'{name}: CSP violations {csp}')
        if vp['width']<=900:
            pg.goto(B+'index.html');pg.click('.burger');ok(pg.evaluate("document.querySelector('nav.menu').offsetHeight>0"),'mobile: menu opens')
        else:
            pg.goto(B+'index.html');pg.wait_for_timeout(300)
            pg.click('nav.menu a.btn');pg.wait_for_url('**/contact.html');ok(True,'')
        # booking form
        pg.goto(B+'contact.html');pg.wait_for_timeout(300)
        pg.click('#bf button[type=submit]');ok(pg.evaluate("document.querySelector('#e_nm').textContent.length>0 && document.querySelector('#e_mb').textContent.length>0"),f'{name}: empty form shows errors')
        ok(pg.evaluate("getComputedStyle(document.querySelector('#ok')).display")=='none',f'{name}: no WhatsApp on invalid form')
        pg.fill('#nm','A');pg.fill('#mb','12ab');pg.select_option('#pu',index=1);pg.fill('#dt','2030-01-01');pg.click('#bf button[type=submit]')
        ok(pg.evaluate("document.querySelector('#e_mb').textContent.length>0"),f'{name}: invalid mobile rejected')
        evil='<img src=x onerror=alert(1)>&"\''
        pg.fill('#nm',evil+' Test');pg.fill('#mb','+91 98765 43210');pg.fill('#ms','Line1\nLine2 & more #hash');
        pg.wait_for_timeout(200)
        ok(pg.evaluate("document.querySelector('#pv img')")is None,f'{name}: preview is XSS-safe')
        with ctx.expect_page() as np: pg.click('#bf button[type=submit]')
        url=np.value.url if False else None
        href=pg.evaluate("document.querySelector('#okLink').href")
        u=urllib.parse.urlparse(href);q=urllib.parse.parse_qs(u.query)
        ok(u.scheme=='https' and u.netloc=='wa.me' and u.path=='/919982507555',f'{name}: WhatsApp target {href[:60]}')
        txt=q.get('text',[''])[0]
        ok('Name: '+evil in txt and 'Line2 & more #hash' in txt and 'Mobile: +91 98765 43210' in txt,f'{name}: message encoded correctly')
        # gallery
        pg.goto(B+'gallery.html');pg.wait_for_timeout(400)
        total=pg.evaluate("document.querySelectorAll('.gi').length");ok(total>=70,f'{name}: gallery has {total} items')
        ok(pg.evaluate("[...document.querySelectorAll('.gi')].every(g=>g.querySelector('figcaption b').textContent.trim().length>2)"),f'{name}: every image captioned')
        pg.click('.filters button[data-f=hospitality]');pg.wait_for_timeout(300)
        vis=pg.evaluate("[...document.querySelectorAll('.gi')].filter(g=>!g.classList.contains('hide')).length");ok(0<vis<total,f'{name}: filter works ({vis})')
        pg.click('.filters button[data-f=all]');pg.wait_for_timeout(200)
        pg.evaluate("document.querySelectorAll('.gi .ph')[3].click()");pg.wait_for_timeout(300)
        ok(pg.evaluate("document.querySelector('.lb').classList.contains('open')")and'/t/' not in pg.evaluate("document.querySelector('.lb img').src"),f'{name}: lightbox opens full image')
        pg.keyboard.press('Escape');pg.wait_for_timeout(200)
        ok(not pg.evaluate("document.querySelector('.lb').classList.contains('open')"),f'{name}: lightbox closes with Esc')
        pg2=ctx.new_page();pg2.goto(B+'gallery.html#civic');pg2.wait_for_timeout(500)
        ok(pg2.evaluate("[...document.querySelectorAll('.gi')].filter(g=>!g.classList.contains('hide')).every(g=>g.dataset.c.includes('civic'))"),f'{name}: #civic deep link filters');pg2.close()
        # reel lazy
        pg.goto(B+'index.html');pg.wait_for_timeout(300)
        ok(pg.evaluate("document.querySelector('#reel video')")is None,f'{name}: video not loaded until play')
        pg.locator('#reel .rp').scroll_into_view_if_needed();pg.click('#reel .rp');pg.wait_for_timeout(800)
        ok(pg.evaluate("!!document.querySelector('#reel video')"),f'{name}: showreel plays on click')
        ctx.close()
    br.close()
srv.shutdown()
print(f'\n{passes[0]} checks passed, {len(fails)} failed');sys.exit(1 if fails else 0)
