#!/usr/bin/env python3
"""Static site generator for Drew's Market.

Content rebuilt from the clean Jan 14, 2026 Wayback Machine snapshot
(pre-compromise). No WordPress, no PHP, no plugins.

Usage:
  python3 build.py                 # images from ./images (production)
  python3 build.py --preview DIR   # images hot-linked from the Wayback Machine
"""
import os, sys, html

PHONE = "(732) 974-9399"
PHONE_TEL = "+17329749399"
EMAIL = "drewsmarketspringlake@gmail.com"
ADDRESS_1 = "2407 NJ-71"
ADDRESS_2 = "Spring Lake Heights, New Jersey 07762"
MAPS = "https://www.google.com/maps/search/?api=1&query=Drew%27s+Market+2407+NJ-71+Spring+Lake+NJ+07762"
HOURS = [("Monday", "10:00 am – 6:00 pm"), ("Tuesday", "10:00 am – 6:00 pm"),
         ("Wednesday", "10:00 am – 6:00 pm"), ("Thursday", "10:00 am – 6:00 pm"),
         ("Friday", "10:00 am – 6:00 pm"), ("Saturday", "10:00 am – 6:00 pm"),
         ("Sunday", "10:00 am – 4:00 pm")]
ARCHIVE = "https://web.archive.org/web/20260114193002im_/https://drewsmarket.com/wp-content/uploads/"

# image key -> path under wp-content/uploads (also used by fetch-images.sh)
IMAGES = {
    # Only these 10 images exist in the Wayback snapshot; others alias to them.
    "logo": "2024/05/logo-new.png",
    "ribs": "2021/05/image-34.jpg",
    "reuben": "2024/04/grilled-reuben-sandwich.jpg",
    "steak": "2021/06/parallax-29.jpg",
    "burgers": "2021/07/product-1.jpg",
    "meatballs": "2021/07/product-2.jpg",
    "cuts": "2021/07/product-4.jpg",
    "roastbeef": "2024/04/Boars-Head-Roast-Beef.jpg",
    "chickenparm": "2024/04/Hot-Hero-Chicken-Parmigiana-300x300.jpeg",
    "seagirt": "2024/04/sea-girt-300x300.jpg",
}
ALIAS = {"hero": "steak", "parallax": "cuts", "meat": "steak", "antipasto": "ribs", "p1": "burgers",
         "p2": "meatballs", "p4": "cuts", "eggplant": "meatballs", "cheese": "chickenparm", "chicken": "seagirt"}

NAV = [("index.html", "Home"), ("about.html", "About"), ("butcher.html", "Butcher"),
       ("deli.html", "Deli"), ("catering.html", "Catering"), ("menus.html", "Menus"),
       ("gallery.html", "Gallery"), ("testimonials.html", "Testimonials"),
       ("faq.html", "FAQ"), ("contact.html", "Contact")]

img_base = "images/"


def img(key, alt, cls=""):
    path = IMAGES[ALIAS.get(key, key)]
    src = (ARCHIVE + path) if img_base == "ARCHIVE" else img_base + os.path.basename(path)
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{src}" alt="{html.escape(alt)}" loading="lazy"{c}>'


