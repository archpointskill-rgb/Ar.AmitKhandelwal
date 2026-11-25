import os
LOGO='assets/img/logo-apcl.png'
PLOGO='assets/img/logo-primary.png'
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
WAI='<svg viewBox="0 0 32 32"><path d="M16 3C9 3 3.3 8.6 3.3 15.5c0 2.3.6 4.4 1.7 6.3L3 29l7.4-1.9a12.8 12.8 0 0 0 5.6 1.3c7 0 12.7-5.6 12.7-12.5S23 3 16 3zm0 22.9c-1.8 0-3.6-.5-5.100-1.400l-.4-.2-4.400 1.100 1.200-4.200-.3-.4a10.200 10.200 0 0 1-1.600-5.500C5.400 9.800 10.100 5.200 16 5.200S26.600 9.800 26.600 15.500 21.900 25.900 16 25.900zm5.800-7.600c-.3-.2-1.900-.9-2.200-1-.3-.1-.5-.2-.7.200s-.8 1-1 1.200c-.2.200-.4.200-.7.100a8.400 8.400 0 0 1-4.200-3.700c-.3-.6.300-.5.900-1.700.1-.2 0-.4 0-.5l-1-2.300c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.100-.8.400-.3.300-1.100 1.100-1.100 2.600s1.100 3 1.300 3.200c.2.200 2.200 3.400 5.400 4.700 2 .8 2.800.9 3.800.7.600-.1 1.900-.8 2.200-1.500.3-.7.300-1.400.2-1.500-.1-.2-.3-.2-.6-.4z"/></svg>'
PAGES=[('index.html','Home'),('about.html','About'),('projects.html','Projects'),('gallery.html','Gallery'),('contact.html','Contact')]
def nav(cur):
    links=''.join(f'<a href="{h}"{" class=on" if h==cur else ""}>{t}</a>' for h,t in PAGES[:-1])
    return f'''<header class="nav"><div class="wrap"><a class="brand" href="index.html"><span class="bn">Ar. Amit <i>Khandelwal</i></span></a>
<button class="burger" aria-label="Menu"><i></i><i></i></button><nav class="menu">{links}<a class="btn" href="contact.html">Book appointment</a></nav></div></header>'''
FOOT=f'''<div class="wmw"><div class="wm"><span>Design is our love</span><span>Design is our love</span><span>Design is our love</span><span>Design is our love</span></div></div><footer><div class="wrap"><div><img class="plogo" src="assets/img/logo-primary-light.png" alt="Arch Point Consultants Pvt. Ltd."><p>Your dream is our mission, accuracy is our goal, perfection is our attitude, achievement is our habit, &amp; design is our love.</p></div>
<div><h4>Explore</h4><a href="index.html">Home</a><a href="about.html">About</a><a href="projects.html">Projects</a><a href="gallery.html">Gallery</a><a href="contact.html">Book an appointment</a></div>
<div><h4>Connect</h4><a href="mailto:connect@archpointgp.com">connect@archpointgp.com</a><a href="tel:+919982507555">+91 99825 07555</a><a href="https://instagram.com/archpoint_architecture" target="_blank" rel="noopener">@archpoint_architecture</a><a href="https://archpoint.in" target="_blank" rel="noopener">archpoint.in</a><a href="https://www.linkedin.com/company/14409093" target="_blank" rel="noopener">LinkedIn</a><a href="https://www.facebook.com/teamarchpoint/" target="_blank" rel="noopener">Facebook</a><a>Plot No. 92/64, Patel Marg, Sector 9, Mansarovar, Jaipur</a></div>
<div class="cp"><span>&copy; 2026 Arch Point Group</span><span>Designed with love in Jaipur</span></div></div></footer>
<a class="fab" href="contact.html" aria-label="Book on WhatsApp">{WAI}</a>'''
import hashlib
def _v(f): return hashlib.md5(open('/home/claude/amit-site/'+f,'rb').read()).hexdigest()[:8]
def page(fn,title,desc,body,extra=''):
    html=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{desc}"><meta name="color-scheme" content="light">{FONTS}<link rel="icon" href="{LOGO}"><link rel="stylesheet" href="css/site.css?v={_v("css/site.css")}"></head><body>{nav(fn)}<main>{body}</main>{FOOT}{extra}<script src="js/site.js?v={_v("js/site.js")}"></script></body></html>'''
    open(fn,'w').write(html)
import re as _re
def ico(n):
    t=open('/home/claude/amit-site/src_icons/'+n+'.svg').read()
    t=_re.sub(r'<!--.*?-->','',t,flags=_re.S).replace('width="24"','width="22"').replace('height="24"','height="22"').replace('class="lucide lucide-'+n+'"','class="ic" aria-hidden="true"')
    return t.strip()
