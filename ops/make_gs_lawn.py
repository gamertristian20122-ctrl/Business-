"""Preview for G's Lawn Care, built from the lawn-seasons template with facts from their Nextdoor page (2026-11-09)."""
import sys
src = open('/home/user/Business-/lawn-seasons/index.html', encoding='utf-8').read()
out = src
def rep(old, new, count=1):
    global out
    n = out.count(old)
    if n != count: sys.exit(f'count {n} (want {count}): {old[:90]}')
    out = out.replace(old, new)
PH, TEL = "(402) 214-8277", "+14022148277"
rep('<title>Ridgeline Lawn &amp; Snow</title>', "<title>G's Lawn Care | Lawn Care &amp; Snow Removal in Omaha, NE</title>\n<meta name=\"robots\" content=\"noindex, nofollow\">")
rep('content="Weekly mowing, fall cleanup and snow removal across Omaha, Papillion, Bellevue and Elkhorn."',
    "content=\"G's Lawn Care: mowing, bush trimming, leaf and spring cleanup, landscaping, mulch and rock, and snow removal in Omaha. A Nextdoor Fave in 228 neighborhoods.\"")
rep('<div class="demo">Demo site · your name, photos and Google reviews go here</div>',
    "<div class=\"demo\">Preview made for G's Lawn Care. Not live yet, and the quote form doesn't send anything.</div>")
rep('        Ridgeline\n', "        G's Lawn Care\n")
out = out.replace('tel:+14025550148', 'tel:' + TEL).replace('sms:+14025550148', 'sms:' + TEL).replace('(402) 555-0148', PH)
rep('<h1 data-show="lawn">Mowed every week. <em>You never call us twice.</em></h1>', '<h1 data-show="lawn">Your lawn, looking great <em>season after season.</em></h1>')
rep('<h1 data-show="snow">Your driveway clear <em>before 7 a.m.</em></h1>', '<h1 data-show="snow">Snow removal from a crew <em>you already trust.</em></h1>')
rep('<p class="lede" data-show="lawn">Weekly mowing, edging and fall leaf cleanup for homes across Omaha. Same crew, same day, every week.</p>',
    '<p class="lede" data-show="lawn">Mowing, bush trimming, cleanups, landscaping and snow removal from a local Omaha crew neighbors call &ldquo;consistent and very professional.&rdquo;</p>')
rep('<p class="lede" data-show="snow">We plow and shovel once 2 inches hit the ground, so you can back out of the garage on time.</p>',
    "<p class=\"lede\" data-show=\"snow\">When the lawns go to sleep, G's Lawn Care clears snow. Call or text to get on the list before the first storm.</p>")
rep('Call for a price</a>', 'Call or text</a>')
rep('<li><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5 9-10"/></svg>Licensed &amp; insured</li>',
    '<li><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5 9-10"/></svg>Nextdoor Fave in 228 neighborhoods</li>')
rep('<li><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5 9-10"/></svg>Quote back the same day</li>',
    '<li><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5 9-10"/></svg>Over 10 years in business</li>')
rep('<li><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5 9-10"/></svg>No contract to start</li>',
    '<li><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12l5 5 9-10"/></svg>Free quotes by call or text</li>')
rep("<p>Clear prices up front. We'll confirm the exact number after a quick look at your yard.</p>", '<p>Every yard is different, so every job starts with a free quote.</p>')
FREE = '<span class="price">Free<small>quote</small></span>'
lawn_old = out[out.index('<ul class="services" data-show="lawn">'):out.index('</ul>', out.index('<ul class="services" data-show="lawn">'))+5]
rep(lawn_old, '<ul class="services" data-show="lawn">\n' + '\n'.join(f'        <li><h3>{h}</h3>{FREE}<p>{p}</p></li>' for h, p in [
    ('Lawn mowing', 'Professional mowing that leaves a clean, even pattern your neighbors will notice.'),
    ('Bush trimming', 'Bushes and shrubs shaped and tidied up.'),
    ('Fall leaf cleanup', 'Get your lawn leaf free before the winter freeze, and your plants winterized.'),
    ('Spring cleanup', 'Get the yard ready for the season.'),
    ('Landscaping &amp; planting', 'From a few new plants to transforming the whole yard.'),
    ('Mulch &amp; rock', 'Mulch and rock installed or removed.')]) + '\n      </ul>')