def page(fname, title, desc, body):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{h}"{cur if h == fname else ""}>{t}</a>' for h, t in NAV)
    hours = "".join(f"<li><span>{d}</span><span>{t}</span></li>" for d, t in HOURS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Restaurant","name":"Drew's Market","servesCuisine":"Italian","telephone":"{PHONE_TEL}","email":"{EMAIL}","address":{{"@type":"PostalAddress","streetAddress":"{ADDRESS_1}","addressLocality":"Spring Lake Heights","addressRegion":"NJ","postalCode":"07762","addressCountry":"US"}},"openingHours":["Mo-Sa 10:00-18:00","Su 10:00-16:00"]}}</script>
</head>
<body>
<div class="topbar"><div class="wrap">
  <span>Open 7 days a week · Mon–Sat 10–6 · Sun 10–4</span>
  <a href="tel:{PHONE_TEL}">{PHONE}</a>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html">{img("logo", "Drew's Market")}</a>
  <input type="checkbox" id="navtoggle" class="navtoggle" aria-label="Menu">
  <label for="navtoggle" class="burger" aria-hidden="true"><span></span><span></span><span></span></label>
  <nav class="site-nav">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site-footer"><div class="wrap cols">
  <div>
    <h3>Drew's Market</h3>
    <p>Italian Specialties · Deli · Butcher · Catering<br>Est. 1986</p>
    <p><a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS_1}<br>{ADDRESS_2}</a></p>
    <p><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
  <div>
    <h3>Hours</h3>
    <ul class="hours">{hours}</ul>
  </div>
  <div>
    <h3>Site Links</h3>
    <p><a href="terms.html">Terms &amp; Conditions</a><br><a href="privacy.html">Privacy Policy</a><br><a href="returns.html">Return Policy</a></p>
  </div>
</div>
<div class="copy">© 2026 Drew's Market Italian Specialties Deli Butcher Catering · FATSOX Inc, dba Drew's Market</div>
</footer>
</body>
</html>
"""


PRICE_NOTE = f'<p class="callprice">Call <a href="tel:{PHONE_TEL}">{PHONE}</a> for current prices.</p>'


def cta(text="Call to order"):
    return (f'<div class="cta-row"><a class="btn" href="tel:{PHONE_TEL}">{text}: {PHONE}</a>'
            f'<a class="btn ghost" href="mailto:{EMAIL}">Email us</a></div>')


def ul(items, cls="list"):
    return f'<ul class="{cls}">' + "".join(f"<li>{html.escape(i)}</li>" for i in items) + "</ul>"


def hero(title, sub, key="hero"):
    k = IMAGES[ALIAS.get(key, key)]
    bg = (ARCHIVE + k) if img_base == "ARCHIVE" else img_base + os.path.basename(k)
    return (f'<section class="hero" style="background-image:linear-gradient(rgba(20,12,8,.62),rgba(20,12,8,.62)),url(\'{bg}\')">'
            f'<div class="wrap"><h1>{title}</h1><p>{sub}</p></div></section>')


PAGES = {}

PAGES["index.html"] = ("Drew's Market – Italian Cooking, Butcher & Catering | Spring Lake Heights, NJ",
 "Authentic homemade Italian cooking, a full-service butcher and catering in Spring Lake Heights, NJ since 1986.",
 hero("Authentic Homemade Italian Cooking",
      "Voted #1 Monmouth Magazine Readers' Choice — Best Caterer, Best Deli, Best Butcher.") + f"""
<a class="promo" href="thanksgiving.html"><strong>Thanksgiving 2026 orders are open!</strong> Fresh all-natural turkeys, cooked dinners &amp; sides. Order by Sunday 11/22 &rarr;</a>
<section class="wrap intro">
  <p class="lead">We use only the freshest, highest quality ingredients to make sure everything is delicious and presented beautifully.</p>
  {cta()}
</section>
<section class="wrap cards">
  <a class="card" href="catering.html">{img("ribs", "Barbecue ribs")}<h2>Catering</h2><p>Trays and full menus for every occasion, available all year round.</p></a>
  <a class="card" href="deli.html">{img("reuben", "Grilled Reuben sandwich")}<h2>Deli</h2><p>Boar's Head provisions, hot heroes and homemade salads made daily.</p></a>
  <a class="card" href="butcher.html">{img("cuts", "Fresh cuts of meat")}<h2>Butcher</h2><p>Prime beef, Bell &amp; Evans poultry, veal, lamb, pork and homemade sausage.</p></a>
</section>
<section class="band"><div class="wrap split">
  <div>
    <h2>Our Menu</h2>
    <h3>Meat Market</h3>{ul(["Chicken Cutlets", "Beef Brisket", "Pork Belly"])}
    <h3>Catering Favorites</h3>{ul(["Pork Marsala", "Chicken Balsamic", "Beef Burgundy"])}
    <p><a class="btn" href="menus.html">See all menus</a></p>
  </div>
  <div>{img("meatballs", "Homemade meatballs", "rounded")}</div>