ARR='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
# gallery data: (cat, project, place/type, [(file,label)])
PR=[
('residential','Baxi Niwas','Residence · Architecture, PMC & Interiors',[('baxi-exterior','Exterior'),('baxi-living','Living room'),('baxi-dining','Dining'),('baxi-foyer','Foyer'),('baxi-bedroom','Master bedroom')]),
('residential','Rakesh Ji Residence','Residence',[('rakesh-exterior','Exterior'),('rakesh-interior','Interiors')]),
('residential','Sangeeta Ji Residence, Ajmer','Residence · 2025',[('sangeeta-exterior','Exterior'),('sangeeta-living','Living'),('sangeeta-lounge','Lounge'),('sangeeta-bedroom','Bedroom')]),
('residential','Godara Ji Residence','Residence · 2025',[('godhara-exterior','Exterior'),('godara-bedroom','Bedroom'),('godara-stair','Staircase'),('godara-dining','Dining'),('godara-pooja','Pooja room'),('godhara-hall','Hall'),('godhara-tv','Living')]),
('residential','Bhagwati Ji Residence, Ajmer','Residence',[('bhagwati-front','Front'),('bhagwati-gate','Entrance'),('bhagwati-exterior','Exterior'),('bhagwati-hall','Hall'),('bhagwati-living','Living'),('bhagwati-first-floor','First-floor living'),('bhagwati-bedroom','Bedroom'),('bhagwati-suite','Master suite'),('bhagwati-kids','Kids room')]),
('residential','Bhagwati Ji Out House','Out house',[('bhagwati-outhouse','Exterior')]),
('residential','Kapil Ji Out House','Out house',[('kapil-exterior','Exterior'),('kapil-living','Living')]),
('residential','Kailash Ji Residence','Residence · PMC',[('kailash-exterior','Exterior'),('kailash-bedroom','Bedroom')]),
('residential','Vikas Jain Ji Residence','Residence · PMC',[('vikas-exterior','Exterior')]),
('residential','High-end Residence','Residence · PMC',[('pmc-exterior','Exterior'),('pmc-living','Living'),('pmc-foyer','Foyer')]),
('residential','Jayesh Ji Residence, Dubai','Architecture, PMC & Interiors',[('jayesh-dining','Dining'),('jayesh-living','Living')]),
('residential','BnB, Siddharth Nagar, Jaipur','Hospitality residence',[('airbnb-siddharth','Exterior'),('bnb-living','Living'),('bnb-dining','Dining'),('bnb-bath','Bathroom')]),
('commercial','YY London','Commercial tower',[('yy-london','Exterior')]),
('commercial','Fair Field','Mixed use',[('fairfield','Exterior')]),
('commercial','72 Parksyde','High-rise',[('parksyde','Exterior')]),
('commercial','GSFC Office, Jaipur','Office interiors',[('gsfc-office','Workspace')]),
('commercial',"Goyal's Jewellery Showroom, Jaipur",'Showroom',[('goyal-exterior','Exterior'),('goyal-interior','Showroom interior')]),
('commercial','Deepak Ji Coworking','Commercial',[('coworking-facade','Facade')]),
('commercial','Hem Securities Office','Office tower',[('hem-office','Exterior')]),
('commercial','Hem Securities Residence','Residence',[('hem-residence','Interior in progress')]),
('commercial','Agrasen Industries, Mahindra SEZ','Industrial · 7.5 acres',[('agrasen-exterior','Plant'),('agrasen-interior','Interior')]),
('hospitality','Grassfield Resorts, Delhi Road','Resort',[('grassfield-clubhouse','Clubhouse'),('grassfield-cottages','Cottages'),('grassfield-landscape-night','Landscape by night'),('grassfield-pool-night','Pool by night'),('grassfield-banquet-hall','Banquet'),('grassfield-room-dome','Dome suite'),('grassfield-room-bath','Suite with bath'),('grassfield-pool','Pool'),('grassfield-aerial','Aerial'),('grassfield-suite','Suite')]),
('hospitality','Pushkar Resort','Resort',[('pushkar-cottages','Cottages'),('pushkar-main','Main block'),('pushkar-club','Clubhouse')]),
('hospitality','Aamrai Mango Resort','Resort · with Pentaspace',[('aamrai-garden','Garden'),('aamrai-dining','Dining'),('aamrai-suite','Suite')]),
('hospitality','Zion Club','Club · with CAID',[('zion-1','Entrance'),('zion-2','Lounge'),('zion-3','Lobby'),('zion-5','Restaurant'),('zion-6','Banquet'),('zion-4','Gym'),('zion-7','Badminton'),('zion-8','Cricket net')]),
('hospitality','Hotel Kapish','Hotel',[('kapish-exterior','Exterior'),('kapish-lobby','Lobby')]),
('hospitality','Hotel Regenta (Royal Orchid), Khatu','Hotel',[('regenta-exterior','Exterior'),('regenta-facade','Front facade'),('regenta-courtyard','Courtyard & pool'),('regenta-dining','Dining'),('regenta-pool','Pool')]),
('civic','Todarmal Smarak','Civic landmark',[('todarmal-facade','Front porch'),('todarmal-render','Exterior'),('todarmal-pavilion','Pavilion'),('todarmal-pavilion-crowd','Ceremony'),('todarmal-night','By night'),('todarmal-front','Front view'),('todarmal-temple','Temple'),('todarmal-hall','Sanctum')]),
('civic','Dhai Dweep, Indore','Religious',[('dhai-aerial','Front & gateway'),('dhai-dweep','Exterior'),('dhai-dome-night','Dome by night'),('dhai-model-hall','Model hall'),('dhai-card-render','Hall render'),('dhai-model-tower','Model towers')]),
('civic','Jain Temple, Kota','Religious',[('jain-temple','Exterior')]),
('civic','Jain Sant Bhawan','Religious',[('sant-bhawan','Exterior')]),
('institutional','Bhagwant University, Pali','Auditorium & campus',[('bhagwant-univ','Entrance'),('bhagwant-auditorium','Auditorium')]),
('institutional','CLC Institute','Institutional',[('clc-institute','Exterior')]),
('institutional','Global School, Hyderabad','43,934 sq ft',[('global-school','Campus')]),
('healthcare','Amar Jain Hospital, Jaipur','Architecture, interiors & PMC',[('amarjain-front-day','Front'),('amarjain-front','Front at dusk'),('amarjain-aerial','Aerial'),('amarjain-render','Design render'),('amarjain-reception','Reception'),('amarjain-helpdesk','Help desk'),('amarjain-icu-ward','Ward')]),
]
CATN={'residential':'Residential','commercial':'Commercial & Industrial','hospitality':'Hospitality','civic':'Religious & Civic','institutional':'Institutional','healthcare':'Healthcare'}
import html as H
from PIL import Image as _I
SIG=[('baxi','Baxi Niwas','Baxi Niwas','Residence'),('grassfield','Grassfield Resorts','Grassfield','Delhi Road · Resort'),('regenta','Hotel Regenta','Hotel Regenta','Khatu · Hotel'),('dhai','Dhai Dweep','Dhai Dweep','Indore · Religious'),('todarmal','Todarmal Smarak','Todarmal','Civic landmark'),('bhagwati','Bhagwati Ji Residence','Bhagwati Ji Residence','Ajmer · Residence'),('zion','Zion Club','Zion Club','Club · CAID'),('amarjain','Amar Jain Hospital','Amar Jain Hospital','Jaipur · Healthcare'),('bnb','BnB','BnB','Siddharth Nagar, Jaipur')]
def sigp(key): return [x for x in PR if x[1].startswith(key)][0]
def imgs_attr(im):
    for f,l in im: assert ',' not in l and '|' not in l
    return ','.join(f'{f}|{l}' for f,l in im)