snow_old = out[out.index('<ul class="services" data-show="snow">'):out.index('</ul>', out.index('<ul class="services" data-show="snow">'))+5]
rep(snow_old, '<ul class="services" data-show="snow">\n' + f'        <li><h3>Snow removal</h3>{FREE}<p>Driveways and walks cleared in winter. Call or text to get on the list.</p></li>\n      </ul>')
rep('<p class="note">Sample prices for the demo. Your real prices go here.</p>', '<p class="note">Need something not listed? Just ask.</p>')
trig = out[out.index('<div class="trigger" data-show="snow">'):out.index('</div>', out.index('<div class="trigger" data-show="snow">'))+6]
rep(trig, '')
rep('<p>Omaha and the suburbs around it. Not on the list? Call and ask.</p>', '<p>Neighbors in these towns named G&rsquo;s Lawn Care a Nextdoor Fave. Not on the list? Call and ask.</p>')
area_old = out[out.index('<ul class="area">'):out.index('</ul>', out.index('<ul class="area">'))+5]
rep(area_old, '<ul class="area">\n' + '\n'.join(f'        <li>{a}<span>{s}</span></li>' for a, s in [('Omaha','NE'),('Bennington','NE'),('Blair','NE'),('Fort Calhoun','NE'),('Arlington','NE'),('Carter Lake','IA'),('Council Bluffs','IA'),('Crescent','IA')]) + '\n      </ul>')
rep('<li><b>Call, text or fill out the form</b><span>Tell us your address and what you need.</span></li>', '<li><b>Call, text or fill out the form</b><span>Tell us your address and what you need done.</span></li>')
rep('<li><b>Get your price the same day</b><span>We look at the yard and text you a number.</span></li>', '<li><b>Get a free quote</b><span>The crew looks at your yard and gives you a fair price.</span></li>')
rep('<li data-show="lawn"><b>First mow this week</b><span>After that, we show up on the same day every week.</span></li>', '<li data-show="lawn"><b>Enjoy a great-looking lawn</b><span>Done thoroughly, with gates closed behind us every time.</span></li>')
rep("<li data-show=\"snow\"><b>You're on the route</b><span>Next time it snows, your driveway gets cleared.</span></li>", "<li data-show=\"snow\"><b>You're on the list</b><span>When the snow comes, G's Lawn Care clears it.</span></li>")
rep('<p><span class="sample-tag">Sample reviews</span> Your real Google reviews show here.</p>', '<p><span class="sample-tag">Real reviews</span> From neighbors on Nextdoor. 159 neighbors have made G&rsquo;s Lawn Care a Fave.</p>')
rep("<blockquote>A customer's review goes here, word for word from Google.</blockquote>\n          <figcaption>Customer name · Neighborhood</figcaption>",
    '<blockquote>I really love the way this company treated me as a customer, I felt valued. They were consistent and very professional.</blockquote>\n          <figcaption>M. L. · Omaha</figcaption>')
star_fig = out[out.index('<figure class="review">'):out.index('</figure>', out.index('<figure class="review">'))+9]
rep('<blockquote>A second review. Three or four short ones beat one long one.</blockquote>\n          <figcaption>Customer name · Neighborhood</figcaption>',
    '<blockquote>The crew leader was amazing and assessed my lawn and gave me a reasonable price and did an amazing job!</blockquote>\n          <figcaption>M. G. · Omaha</figcaption>')
third = star_fig.replace('I really love the way this company treated me as a customer, I felt valued. They were consistent and very professional.', 'Love these guys! Always very friendly and willing to help. I couldn&rsquo;t ask for better service.').replace('M. L. · Omaha', 'A. T. · Omaha')
rep('</figure>\n      </div>\n    </div>\n  </section>\n\n  <section id="quote">', '</figure>\n        ' + third + '\n      </div>\n    </div>\n  </section>\n\n  <section id="quote">')
rep('<p>Takes about a minute. We text you back the same day.</p>', "<p>Takes about a minute. G's Lawn Care will call or text you back.</p>")
rep('<option>Weekly mowing</option><option>Fall leaf cleanup</option><option>Aeration &amp; overseed</option><option>Spring cleanup</option>\n            <option>Snow removal, per storm</option><option>Snow season contract</option><option>Something else</option>',
    '<option>Lawn mowing</option><option>Bush trimming</option><option>Fall leaf cleanup</option><option>Spring cleanup</option>\n            <option>Landscaping &amp; planting</option><option>Mulch or rock</option><option>Snow removal</option><option>Something else</option>')
rep("svc.selectedIndex = season === 'snow' ? 4 : 0;", "svc.selectedIndex = season === 'snow' ? 6 : 0;")
rep('<p>This is the demo, so nothing was sent. On the live site, this form texts the owner right away with the customer\'s name, number and address.</p>',
    "<p>This is a preview, so nothing was sent. On the live site, this form goes straight to G's Lawn Care with the customer's name, number and address.</p>")
rep('<div class="mark" style="color:var(--fg)">Ridgeline Lawn &amp; Snow</div>', '<div class="mark" style="color:var(--fg)">G&rsquo;s Lawn Care</div>')
rep('<dt>Mon–Fri</dt><dd>7 a.m. – 7 p.m.</dd>\n      <dt>Saturday</dt><dd>8 a.m. – 4 p.m.</dd>\n      <dt>Snow days</dt><dd>On call from 3 a.m.</dd>',
    '<dt>Mon–Fri</dt><dd>7 a.m. – 8 p.m.</dd>\n      <dt>Sat–Sun</dt><dd>Closed</dd>')
rep('<p>Omaha, Nebraska. Sample business for a website demo; the name and number are made up.</p>', '<p>Omaha, Nebraska. Lawn care, landscaping and snow removal.</p>')
for bad in ['Ridgeline', '555-0148', '555-0', 'Sample prices', 'Licensed &amp; insured', 'from $']:
    if bad in out and bad != '555-0': sys.exit('LEFTOVER ' + bad)
open('/home/user/Business-/demos/gs-lawn-care/index.html', 'w', encoding='utf-8').write(out)  # template already has the [hidden] fix
print('ok', len(out), 'placeholder 402-555-0123 kept in phone field:', '402-555-0123' in out)