</div></section>
""")

PAGES["about.html"] = ("About Us – Drew's Market | Est. 1986", "Family-run Italian market in Spring Lake Heights, NJ since 1986.",
 hero("Welcome to Drew's", "Est. 1986", "cuts") + f"""
<section class="wrap split">
  <div>
    <h2>Only the Best Quality</h2>
    <p>For nearly four decades Drew's Market has served the Jersey Shore with tasty, savory Italian specialties, a full-service butcher counter and catering for every occasion.</p>
    <h3>Our Specialties</h3>{ul(["Butcher", "Catering", "Deli"])}
    <h3>We carry</h3>{ul(["Lamb", "Beef", "Veal", "Pork", "Rabbit"], "chips")}
  </div>
  <div class="stack">{img("burgers", "Sirloin burgers", "rounded")}{img("meatballs", "Homemade meatballs", "rounded")}</div>
</section>
""")

BEEF = ["Beef Brisket", "Beef Braciole", "Beef Tenderloin", "Bone-in Beef Short Ribs", "Butter Steak (Flat Iron)",
        "Corned Beef – 1st & 2nd Cut", "Ground Sirloin", "NY Strip Steak", "Porterhouse Steak", "Ribeye",
        "Cowboy Ribeye", "Silver Tip", "Sirloin Hamburgers", "Sirloin Kabobs", "Sirloin London Broil",
        "Sirloin Sliders", "Sirloin Stew Meat", "Steak Pinwheels", "T-Bone Steak", "Tri Tip"]
POULTRY = ["Bell & Evans Chicken Cutlet", "Bell & Evans Whole Chicken", "Bell & Evans Fresh Whole Turkey",
           "Chicken – Raw Wings", "Chicken – Bone-in Legs & Thighs", "Chicken Cordon Bleu", "Chicken Kabobs",
           "Chicken Oreganata", "Chicken Patties", "Chicken Sausage", "Ground Chicken", "Ground Turkey",
           "Turkey Breast – Bone In", "Turkey London Broil", "Turkey Patties", "Turkey Roast"]
OTHER = ["Baby Back Ribs", "Ground Pork", "Ground Beef, Pork & Veal", "Pork Braciole", "Pork Butt", "Pork Chops",
         "Pork Chops – Apple Stuffing", "Pork Crown Roast", "Pork Kabobs", "Pork Loin – Stuffed Country Apple",
         "Pork Loin – Stuffed Italian", "Pork Tenderloin", "Sausage – Homemade", "Sausage – Cheese & Parsley Ring",
         "Sausage Kabobs", "Slab Bacon", "Pulaski Polish Kielbasa Ring", "Thumann's Hotdogs", "Ground Veal",
         "Veal Cutlets", "Veal Osso Bucco", "Lamb Boneless Chops", "Lamb Chops – Loin", "Lamb Crown Roast",
         "Lamb Leg – Bone In", "Lamb Leg Boneless", "Lamb Loin Eye", "Lamb Rack"]

PAGES["butcher.html"] = ("Butcher – Drew's Market | Fresh Cuts Daily", "Prime beef, poultry, pork, veal and lamb cut daily in Spring Lake Heights, NJ.",
 hero("Butcher", "Becoming a vegetarian is a big missed steak.", "meat") + f"""
<section class="wrap">
  <p class="lead">Quality craftsmanship and the freshest cuts. Call ahead and we'll have your order ready.</p>
  <div class="cols3">
    <div><h2>Beef</h2>{ul(BEEF)}</div>
    <div><h2>Poultry</h2>{ul(POULTRY)}</div>
    <div><h2>Pork, Veal, Lamb &amp; More</h2>{ul(OTHER)}</div>
  </div>
  <p class="note">Final prices for butcher items are determined by final weight once prepared. A non-refundable deposit is required for all butcher orders; the balance, less deposit, is due at pick-up. Prices are subject to change without notice.</p>
  {PRICE_NOTE}
  {cta()}