def vcard(i,name,sub,key,gal=True,feat=False):
    c,n,k,im=sigp(key)
    n_=len(im); cnt=f'{n_} {"photo" if n_==1 else "photos"}'
    href=f'#{i}' if gal else f'gallery.html#{i}'
    da=f' data-t="{H.escape(name)}" data-imgs="{imgs_attr(im)}"' if gal else ''
    d='' if feat else 't/'
    cl='vc vfeat rv' if feat else 'vc rv'
    return f'<a class="{cl}" id="{i}" href="{href}"{da}><span class="ph"><img src="assets/img/{d}{im[0][0]}.jpg" alt="{H.escape(name)}" loading="lazy" decoding="async"><em>{cnt}</em></span><span class="vm"><b>{name}</b><small>{sub}</small></span></a>'.replace(f' id="{i}"',f' id="{i}"' if gal else '')
AREAS='ABCDEFGHI'
def mtile(j,i,name,sub,key):
    c,n,k,im=sigp(key); n_=len(im); cnt=f'{n_} photos'
    big=j in (0,1,7,8)
    d='' if big else 't/'
    return f'<a class="vc mt rv d{j%4}" id="{i}" href="#{i}" style="grid-area:{AREAS[j]};--k:{j}" data-t="{H.escape(name)}" data-imgs="{imgs_attr(im)}"><img src="assets/img/{d}{im[0][0]}.jpg" alt="{H.escape(name)}" loading="lazy" decoding="async"><em>{cnt}</em><span class="vm"><b>{name}</b><small>{sub}</small></span></a>'
def slides(lst,hq=False):
    o=''
    for f,t,k in lst:
        w,h=_I.open(f'/home/claude/amit-site/assets/img/{f}.jpg').size
        r=max(.7,min(1.6,w/h))
        o+=f'<figure class="cs" style="--r:{r:.3f}" data-t="{H.escape(t)}" data-k="{H.escape(k)}" tabindex="0"><img src="assets/img/{"" if hq else "t/"}{f}.jpg" data-full="assets/img/{f}.jpg" alt="{H.escape(t)}" loading="lazy" decoding="async"><figcaption><b>{H.escape(t)}</b><span>{H.escape(k)}</span></figcaption></figure>'
    return o
def car(lst,hq=False):
    return f'<div class="car"><div class="strip">{slides(lst,hq)}</div><button class="cb cp" type="button" aria-label="Previous">&lsaquo;</button><button class="cb cn" type="button" aria-label="Next">&rsaquo;</button></div>'
def gi(f,t,k,c,x=''):
    return f'<figure class="gi rv{x}" data-c="{c}" data-t="{t}" data-k="{k}"><div class="ph"><img src="assets/img/t/{f}.jpg" data-full="assets/img/{f}.jpg" alt="{t}" loading="lazy" decoding="async"></div><figcaption><b>{t}</b><span>{k}</span></figcaption></figure>'
def cards(cat):
    o=''
    for c,n,k,im in PR:
        if c!=cat: continue
        o+=f'<a class="pk rv" href="#" data-t="{H.escape(n)}" data-imgs="{imgs_attr(im)}"><div class="ph"><img src="assets/img/t/{im[0][0]}.jpg" alt="{H.escape(n)}" loading="lazy" decoding="async"><em>{len(im)} {"photo" if len(im)==1 else "photos"}</em></div><div class="pm"><b>{n}</b><span>{k}</span></div></a>'
    return o
CTA='''<section><div class="wrap"><div class="ctab rv"><h2>Let's build something <mark class="hl full" style="color:#0C1B33">worth keeping</mark>.</h2><p>Share your plot, your idea or your questions. Book a conversation with me in under a minute.</p><a class="btn" href="contact.html">Book appointment on WhatsApp '''+ARR+'''</a><p class="soc"><a href="https://archpoint.in" target="_blank" rel="noopener">archpoint.in</a><span>&middot;</span><a href="https://instagram.com/archpoint_architecture" target="_blank" rel="noopener">@archpoint_architecture</a></p></div></div></section>'''
TEST=[('Parth Saini', 'Home Owner', '4.9', 'One of the best architects in Jaipur! Excellent services, professional approach, and very friendly nature. The house plan and commercials were explained in detail, which made everything clear and smooth.', 'Residential project, Mansarovar'), ('SP Bharill', 'Hospital Administrator', '4.8', 'Arch Point Consultants has done an excellent job in completing the Amar Jain Hospital project with architectural, interior, and PMC services, ensuring everything was delivered with precision and professionalism.', 'Amar Jain Hospital, Jaipur'), ('Riddhi Kapoor', 'Client', '4.7', 'The team was an absolute delight to work with! Their professionalism, creativity, and collaborative approach made the entire experience seamless.', 'Design consultation, Jaipur'), ('Gopal Sharma', 'Flat Owner', '4.9', 'Completed the interiors of our Seven Heaven flat so beautifully. The design, finishing, and attention to detail have truly exceeded our expectations.', 'Seven Heaven Flats, Mansarovar'), ('Anurag Aman', 'Client', '4.6', 'An amazing choice for your dream construction. A hardworking team which delivers on time and has an aesthetic sense to design your building.', 'Residence interior, Jaipur'), ('Vivek Kalra', 'Home Owner', '4.8', 'Right from the first discussion till the final handover, the team was approachable and clear in their process. They balanced creativity with practicality.', 'Residential design, Jaipur'), ('Hetansh Sheth', 'Client', '4.7', "Professional approach and creative solutions, listens to the client's demands and gives an appropriate design.", 'Design consultation, Jaipur')]
def tcards(items):
    return ''.join(f'<article class="tc rv"><div class="st">&#9733; {r}</div><p>&ldquo;{q}&rdquo;</p><b>{n}</b><span>{role} &middot; {pj}</span></article>' for n,role,r,q,pj in items)
