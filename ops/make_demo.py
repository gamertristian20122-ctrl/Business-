"""Build a client preview from Business-/cleaning/index.html. Usage: python3 make_demo.py <spec.py> <out_dir>"""
import sys, json, os, shutil, runpy
spec = runpy.run_path(sys.argv[1])['SPEC']
out_dir = sys.argv[2]
src = open('/home/user/Business-/cleaning/index.html', encoding='utf-8').read()
out = src
def rep(old, new):
    global out
    n = out.count(old)
    if n != 1: sys.exit(f'count {n}: {old[:90]}')
    out = out.replace(old, new)
S = spec
rep('<title>Sparkline Cleaning Co.</title>', f'<title>{S["title"]}</title>\n<meta name="robots" content="noindex, nofollow">')
rep('content="House cleaning in Omaha, NE. Standard, deep, move-in/move-out and recurring cleaning from insured, background-checked cleaners. Free quote in minutes."', f'content="{S["description"]}"')
rep('content="house cleaning Omaha, maid service Omaha, deep cleaning Omaha, move out cleaning Omaha, recurring cleaning Omaha NE"', f'content="{S["keywords"]}"')
start = out.index('window.SITE = {'); end = out.index('};', start) + 2
out = out[:start] + 'window.SITE = ' + json.dumps(S['site'], ensure_ascii=False, indent=2) + ';' + out[end:]
rep('<div class="demo">Demo site for a made-up Omaha business. Name, number, prices and reviews are placeholders.</div>',
    f'<div class="demo">Preview made for {S["site"]["name"]}. Not live yet, and the quote form doesn\'t send anything.</div>')
rep('<a href="#prices">Prices</a>', '<a href="#prices">Services</a>')
rep('<p class="lede">Here\'s what a cleaning day with <span data-text="name">Sparkline Cleaning Co.</span> looks like, from Sunday night on your phone to Tuesday at 5:30, when you walk into a clean house.</p>', f'<p class="lede">{S["lede"]}</p>')
rep('<a class="btn btn-cyan" href="#quote">Get a Free Quote</a>', '<a class="btn btn-cyan" href="#quote">Get a Free Estimate</a>')
rep('''        <li><b>Insured</b><span>on every job</span></li>
        <li><b>Background-checked</b><span>every cleaner</span></li>
        <li><b>24-hour guarantee</b><span>we come back free</span></li>
        <li><b>Eco option</b><span>plant-based products</span></li>''', '\n'.join(f'        <li><b>{a}</b><span>{b}</span></li>' for a, b in S['trust']))
rep('<p>Starting prices for a typical 3-bedroom home. Your quote depends on size and condition, and you\'ll see it before anything is booked.</p>', f'<p>{S["services_intro"]}</p>')
rep('<p class="svc-note">Sample prices for this demo.</p>', '<p class="svc-note">Need something not listed? Ask when you call.</p>')
rep('<figcaption class="spec">Standard clean · about 2.5 hours</figcaption>', f'<figcaption class="spec">{S["photo_caption"]}</figcaption>')
rep('<h2 id="how-h">We text you a time</h2>', f'<h2 id="how-h">{S["how_h"]}</h2>')
rep('<p>Three steps from asking to a clean house. No in-home estimate, no contract.</p>', '<p>Three steps from asking to a clean space.</p>')
steps = S['steps']
rep('<li><span class="spec">Step 1 · 2 minutes</span><h3>Request a quote</h3><p>Use the form or call. Tell us how many bedrooms and baths, and what kind of clean.</p></li>', f'<li><span class="spec">Step 1 · {steps[0][0]}</span><h3>{steps[0][1]}</h3><p>{steps[0][2]}</p></li>')
rep('<li><span class="spec">Step 2 · same day</span><h3>We confirm a time</h3><p>You get a price and a time slot by text. Reply yes and you\'re on the calendar.</p></li>', f'<li><span class="spec">Step 2 · {steps[1][0]}</span><h3>{steps[1][1]}</h3><p>{steps[1][2]}</p></li>')
rep('<li><span class="spec">Step 3 · cleaning day</span><h3>Come home clean</h3><p>We clean, lock up and text you a photo when we leave. You pay after.</p></li>', f'<li><span class="spec">Step 3 · {steps[2][0]}</span><h3>{steps[2][1]}</h3><p>{steps[2][2]}</p></li>')
rep('<h2 id="arrive-h">Two cleaners let themselves in</h2>', f'<h2 id="arrive-h">{S["arrive_h"]}</h2>')
rep('<p>You\'re trusting someone with your keys. Here\'s what we do to earn it.</p>', f'<p>{S["arrive_p"]}</p>')
rep('<figcaption class="spec">Our eco line, on request</figcaption>', f'<figcaption class="spec">{S["supplies_caption"]}</figcaption>')
rep('<div class="trust-stat"><b>2</b><span>cleaners per home, the same pair each visit on a schedule</span></div>', f'<div class="trust-stat"><b>{S["stat"][0]}</b><span>{S["stat"][1]}</span></div>')
rep('''          <li><h3>Insured</h3><p>Liability insurance covers every job. If something gets broken, it gets paid for.</p></li>
          <li><h3>Background-checked</h3><p>Every cleaner passes a background check before they walk into their first home.</p></li>
          <li><h3>Satisfaction guarantee</h3><p>Missed a spot? Tell us within 24 hours and we'll come back and redo it, free.</p></li>
          <li><h3>Eco-friendly option</h3><p>Plant-based, fragrance-free products for homes with kids, pets or allergies. Just ask when you book.</p></li>''', '\n'.join(f'          <li><h3>{a}</h3><p>{b}</p></li>' for a, b in S['promises']))