</section>
""")

SALADS = ["Shrimp", "Tuna", "Chicken", "Pasta", "Antipasto", "Potato", "Coleslaw", "Macaroni", "Fruit", "Penne Tomato"]
HOT = ["Eggplant Rollatini", "Lasagna", "Lasagna Rollups", "Eggplant Parm", "Eggplant Towers", "Turkey London Broil",
       "Chicken Francese", "Chicken Payetta", "Fried & Grilled Chicken Cutlets", "Mashed Potatoes", "Mac & Cheese"]

PAGES["deli.html"] = ("Deli – Drew's Market | Boar's Head & Homemade", "Boar's Head and imported meats and cheeses, hot heroes and homemade salads made daily.",
 hero("Deli", "Boar's Head Provisions &amp; Homemade") + f"""
<section class="wrap">
  <p class="lead">Premium Boar's Head and imported deli meats &amp; cheeses, plus an extensive collection of fresh salads and foods made daily — and too many more to list.</p>
  <div class="cols3">
    <div><h2>Salads</h2>{ul(SALADS)}</div>
    <div><h2>Prepared Foods</h2>{ul(HOT)}</div>
    <div><h2>Sandwich Favorites</h2>
      {ul(["Grilled Reuben", "Hot Hero Chicken Parmigiana", "Hot Hero Milano", "Sea Girt", "Hot Grilled Pork"])}
    </div>
  </div>
  <div class="cards small">{img("reuben", "Grilled Reuben")}{img("chickenparm", "Chicken Parm hero")}{img("seagirt", "Sea Girt sandwich")}{img("roastbeef", "Boar's Head roast beef")}</div>
  {PRICE_NOTE}
  {cta()}
</section>
""")

PAGES["catering.html"] = ("Catering – Drew's Market | Custom Menus for Every Occasion", "Italian catering for parties, showers, graduations, funerals and corporate events.",
 hero("Catering", "Our catering menu is available all year round.", "ribs") + f"""
<section class="wrap">
  <p class="lead">From intimate family gatherings to 300-sandwich corporate luncheons, we'll build the right menu for your event.</p>
  <h2>Platters</h2>
  {ul(["Antipasto Platter (Small, Medium, Large)", "Asparagus w/ Roasted Garlic & Olive Oil", "Shrimp Cocktail Platter", "Caprese Platter", "Hot trays, entrées, pasta & salads", "Sandwich platters & desserts"])}
  {PRICE_NOTE}
  <p>Hosting for the holidays? <a href="thanksgiving.html">See our Thanksgiving 2026 menu</a>.</p>
  <div class="cards small">{img("ribs", "Barbecue ribs")}{img("meatballs", "Homemade meatballs")}{img("chickenparm", "Chicken Parm hero")}{img("roastbeef", "Boar's Head roast beef")}</div>
  {cta("Plan your event")}
</section>
""")

PAGES["menus.html"] = ("Menus – Drew's Market | Catering, Sandwich & Holiday Menus", "Download Drew's Market catering, sandwich & salad, holiday menus and cooking instructions.",
 hero("Menus", "Catering · Sandwich &amp; Salad · Holiday · Cooking Instructions") + f"""
<section class="wrap">
  <div class="cards">
    <div class="card"><h2>Catering Menu</h2><p>Available all year round.</p><p>Call for the current menu and prices.</p></div>
    <div class="card"><h2>Sandwich &amp; Salad Menu</h2><p>Heroes, wraps, homemade salads.</p><p>Call for the current menu and prices.</p></div>
    <a class="card feature" href="thanksgiving.html"><h2>Thanksgiving 2026</h2><p>Fresh turkeys, cooked dinners, sides &amp; desserts. Order by <strong>Sunday 11/22</strong>.</p><p><span class="btn">View menu</span></p></a>
    <div class="card"><h2>Cooking Instructions</h2><p>Reheating instructions for cooked holiday foods and roasts.</p><p class="todo">PDF coming soon.</p></div>
  </div>
  {cta()}