def tc3(names):
    o=''
    for n,role,r,q,pj in TEST:
        if n in names:
            ini=''.join(w[0] for w in n.split()[:2])
            o+=f'<article class="tc3 rv"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>&ldquo;{q}&rdquo;</p><div class="who"><i>{ini}</i><div><b>{n}</b><span>{role} &middot; {pj}</span></div></div></article>'
    return o
AWA=[('ach-iibl-trophy','IIBL Award 2024'),('ach-national-icon-trophy','National Icon Award 2025'),('ach-asia-leadership-trophy',"Asia's Leadership Awards"),('award-2025','Excellence Awards 2025'),('ach-womens-day-stage',"Women's Day felicitation")]
AWB=[('ach-iibl-certificate','Most Admired Architecture Company'),('ach-pride-of-rajasthan','Pride of Rajasthan'),('ach-asia-leadership-certificate',"3rd Asia's Leadership Awards"),('ach-national-icon-certificate','National Icon Awards 2025')]
def awcol(lst,cls=''):
    one=lambda hid:''.join(f'<a href="gallery.html#achievements"{" aria-hidden=\"true\" tabindex=\"-1\"" if hid else ""}><img src="assets/img/t/{f}.jpg" alt="{"" if hid else H.escape(t)}" loading="lazy" decoding="async"><b>{H.escape(t)}</b></a>' for f,t in lst)
    return f'<div class="vcol{cls}">{one(False)}{one(True)}</div>'
HIGH=[('baxi-exterior','Baxi Niwas','Residence'),('grassfield-clubhouse','Grassfield Resorts','Delhi Road'),('regenta-exterior','Hotel Regenta','Khatu'),('dhai-aerial','Dhai Dweep','Indore')]
AWALL=AWA+AWB
def awrow(hid):
    return ''.join(f'<a href="gallery.html#achievements"{" aria-hidden=\"true\" tabindex=\"-1\"" if hid else ""}><img src="assets/img/t/{f}.jpg" alt="{"" if hid else H.escape(t)}" loading="lazy" decoding="async"></a>' for f,t in AWALL)