rep('<p class="rev-intro"><span class="sample">Sample reviews</span>Placeholders. The client\'s real Google reviews go here.</p>', f'<p class="rev-intro"><span class="sample">{S["rev_tag"]}</span>{S["rev_intro"]}</p>')
rep('<h2 id="area-h">Neighborhoods we clean in <span data-text="city">Omaha</span></h2>', f'<h2 id="area-h">{S["area_h"]}</h2>')
rep('<h2 id="quote-h">Get a free quote</h2>', '<h2 id="quote-h">Get a free estimate</h2>')
rep('<p>Takes about a minute. We\'ll text or email you a price, usually the same day.</p>', f'<p>{S["quote_p"]}</p>')
rep('<p class="form-foot">We only use your info to send your quote.</p>', '<p class="form-foot">Your info is only used to set up your estimate.</p>')
rep('<button class="btn btn-cyan" type="submit">Send my quote request</button>', '<button class="btn btn-cyan" type="submit">Send my estimate request</button>')
rep('btn.textContent = "Send my quote request"', 'btn.textContent = "Send my estimate request"')
rep('<p id="done-msg">We\'ll text or email you a price shortly.</p>', f'<p id="done-msg">{S["done_msg"]}</p>')
rep('<a class="btn btn-cyan" href="#quote">Free Quote</a>', '<a class="btn btn-cyan" href="#quote">Free Estimate</a>')
rep('<p class="legal">© <span id="year">2026</span> <span data-text="name">Sparkline Cleaning Co.</span> All rights reserved.</p>', f'<p class="legal">© <span id="year">2026</span> <span data-text="name">{S["site"]["name"]}</span>{S.get("legal_extra", "")}</p>')
rep('''return '<li class="svc"><h3>' + esc(s.name) + '</h3><span class="price"><span class="from">from</span>$' + esc(s.price) + "<small>" + esc(s.unit) + "</small></span><p>" + esc(s.line) + "</p>" + plans + "</li>";''',
    '''var price = s.price ? '<span class="from">from</span>$' + esc(s.price) : '<span class="from">price</span>Free';
    return '<li class="svc"><h3>' + esc(s.name) + '</h3><span class="price">' + price + "<small>" + esc(s.unit) + "</small></span><p>" + esc(s.line) + "</p>" + plans + "</li>";''')
rep('''"telephone": S.phoneLink, "email": S.email, "foundingDate": String(S.founded), "priceRange": "$$",''', '''"telephone": S.phoneLink, "email": S.email,''')
rep('''"address": { "@type": "PostalAddress", "addressLocality": S.city, "addressRegion": S.state, "postalCode": S.zip, "addressCountry": "US" },''', '''"address": { "@type": "PostalAddress", "addressLocality": S.city, "addressRegion": S.state, "addressCountry": "US" },''')
rep('''"areaServed": S.areas.map(function (a) { return { "@type": "Place", "name": a + ", " + S.city + ", " + S.state }; }),''', '''"areaServed": S.areas.map(function (a) { return { "@type": "Place", "name": a + ", " + S.state }; }),''')
rep('''"makesOffer": S.services.map(function (s) { return { "@type": "Offer", "name": s.name, "price": s.price, "priceCurrency": "USD" }; })''', '''"makesOffer": S.services.map(function (s) { return { "@type": "Offer", "itemOffered": { "@type": "Service", "name": s.name } }; })''')
rep('"description": "House cleaning in " + S.city + ", " + S.state + ". " + S.tagline + ".",', '"description": "Cleaning in " + S.city + ", " + S.state + ". " + S.tagline + ".",')
ph, pl, em, nm = S['site']['phone'], S['site']['phoneLink'], S['site']['email'], S['site']['name']
out = out.replace('tel:+14025550199', 'tel:' + pl).replace('(402) 555-0199', ph)
out = out.replace('mailto:hello@sparklinecleaning.example', 'mailto:' + em).replace('hello@sparklinecleaning.example', em)
out = out.replace('Sparkline Cleaning Co.', nm).replace('Spotless homes across Omaha', S['site']['tagline'])
for bad in ['Sparkline', '555-0199', '24-hour guarantee', 'Background-checked']:
    if bad in out: sys.exit('LEFTOVER: ' + bad)
os.makedirs(out_dir, exist_ok=True)
if not os.path.exists(os.path.join(out_dir, 'images')):
    shutil.copytree('/home/user/Business-/cleaning/images', os.path.join(out_dir, 'images'))
open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(out)
print('ok', out_dir, len(out))