</section>
""")

PAGES["gallery.html"] = ("Gallery – Drew's Market", "Photos of Drew's Market catering, deli and butcher.",
 hero("Gallery", "A taste of what we make") + '<section class="wrap"><div class="gallery">' +
 "".join(img(k, a) for k, a in [("ribs", "Barbecue ribs"), ("steak", "Fresh steak"), ("cuts", "Prime cuts"), ("burgers", "Sirloin burgers"), ("meatballs", "Homemade meatballs"), ("reuben", "Grilled Reuben"), ("chickenparm", "Chicken Parm hero"), ("seagirt", "Sea Girt sandwich"), ("roastbeef", "Boar's Head roast beef")]) + "</div></section>")

def tg_list(items):
    return '<ul class="price">' + "".join(f"<li><span>{html.escape(a)}</span><span>{html.escape(b)}</span></li>" for a, b in items) + "</ul>"


PAGES["thanksgiving.html"] = ("Thanksgiving 2026 Menu – Drew's Market | Spring Lake Heights, NJ",
 "Order fresh all-natural turkeys, cooked turkey dinners, sides and desserts from Drew's Market. Order deadline Sunday 11/22.",
 hero("Thanksgiving Specials 2026", "Order &amp; change deadline: <strong>Sunday 11/22</strong>", "ribs") + f"""
<section class="wrap">
  <div class="note tg-hours">
    <p><strong>Holiday hours:</strong> Mon 11/23 10–6 · Tue 11/24 10–6 · Wed 11/25 9–6 · <strong>Closed</strong> Thanksgiving 11/26 &amp; Friday 11/27</p>
    <p>Our turkeys are all natural, all grain-fed vegetable diet, no antibiotics, air chilled and never frozen!</p>
  </div>
  <div class="cta-row"><a class="btn" href="tel:{PHONE_TEL}">Call to order: {PHONE}</a><a class="btn ghost" href="thanksgiving-menu.html">View / print menu</a></div>
  <div class="cols2">
    <div>
      <h2>Fresh Turkey</h2>
      {tg_list([("Turkey Roast, 5–6 lbs, bone-in", "$8.99/lb"), ("Turkey Roast, 5–6 lbs, boneless", "$12.99/lb"),
                ("Fresh Whole Turkey", "$5.89/lb"), ("Turkey London Broil", "$11.99/lb"), ("Sausage, loose Italian or traditional sage", "$9.99/lb")])}
      <p class="small">Whole turkeys: 10–12, 12–14, 16–18, 20–22, 24–26, 30–32 lbs. London broils: lemon basil, honey mustard, honey teriyaki or balsamic.</p>
      <h2>Cooked &amp; Ready</h2>
      {tg_list([("Cooked Whole Turkey, carved & sliced on the frame (serves 8–10)", "$130"),
                ("Cooked Sliced Turkey Breast (serves 8–10)", "$79.99"),
                ("Cooked Virginia Ham, large (~60 slices)", "$79.99"), ("Cooked Virginia Ham, small (~30 slices)", "$59.99"),
                ("Heritage Berkshire Ham (100% Kurobuta, no nitrates or antibiotics)", "$12.99/lb")])}
      <p class="small">Virginia ham is sliced, tied, glazed and garnished with cherries and pineapple.</p>
    </div>
    <div>
      <h2>Sides <small>(half trays serve 10–12)</small></h2>
      {tg_list([("Sweet Potato Mashed", "$59.99"), ("Homemade Stuffing", "$59.99"), ("Mac-N-Cheese", "$49.99"),
                ("Mashed Potatoes", "$59.99"), ("String Beans in Garlic & Oil", "$49.99"), ("Antipasto Platter", "$69.99"),
                ("Shrimp Cocktail Platter (50 pcs)", "$89.99"), ("Caprese Platter", "$59.99"),
                ("Turkey Gravy (quart)", "$9.99"), ("Cranberry Sauce (quart)", "$9.99")])}
      <h2>Desserts</h2>
      {tg_list([("Chocolate Cornucopia", "$39.99"), ("Apple Pie or Pumpkin Pie", "$17.99"),
                ("Chocolate Brownie & Cookie Platter", "$29.99"), ("Chocolate Chip Cookie Platter", "$19.99")])}
    </div>
  </div>
  <div class="dinner">
    <h2>Complete Thanksgiving Dinner — $350</h2>
    <p>Serves 8–10 people. Half trays of our homemade sliced turkey breast, mashed potatoes, string beans in garlic &amp; olive oil, stuffing, mac-n-cheese, turkey gravy (quart), cranberry sauce (quart) and a pumpkin pie. <em>No substitutions, please.</em></p>
  </div>
  <p class="note">Prices subject to change. NJ sales tax not included where applicable. 3.5% credit card fee; no fee for cash or check. Fresh turkeys require a deposit. Cooked dishes and sides require non-refundable payment in full when ordered.</p>
  <div class="cta-row"><a class="btn" href="tel:{PHONE_TEL}">Call to order: {PHONE}</a></div>