LB='<div class="lb"><button class="x" aria-label="Close">&times;</button><button class="pv" aria-label="Previous">&lsaquo;</button><img alt=""><p></p><button class="nx" aria-label="Next">&rsaquo;</button></div>'
# ---------- HOME
home=f'''<section class="hero"><div class="vside" aria-hidden="true">Architecture &middot; Interiors &middot; PMC &middot; Real Estate</div><div class="wrap"><div>
<img class="plogo hl1" src="{PLOGO}" alt="Arch Point Consultants Pvt. Ltd. - Your dream is our mission">
<div class="eyebrow">Founder &amp; CMD &middot; Arch Point Group</div>
<h1><span data-letters>Ar. Amit</span><span class="n2" data-letters>Khandelwal</span></h1>
<p class="role">ARCHITECT <span>|</span> ENTREPRENEUR <span>|</span> AUTHOR</p>
<p class="tagline">Where <mark class="hl">design</mark> meets <mark class="hl b">purpose</mark>.</p>
<div class="cta"><a class="btn" href="contact.html">Book appointment {ARR}</a><a class="btn ghost" href="projects.html">View projects</a></div><div class="hstats rv"><div><b data-n="27">0</b><small>Years of experience</small></div><div><b data-n="500">0</b><small>Projects delivered</small></div><div><b data-n="100">0</b><small>Team members</small></div></div><ul class="trust"><li>ISO recognised</li><li>Startup India</li><li>Vastu &amp; energy aligned</li></ul></div>
<div class="portrait"><div class="arch"><div class="mono">AK</div><img src="assets/amit-2026.jpg" alt="Ar. Amit Khandelwal" fetchpriority="high" decoding="async"></div>
<a class="glass" href="contact.html"><small>Available for projects</small><b>Let's design something worth keeping</b><p>Share a few details, and I'll get back to you with a clear direction.</p><span class="go">{ARR}</span></a></div></div><div class="blob b1"></div><div class="blob b2"></div><svg class="orbit" viewBox="0 0 200 200"><circle cx="100" cy="100" r="96"/><circle cx="100" cy="100" r="70"/></svg><div id="elev"></div></section>
<div class="ticker"><div><span>Architecture</span><span>Interior Design</span><span>Project Management</span><span>Real Estate</span><span>Wellness</span><span>Technology</span><span>Architecture</span><span>Interior Design</span><span>Project Management</span><span>Real Estate</span><span>Wellness</span><span>Technology</span></div></div>
<section class="hlsec"><div class="wrap"><div class="eyebrow">Arch Point portfolio</div><h2 class="rv">Highlighted <mark class="hl">Projects</mark> of Arch Point</h2><div style="height:22px"></div>{car(HIGH,True)}<div style="text-align:center;margin-top:30px"><a class="btn" href="projects.html">All projects {ARR}</a> <a class="btn ghost" href="gallery.html">Open gallery</a></div></div></section>
<section class="story"><div class="wrap"><div class="eyebrow">Our story</div><h2 class="rv">A <mark class="hl o">family of 100+</mark>, one belief</h2><p class="lead" style="max-width:62ch;margin-top:14px">Accuracy in the plan and perfection in the detail guide everything we do at Arch Point. Today a family of 100+ professionals shares that belief and brings it to every project with care.</p>
<div class="bn numbers"><div class="d" style="grid-area:a"><b data-n="27">0</b>{ico('calendar-check')}<small>Years of experience</small></div>
<div class="p" style="grid-area:b"><img src="assets/img/team.jpg" alt="The Arch Point team" loading="lazy" decoding="async"><span>The Arch Point family</span></div>
<div class="p" style="grid-area:c"><img src="assets/img/t/grassfield-cottages.jpg" alt="Grassfield Resorts" loading="lazy" decoding="async"></div>
<div class="d y" style="grid-area:d"><b data-n="500">0</b>{ico('building-2')}<small>Projects delivered</small></div>
<div class="d" style="grid-area:e"><b data-n="10">0</b>{ico('globe')}<small>Locations across the globe</small></div>
<div class="p" style="grid-area:f"><img src="assets/img/t/zion-1.jpg" alt="Zion Club" loading="lazy" decoding="async"></div>
<div class="d b" style="grid-area:g"><b data-n="100">0</b>{ico('users')}<small>Team members</small></div></div></div></section>
<section style="padding-top:20px"><div class="wrap split"><div class="imgrv rv" style="aspect-ratio:4/5"><img src="assets/img/sangeeta-exterior.jpg" alt="Sangeeta Ji Residence, Ajmer" loading="lazy" decoding="async"></div>
<div class="rv d1"><div class="eyebrow">The philosophy</div><p class="bigq">Buildings should do more than <mark class="hl">stand</mark>. They should hold <mark class="hl b">families</mark>, <mark class="hl o">businesses</mark> and futures.</p><div style="height:22px"></div><a class="btn ghost" href="about.html">The Arch Point story {ARR}</a></div></div></section>
<section class="awsec"><div class="wrap"><div class="eyebrow">Awards &amp; recognition</div></div><div class="hmar rv" aria-label="Awards and achievements"><div class="hrow">{awrow(False)}{awrow(True)}</div></div></section>
<section><div class="wrap"><div class="eyebrow">Showreel</div><h2 class="rv">Our work, <mark class="hl o">in motion</mark></h2><div class="reel rv" id="reel"><img src="assets/showreel-poster.jpg" alt="Arch Point showreel: architecture, interiors and PMC" loading="lazy" decoding="async"><button class="rp" type="button" aria-label="Play showreel"><svg width="34" height="34" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button></div></div></section>
<section><div class="wrap"><div class="eyebrow">What we offer</div><h2 class="rv">Four ways we <mark class="hl">build</mark> with you</h2><div class="svc">
<a class="rv" href="projects.html"><i>{ico('building-2')}</i><div><h3>Architectural Design</h3><p>Innovative, sustainable design shaped around your vision.</p></div><span class="go">{ARR}</span></a>
<a class="rv d1" href="projects.html"><i>{ico('armchair')}</i><div><h3>Interior Design</h3><p>Refined, functional interiors that reflect your personality and purpose.</p></div><span class="go">{ARR}</span></a>
<a class="rv d2" href="projects.html"><i>{ico('clipboard-check')}</i><div><h3>Project Management Consultancy</h3><p>Closely managed planning, coordination and execution for timely, cost-effective delivery.</p></div><span class="go">{ARR}</span></a>
<a class="rv d3" href="contact.html"><i>{ico('landmark')}</i><div><h3>Real Estate</h3><p>Site feasibility, investment guidance and development support for plots and projects.</p></div><span class="go">{ARR}</span></a></div></div></section>
<section class="tsec"><div class="wrap"><div class="tmrow" aria-hidden="true"><img class="tm t0" style="--h:150px;--d:0" src="assets/img/t/baxi-exterior.jpg" alt="" loading="lazy" decoding="async"><img class="tm t1" style="--h:110px;--d:1" src="assets/img/t/grassfield-clubhouse.jpg" alt="" loading="lazy" decoding="async"><img class="tm t2" style="--h:210px;--d:2" src="assets/img/t/regenta-exterior.jpg" alt="" loading="lazy" decoding="async"><img class="tm t3" style="--h:170px;--d:3" src="assets/img/t/dhai-aerial.jpg" alt="" loading="lazy" decoding="async"><img class="tm t4" style="--h:230px;--d:4" src="assets/img/t/todarmal-facade.jpg" alt="" loading="lazy" decoding="async"><img class="tm t5" style="--h:180px;--d:5" src="assets/img/t/zion-1.jpg" alt="" loading="lazy" decoding="async"><img class="tm t6" style="--h:120px;--d:6" src="assets/img/t/bhagwati-front.jpg" alt="" loading="lazy" decoding="async"><img class="tm t7" style="--h:200px;--d:7" src="assets/img/t/amarjain-front-day.jpg" alt="" loading="lazy" decoding="async"><img class="tm t8" style="--h:150px;--d:8" src="assets/img/t/grassfield-room-dome.jpg" alt="" loading="lazy" decoding="async"></div><div class="tcen"><span class="pill2">Testimonials</span><h2 class="rv">Trusted by families <span>and businesses</span></h2></div><div class="tg">{tc3(['Parth Saini','Gopal Sharma','Vivek Kalra'])}</div></div></section>
<section><div class="wrap"><div class="quote rv"><blockquote>Your dream is our <mark class="hl">mission</mark>, accuracy is our goal, <mark class="hl">perfection</mark> is our attitude.</blockquote><cite>The Arch Point creed</cite></div></div></section>
{CTA}'''
page('index.html','Ar. Amit Khandelwal | Founder & CMD, Arch Point Group','Portfolio of Ar. Amit Khandelwal, Founder & CMD of Arch Point Group, Jaipur. Architecture, interiors, PMC, real estate and wellness.',home,LB)
# ---------- ABOUT
tl=[('The beginning','Home Aura Arch Point','We began with a small studio, a paper attendance register and one clear promise: design quality that clients can feel.'),
('2010','Arch Point Consultants Pvt. Ltd. incorporated','Our founding practice took shape, bringing architecture, interior design and project management consultancy under one roof.'),
('Growth years','500+ projects, 100+ team','Our studio grew to 100+ professionals, supported by HRMS software that keeps every project well coordinated.'),
('Expansion','Wellness &amp; Technology','Arch Point Wellness (EKASA) and Arch Point Technology widened our reach into wellbeing, software and AI.'),
('Today','Architect, Entrepreneur &amp; Author','I lead Arch Point Group across design, real estate and wellness, and I enjoy sharing the journey through speaking, writing and collaboration.')]
STEPS=[('Research & Analysis','In-depth research into your needs and the site conditions.'),('Conceptual Design','Innovative ideas, developed with a scientific and artistic approach.'),('Design Development','Detailed planning that respects social, economic and cultural considerations.'),('Project Execution','High-quality design and Vastu solutions, executed with care.'),('Client Satisfaction','A clear presentation, so that you can see your dream as it will be built.')]
VALS=[('A','uthentic'),('R','esponsible'),('C','onfident'),('H','onest'),('P','assionate'),('O','ptimistic'),('I','mpressive'),('N','oble'),('T','rustworthy')]
SECT=['Residential','Commercial','Resorts & Hotels','Auditoriums','Sports Complexes','Townships','Religious Projects','Hospitals','Institutional','Interiors & PMC']
about=f'''<section class="pagehead"><div class="wrap"><div class="eyebrow">About</div><h1>Architecture led by <mark class="hl">purpose</mark>,<br>built on <mark class="hl b">trust</mark>.</h1><p class="lead">I am Ar. Amit Khandelwal, Founder &amp; CMD of Arch Point Group. Over 27 years, I have grown the group from a focused design practice into a multi-disciplinary organisation spanning architecture, interior design, project management consultancy, real estate, wellness and technology. Today a team of 100+ professionals has delivered 500+ projects across 10+ locations, each shaped by the same commitment to accuracy, craft and long-term value.</p></div></section>
<section style="padding-top:0"><div class="wrap split abt"><div class="portrait" style="margin:0"><div class="arch"><div class="mono">AK</div><img src="assets/amit-2026.jpg" alt="Ar. Amit Khandelwal"></div></div>
<div class="rv"><p class="bigq">The relationship between <mark class="hl">vertical energy</mark> and the built form decides how a space feels, performs and lasts.</p><p class="lead" style="margin-top:20px">At Arch Point, I design for that relationship, bringing science, Vastu and energy alignment together with design innovation. We have grown from two people to a team of 100+ and delivered 500+ projects across the residential, commercial, hospitality, institutional and civic sectors. As an architect, entrepreneur and author, my goal is value-driven, future-ready design for every client.</p></div></div></section>
<section style="background:#fff;border-block:1px solid var(--line)"><div class="wrap"><div class="eyebrow">The journey</div><h2 class="rv" style="margin-bottom:50px">From a paper register to a <mark class="hl o">100+ strong</mark> studio</h2><div class="tlw"><div class="tl"><div class="fill"></div>{''.join(f'<article class="rv"><div class="yr">{a}</div><h3>{b}</h3><p>{c}</p></article>' for a,b,c in tl)}</div><aside class="side rv"><svg class="conc" viewBox="0 0 200 200"><circle cx="100" cy="100" r="40"/><circle cx="100" cy="100" r="70"/><circle cx="100" cy="100" r="98"/></svg><div class="eyebrow" style="color:var(--yellow)">Vertical energy</div><p class="bigq">Where science, Vastu and energy alignment meet design.</p><ul><li>Science and technical mastery</li><li>Vastu and energy alignment</li><li>Value-driven, future-ready design</li></ul><div class="cr">Your dream is our mission, accuracy is our goal, perfection is our attitude.</div></aside></div></div></section>
<section><div class="wrap"><div class="eyebrow">The group</div><h2 class="rv">Three firms, <mark class="hl">one</mark> vision</h2><div class="firms">
<a href="https://www.archpoint.in" target="_blank" rel="noopener" class="firm rv"><div class="flogo"><img src="assets/img/logo-primary.png" alt="Arch Point Consultants Pvt. Ltd."></div><h3>Arch Point Consultants</h3><span class="tag">Architecture &middot; Interiors &middot; PMC</span><p>Where it all began. We offer architecture, interior design and project management consultancy for homes, commercial spaces, hospitality and institutions, with 500+ projects delivered.</p></a>
<a href="https://www.ekasa.in" target="_blank" rel="noopener" class="firm rv d1"><div class="flogo"><img src="assets/img/logo-apw.png" alt="Arch Point Wellness Pvt. Ltd."></div><h3>Arch Point Wellness</h3><span class="tag">EKASA &middot; Wellbeing</span><p>Our wellness arm and the home of the EKASA brand, bringing design thinking to spaces, programmes and experiences that nurture mind, body and balanced living.</p></a>
<a href="https://www.archpoint.in" target="_blank" rel="noopener" class="firm rv d2"><div class="flogo"><img src="assets/img/logo-apt.png" alt="Arch Point Technology Pvt. Ltd."></div><h3>Arch Point Technology</h3><span class="tag">Software &middot; Automation &middot; AI</span><p>Our technology arm, building software, workflow automation and AI tools that make design, construction and business operations faster and sharper.</p></a></div></div></section>
<section><div class="wrap"><div class="eyebrow">Our process</div><h2 class="rv">Design is a process, not a <mark class="hl">flick of an eye</mark></h2><div class="steps">{''.join(f'<div class="step rv"><b>0{i+1}</b><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate(STEPS))}</div></div></section>
<section style="background:#fff;border-block:1px solid var(--line)"><div class="wrap split"><div><div class="eyebrow">Core values</div><h2 class="rv">The ARCHPOINT <mark class="hl o">way</mark></h2><p class="lead" style="margin-top:18px">Nine values that spell our name and guide every decision we make.</p></div><div class="vals rv">{''.join(f'<span><b>{l}</b>{w}</span>' for l,w in VALS)}</div></div></section>
<section><div class="wrap"><div class="eyebrow">Sectors we serve</div><h2 class="rv">Every scale, <mark class="hl b">every sector</mark></h2><div style="margin-top:30px" class="rv">{''.join(f'<span class="pill">{x}</span>' for x in SECT)}</div></div></section>
<section style="background:#fff;border-block:1px solid var(--line)"><div class="wrap"><div class="eyebrow">Recognition &amp; media</div><h2 class="rv" style="margin-bottom:40px">Recognised, <mark class="hl b">published</mark> and <mark class="hl">on stage</mark></h2><div class="rec rv">
<div><span class="d">08/26</span><div><h3>Livingetc India</h3><p>Featured in the August 2026 issue.</p></div></div>
<div><span class="d">Talk</span><div><h3>ITM Group</h3><p>Invited to speak on architecture and entrepreneurship.</p></div></div>
<div><span class="d">11/10</span><div><h3>Dholera Investors Meet</h3><p>Hosted in Jaipur on 11 October 2026 with Nestoria Group.</p></div></div>
<div><span class="d">04/24</span><div><h3>Indian Iconic Brands &amp; Leaders Award</h3><p>IIBL Awards 2024 winner, with a Certificate of Achievement as Most Admired Architecture Company of the Year (Rajasthan).</p></div></div>
<div><span class="d">02/25</span><div><h3>Asia's Leadership Awards</h3><p>3rd Asia's Leadership Awards 2025 winner, with a Certificate of Achievement.</p></div></div>
<div><span class="d">2025</span><div><h3>National Icon Awards</h3><p>National Icon Award 2025 for Sustainability, with a Certificate of Achievement.</p></div></div>
<div><span class="d">Honour</span><div><h3>Pride of Rajasthan</h3><p>Pride of Rajasthan, presented by The Women Foundation.</p></div></div>
<div><span class="d">Award</span><div><h3>Most Promising Architecture Firm</h3><p>Awarded by Big Research.</p></div></div>
<div><span class="d">Award</span><div><h3>NDTV recognition</h3><p>Awarded by NDTV for a notable project.</p></div></div>
<div><span class="d">Award</span><div><h3>Auditorium design project</h3><p>Award for an auditorium design project.</p></div></div>
<div><span class="d">Honour</span><div><h3>Khandelwal Samaj Trust</h3><p>Appreciation from the Khandelwal Samaj Trust.</p></div></div>
<div><span class="d">Honour</span><div><h3>Todarmal Smarak</h3><p>Appreciation award for the Todarmal Smarak project.</p></div></div>
<div><span class="d">03/25</span><div><h3>International Women's Day</h3><p>Ar. Poonam Jain felicitated on 8 March 2025 at Global Institute of Technology.</p></div></div>
<div><span class="d">ISO</span><div><h3>ISO recognition</h3><p>Recognised for our commitment to quality.</p></div></div>
<div><span class="d">Govt</span><div><h3>Startup recognition</h3><p>Recognised as a startup by the Government of India.</p></div></div>
<div><span class="d">Pod</span><div><h3>Skyline Sessions: Rajasthan</h3><p>Podcast with Pentaspace Design Studio.</p></div></div></div></div></section>
{CTA}'''
page('about.html','About | Ar. Amit Khandelwal','The story of Ar. Amit Khandelwal, Founder & CMD of Arch Point Group: from a growing studio to a family of 100+.',about)
# ---------- PROJECTS
also=['JLN Auditorium','Kapish Tower','Navjeevan Science College','Udaipur Ashram','Varuna MUF Warehousing','JCB Workshop','Celebi','Aksh Optifibre','Siscol','Delhi Institutional Campus','Pentaspace collaborations']
bx=[f for f in PR[0][3]]
feat=f'''<section style="padding-top:0"><div class="wrap"><div class="eyebrow">Featured project</div><h2 class="rv">Baxi Ji <mark class="hl o">Residence</mark></h2><p class="lead rv" style="margin:14px 0 36px">A sculpted private residence, with architecture, PMC and interiors delivered together.</p>
<div class="feat">{''.join(f'<figure class="rv{" fa" if i==0 else ""}"><div class="ph"><img src="assets/img/{"" if i==0 else "t/"}{f}.jpg" alt="Baxi Ji Residence, {l}" loading="lazy" decoding="async"></div><figcaption><b>Baxi Ji Residence</b><span>{l}</span></figcaption></figure>' for i,(f,l) in enumerate(bx))}</div>
<div style="margin-top:34px"><a class="btn" href="gallery.html#baxi">See all in the gallery {ARR}</a></div></div></section'''
secs=''.join(f'<section style="padding-top:0"><div class="wrap"><div class="chead rv"><h2>{CATN[c]}</h2><span>{sum(1 for p in PR if p[0]==c)} projects</span></div><div class="pkg">{cards(c)}</div></div></section>' for c in CATN)
proj=f'''<section class="pagehead"><div class="wrap"><div class="eyebrow">Projects</div><h1>Spaces we have <mark class="hl">brought to life</mark></h1><p class="lead">A selection of the residential, commercial, hospitality, religious and institutional work we are proud of across India. Tap any project to view its photos.</p></div></section>
{secs}
<section style="background:#fff;border-block:1px solid var(--line)"><div class="wrap"><div class="eyebrow">Also delivered</div><h2 class="rv">Many more, <mark class="hl o">across India</mark></h2><div style="margin-top:30px" class="rv">{''.join(f'<span class="pill">{a}</span>' for a in also)}</div></div></section>
{CTA}'''
page('projects.html','Projects | Ar. Amit Khandelwal','Selected projects by Arch Point Group: civic, commercial, hospitality and residential architecture and interiors.',proj,LB)
# ---------- GALLERY
nsig=sum(len(sigp(k)[3]) for _,_,k,_ in SIG)
TEAM=[('team','The Arch Point family','Designers, engineers and PMC specialists'),('team-celebration','Celebrating together','Arch Point team')]
EVT=[('ev-women-foundation','Women Foundation event','Arch Point events'),('ev-wellness-day','Wellness Day','Arch Point events'),('ev-guest-book','Guest book signing','Distinguished guest'),('ev-guest-portrait','With a distinguished guest','Arch Point events'),('ev-guest-ekasa','Felicitating a guest','At EKASA')]
ACH=[('ach-iibl-trophy','Indian Iconic Brands & Leaders Award','IIBL Awards Winner 2024'),('ach-iibl-certificate','IIBL Certificate of Achievement','Most Admired Architecture Company of the Year, Rajasthan'),('ach-national-icon-trophy','National Icon Award 2025','Sustainability · Eminent Research'),('ach-national-icon-certificate','National Icon Awards 2025','Certificate of Achievement'),('ach-pride-of-rajasthan','Pride of Rajasthan Award','The Women Foundation'),('ach-asia-leadership-trophy',"Asia's Leadership Awards 2025",'Winner · 28 February 2025'),('ach-asia-leadership-certificate',"3rd Asia's Leadership Awards 2025",'Certificate of Achievement'),('ach-womens-day-stage',"International Women's Day, 8 March 2025",'Ar. Poonam Jain felicitated'),('ach-womens-day-felicitation','Felicitation ceremony','Global Institute of Technology'),('ach-womens-day-poster','Honouring women achievers','8 March 2025'),('award-2025','Excellence Awards 2025','Architecture & Interior Design'),('awards-asia',"Asia's Leadership Awards",'Trophies & moments')]
gal=f'''<section class="pagehead"><div class="wrap"><div class="eyebrow">Gallery</div><h1>The work, <mark class="hl b">in frames</mark></h1><p class="lead">A mosaic of the projects, people and moments that define Arch Point. Tap any tile to explore its photos.</p>
<div class="filters tabs" role="tablist"><button class="on" data-tab="projects" type="button">Signature projects</button><button data-tab="team" type="button">Team</button><button data-tab="events" type="button">Events</button><button data-tab="achievements" type="button">Achievements</button></div></div></section>
<section style="padding-top:0"><div class="wrap">
<div class="gp" data-p="projects"><div class="mosaic">{''.join(mtile(j,i,n,sb,k) for j,(i,n,k,sb) in enumerate(SIG))}</div></div>
<div class="gp" data-p="team"><p class="gnote">The people behind every project.</p>{car(TEAM)}</div>
<div class="gp" data-p="events"><p class="gnote">Celebrations, wellness days and distinguished guests.</p>{car(EVT)}</div>
<div class="gp" data-p="achievements"><p class="gnote">Awards and recognition that honour the work.</p>{car(ACH)}</div>
</div></section>
{CTA}'''
lb='<div class="lb"><button class="x" aria-label="Close">&times;</button><button class="pv" aria-label="Previous">&lsaquo;</button><img alt=""><p></p><button class="nx" aria-label="Next">&rsaquo;</button></div>'
page('gallery.html','Gallery | Ar. Amit Khandelwal','Signature projects, team, events and achievements of Arch Point Group.',gal,lb)
# ---------- CONTACT
contact=f'''<section class="pagehead"><div class="wrap"><div class="eyebrow">Contact</div><h1>Book an <mark class="hl">appointment</mark></h1><p class="lead">Share a few details and they reach me directly on WhatsApp, so we can confirm your appointment together.</p></div></section>
<section style="padding-top:0"><div class="wrap split cs">
<form class="form" id="bf" novalidate>
<div class="f"><label for="nm">Your name</label><input id="nm" autocomplete="name"><span class="err" id="e_nm"></span></div>
<div class="f"><label for="mb">Mobile</label><input id="mb" type="tel" autocomplete="tel" placeholder="+91"><span class="err" id="e_mb"></span></div>
<div class="f"><label for="pu">Looking for</label><select id="pu"><option value="">Select</option><option>Architecture &amp; design</option><option>Interior design</option><option>Project management (PMC)</option><option>Real estate / investment</option><option>Speaking / collaboration</option><option>Other</option></select><span class="err" id="e_pu"></span></div>
<div class="f"><label for="dt">Preferred date</label><input id="dt" type="date"><span class="err" id="e_dt"></span></div>
<div class="f full"><label for="sl">Preferred time</label><select id="sl"><option>Morning (10 am to 1 pm)</option><option>Afternoon (2 pm to 5 pm)</option><option>Evening (5 pm to 7 pm)</option></select></div>
<div class="f full"><label for="ms">Message (optional)</label><textarea id="ms" rows="3"></textarea></div>
<div class="full"><button class="btn" type="submit">Send on WhatsApp {ARR}</button></div>
<div id="ok"><b>Opening WhatsApp&hellip;</b> If nothing opened, <a id="okLink" href="#" target="_blank" rel="noopener" style="text-decoration:underline;color:var(--blue)">tap here to open WhatsApp</a>.</div></form>
<div class="info rv"><div class="wp" aria-live="polite"><small>Preview of your WhatsApp message</small><div class="bub" id="pv">Hello Ar. Amit Khandelwal, I would like to book an appointment.</div></div><div><small>{ico('message-circle')}WhatsApp</small><a href="https://wa.me/919982507555">+91 99825 07555</a></div><div><small>{ico('phone')}Phone</small><a href="tel:+919982507555">+91 99825 07555</a></div><div><small>{ico('mail')}Email</small><a href="mailto:connect@archpointgp.com">connect@archpointgp.com</a></div><div><small>{ico('globe')}Website</small><a href="https://archpoint.in" target="_blank" rel="noopener">archpoint.in</a></div><div><small>{ico('at-sign')}Instagram</small><a href="https://instagram.com/archpoint_architecture" target="_blank" rel="noopener">@archpoint_architecture</a></div><div><small>{ico('map-pin')}Studio</small><span>Plot No. 92/64, Patel Marg, Sector 9, Mansarovar, Jaipur</span></div><div style="border:0"><button class="btn ghost" id="vcard" type="button">Save contact</button></div></div></div></section>'''
page('contact.html','Book an Appointment | Ar. Amit Khandelwal','Book an appointment with Ar. Amit Khandelwal via WhatsApp.',contact)
print('built')