</section>
""")

TESTIMONIALS = [
 ("Hi Chuck, just wanted to show you how beautiful our 3 rib 9.4 LB Christmas prime rib roast turned out. I have been getting the roast from Drew's for several years & it is always excellent. My sister said this one was especially delicious and the family thoroughly enjoyed it. Thanks for keeping the prime meats prime!!!", "Gail Solimine"),
 ("I wanted to let you know that we were very happy with the food. I can't tell you how many people said it was the best corned beef they've ever had. The rollatini were delicious. I liked that they weren't breaded.", "Victoria"),
 ("Thank you so much for the impeccable service and the delicious food. Our party was a great success and compliments poured in about the food. This from a whole bunch of fussy Italian-Americans! We would call you for another event or recommend you in a heartbeat.", "Nancy C."),
 ("I along with everyone here want to extend a very heartfelt thank you. You never let us down with the quality of food that you send us. The sandwiches were a big hit!! The luncheon meats, tuna and chicken salads and the side salads were so yummy. The bread was so squish fresh that it was a true pleasure eating.", "Joanne L."),
 ("You did it again. Another great graduation party thanks to the delicious food. Only one more to go!", "Coleen P."),
 ("Just wanted to let you know that everyone raved about the food today, especially the chili and the pasta salads. Thanks again for the cookies and chocolate cornucopia – that was a big hit as well.", "Shari B., HR & Facilities Manager, French & Parrello Associates"),
 ("I just wanted to drop you a note and thank you for being so pleasant and accommodating on the phone when I placed my order. The family really appreciated the food in their time of need. Your professionalism and working with their schedule for delivery was something to be proud of.", "Pat K."),
 ("The food was incredible — everyone was raving about it! Thank you for taking care of us on our wedding day.", "Diane Y."),
 ("We ordered food for my sister's bridal shower and everyone loved it! Thank you for such good food and great service!!!!", "Lori M."),
 ("I'm sick with bronchitis, but after going to the doctor Saturday morning, I went straight to Drew's Market to get 5 quarts of chicken soup! My only problem is that my kids are hogging it all! Should've gotten 10!!!", "Lindsay M."),
]
PAGES["testimonials.html"] = ("Testimonials – Drew's Market", "What our customers say about Drew's Market catering, deli and butcher.",
 hero("Testimonials", "Straight from our customers") + '<section class="wrap quotes">' +
 "".join(f"<blockquote><p>“{html.escape(q)}”</p><cite>— {html.escape(w)}</cite></blockquote>" for q, w in TESTIMONIALS) +
 "</section>")

PAGES["faq.html"] = ("FAQ – Drew's Market | Catering, Butcher & Deli", "Answers to common questions about Drew's Market catering, butcher and deli orders.",
 hero("Frequently Asked Questions", "Catering · Butcher · Deli") + f"""
<section class="wrap faq">
  <details open><summary>How are butcher prices calculated?</summary><p>The final price of butcher items is determined by final weight once prepared. Prices are subject to change without notice.</p></details>
  <details><summary>Is a deposit required?</summary><p>Yes — a non-refundable deposit is required for all butcher orders. The final balance, less deposits, is paid at pick-up.</p></details>
  <details><summary>How do I place a catering or holiday order?</summary><p>Call us at <a href="tel:{PHONE_TEL}">{PHONE}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>. Holiday orders fill up quickly, so order early.</p></details>
  <details><summary>Do you deliver?</summary><p>Please call to discuss delivery for your event.</p></details>
  <details><summary>What is your return policy?</summary><p>All sales are final. If you have any issue, contact us right away — as a family-run business we'll do our best to work something out. <a href="returns.html">Read more</a>.</p></details>
  <p class="todo">Owner to review/expand these answers.</p>
</section>
""")

PAGES["contact.html"] = ("Contact – Drew's Market | Spring Lake Heights, NJ", "Call, email or visit Drew's Market at 2407 NJ-71, Spring Lake Heights, NJ.",
 hero("Contact Us", "We're excited to hear from you!") + f"""
<section class="wrap split">
  <div>
    <h2>Get in Touch</h2>
    <p>Whether you have questions about our services, want to plan an event, or simply need more information, please don't hesitate to reach out.</p>
    <p><strong>Call:</strong> <a href="tel:{PHONE_TEL}">{PHONE}</a><br>
       <strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a><br>
       <strong>Visit:</strong> <a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS_1}, {ADDRESS_2}</a></p>
    {cta("Call now")}
  </div>
  <div><h2>Hours</h2><ul class="hours big">{"".join(f"<li><span>{d}</span><span>{t}</span></li>" for d, t in HOURS)}</ul></div>
</section>
""")

PAGES["returns.html"] = ("Return Policy – Drew's Market", "Drew's Market return policy.",
 hero("Return Policy", "") + f"""
<section class="wrap prose"><p>To safeguard our employees and customers, please make your purchases carefully — all sales are final. If you have any issues, please contact us first and immediately. As a family-run business, we will try to accommodate your needs and work something out.</p>{cta("Contact us")}</section>""")

PAGES["privacy.html"] = ("Privacy Policy – Drew's Market", "Drew's Market website privacy policy.",
 hero("Privacy Policy", "") + f"""
<section class="wrap prose">
<p>Drew's Market (“we,” “us”) respects your privacy. This website is informational: it has no user accounts, online checkout, or tracking cookies, and it does not collect personal information on its own.</p>
<p>If you call or email us, we use the information you provide (such as your name, phone number and email) only to respond to you and fulfill your order. We do not sell your information.</p>
<p>Questions? Contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>
<p class="todo">Owner to review before launch.</p>
</section>""")

PAGES["terms.html"] = ("Terms & Conditions – Drew's Market", "Drew's Market website terms and conditions.",
 hero("Terms &amp; Conditions", "") + """
<section class="wrap prose">
<p>This website is operated by FATSOX Inc, dba Drew's Market (“Drew's Market”). These Terms &amp; Conditions apply to your use of this website and its content, including text, images, menus, offers and other information. By accessing the website you agree to these Terms &amp; Conditions. If you object to any of them, please discontinue use of the website.</p>
<p>Menu items, prices and availability are subject to change without notice. Butcher prices are determined by final weight once prepared, and deposits on butcher orders are non-refundable.</p>
<p>You agree not to use the website in any manner that could damage, disable, impair or interfere with it or its host, or transmit any virus or malicious code to it.</p>
<p>Drew's Market may revise these Terms &amp; Conditions from time to time; changes will be posted on this page.</p>
<p class="todo">Owner to review before launch.</p>
</section>""")


def main():
    global img_base
    out = "site"
    if "--preview" in sys.argv:
        img_base = "ARCHIVE"
        out = sys.argv[sys.argv.index("--preview") + 1]
    os.makedirs(out, exist_ok=True)
    for f, (t, d, b) in PAGES.items():
        with open(os.path.join(out, f), "w") as fh:
            fh.write(page(f, t, d, b))
    with open("style.css") as src, open(os.path.join(out, "style.css"), "w") as dst:
        dst.write(src.read())
    print(f"built {len(PAGES)} pages -> {out}")


if __name__ == "__main__":
    main()
