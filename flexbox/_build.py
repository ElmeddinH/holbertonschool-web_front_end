#!/usr/bin/env python3
# Reads existing 1-styles.css and 1-index.html from the repo, then generates
# every remaining Flexbox task file (2-14) cumulatively.

import sys, os

def need(cond, msg):
    if not cond:
        print("ERROR:", msg); sys.exit(1)

need(os.path.exists("1-styles.css"), "1-styles.css not found -- run this inside the flexbox folder")
need(os.path.exists("1-index.html"), "1-index.html not found -- run this inside the flexbox folder")

BASE_CSS = open("1-styles.css").read()
base_index = open("1-index.html").read()

# --- Repair dropped testimonial <cite> tags (cosmetic fix for manual QA) ---
base_index = base_index.replace("5th website!Yuri Y.", "5th website!<cite>Yuri Y.</cite>")
base_index = base_index.replace("is awesome!Dorrie S.", "is awesome!<cite>Dorrie S.</cite>")
base_index = base_index.replace("Techium company.Sven H.", "Techium company.<cite>Sven H.</cite>")

# --- Extract site header + footer (with SVGs) from the homepage for reuse ---
hs = base_index.find('    <header class="header"')
he = base_index.find('</header>') + len('</header>')
SITE_HEADER = base_index[hs:he]
fs = base_index.find('    <footer class="footer"')
fe = base_index.find('</footer>') + len('</footer>')
FOOTER = base_index[fs:fe]
need(SITE_HEADER.strip().startswith('<header class="header"'), "could not extract site header")
need(FOOTER.strip().startswith('<footer class="footer"'), "could not extract footer")

CARD = "/*** 4. CARD ***/"

# ---------------------------------------------------------------------------
# CSS build (cumulative)
# ---------------------------------------------------------------------------
def build_css():
    css = {}
    c = BASE_CSS
    css[2] = c  # placeholder, real 2 built below

    def rep(s, a, b):
        need(a in s, "CSS pattern not found: " + a[:60])
        return s.replace(a, b)

    # Task 2
    latest = ("/* Section Latest news\n    ============================= */\n\n"
              ".section-latest-news .row {\n  flex-direction: row-reverse;\n}\n\n")
    c = rep(c, CARD, latest + CARD); css[2] = c
    # Task 3
    services = ("/* Section SERVICES\n    ============================= */\n\n"
                ".section-services .row {\n  flex-wrap: wrap;\n}\n\n")
    c = rep(c, CARD, services + CARD); css[3] = c
    # Task 4
    c = rep(c, ".col-1-3 {\n  width: 33.33%;\n}", ".col-1-3 {\n  width: calc((100% / 3) - 2rem);\n}")
    c = rep(c, ".col-1-2 {\n  width: 50%;\n}", ".col-1-2 {\n  width: calc((100% / 2) - 2rem);\n}")
    c = rep(c, "[class*='col-'] {\n  padding: 0.5rem;\n}", "[class*='col-'] {\n  margin: 1rem;\n}")
    c = rep(c, "ul.row {\n  margin: 0;\n  padding: 0;\n  list-style: none;\n}",
               "ul.row {\n  margin: -1rem;\n  padding: 0;\n  list-style: none;\n}")
    css[4] = c
    # Task 5
    old_hdr = (".header {\n  padding: var(--header-padding);\n  position: relative;\n"
               "  z-index: 3;\n  background: transparent;\n}\n\n"
               ".header-logo {\n  position: var(--header-logo-position);\n}\n\n"
               ".header-logo a {\n  display: var(--header-logo-link-display);\n"
               "  position: var(--header-logo-link-position);\n  top: var(--header-logo-link-top);\n"
               "  left: var(--header-logo-link-left);\n}")
    new_hdr = (".header {\n  padding: var(--header-padding);\n  position: relative;\n"
               "  z-index: 3;\n  background: transparent;\n}\n\n"
               ".header-container {\n  display: flex;\n  justify-content: space-between;\n}")
    c = rep(c, old_hdr, new_hdr)
    c = rep(c, ".navbar-menu {\n  float: right;\n}\n\n", "")
    c = rep(c, "  --header-logo-position: relative;\n"
               "  --header-logo-link-display: inline-block;\n"
               "  --header-logo-link-position: absolute;\n"
               "  --header-logo-link-top: -1rem;\n"
               "  --header-logo-link-left: 0;\n", "")
    css[5] = c
    # Task 6
    c = rep(c, ".nav {\n  margin: 0;\n  padding: 0;\n  list-style: none;\n  text-align: center;\n}",
               ".nav {\n  display: flex;\n  margin: 0;\n  padding: 0;\n  list-style: none;\n  text-align: center;\n}")
    c = rep(c, ".nav .nav-item {\n  font-family: var(--nav-item-font-family);\n"
               "  font-weight: var(--nav-item-font-weight);\n"
               "  font-size: var(--nav-item-font-size);\n"
               "  letter-spacing: var(--nav-item-letter-spacing);\n"
               "  display: var(--nav-item-display);\n"
               "  margin: var(--nav-item-margin);\n}",
               ".nav .nav-item {\n  font-family: var(--nav-item-font-family);\n"
               "  font-weight: var(--nav-item-font-weight);\n"
               "  font-size: var(--nav-item-font-size);\n"
               "  letter-spacing: var(--nav-item-letter-spacing);\n}\n\n"
               ".nav .nav-item + .nav-item {\n  margin: var(--nav-item-margin);\n}")
    c = rep(c, "--nav-item-margin: 0 2rem 0 0;", "--nav-item-margin: 0 0 0 2rem;")
    css[6] = c
    # Task 7
    c = rep(c, ".header-container {\n  display: flex;\n  justify-content: space-between;\n}",
               ".header-container {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}")
    css[7] = c
    # Task 8
    c = rep(c, ".section-hero .section-inner {\n  padding: 10rem 40rem 2rem 0;\n}",
               ".section-hero .section-inner {\n  display: flex;\n  flex-direction: column;\n"
               "  align-items: flex-start;\n  justify-content: center;\n  min-height: 50vh;\n}")
    css[8] = c
    # Task 9
    aboutus = ("/* Section ABOUT US\n    ============================= */\n\n"
               ".section-about-us [class*='col-'] {\n  align-self: center;\n}\n\n")
    c = rep(c, CARD, aboutus + CARD); css[9] = c
    # Task 10
    c = rep(c, ".section-hero {\n  background-position: 75% 0;\n  background-repeat: no-repeat;\n"
               "  background-size: 90rem auto;\n  background-color: #010101;\n}",
               ".section-hero {\n  position: relative;\n  margin-top: -8.5rem;\n}\n\n"
               ".hero-homepage {\n  background-position: 75% 0;\n  background-repeat: no-repeat;\n"
               "  background-size: 90rem auto;\n  background-color: #010101;\n}\n\n"
               ".section-hero .section-body {\n  padding: 10rem 4rem;\n}\n\n"
               ".section-hero .section-category {\n  color: var(--color-white);\n"
               "  text-transform: uppercase;\n}")
    css[10] = c
    # Task 11
    c = c + ("\n/*** ARTICLE PAGE ***/\n"
             "/* Section HERO (article)\n    ============================= */\n\n"
             ".hero-article {\n  background-size: 150rem 100rem;\n  background-position: 50% 0;\n}\n\n"
             ".hero-article::before {\n  content: '';\n  background: rgba(0, 0, 0, 0.8);\n"
             "  position: absolute;\n  top: 0;\n  right: 0;\n  left: 0;\n  bottom: 0;\n  z-index: 0;\n}\n\n"
             ".hero-article .section-inner {\n  text-align: center;\n  align-items: center;\n  min-height: 40vh;\n}\n\n"
             ".hero-article .section-body {\n  position: relative;\n  padding: 7rem 0 0;\n  z-index: 2;\n}\n")
    css[11] = c
    # Task 12
    c = c + ("\n/* Main article\n    ============================= */\n\n"
             ".main-article {\n  padding: 5rem 0;\n}\n\n"
             "/* Post\n    ============================= */\n\n"
             ".post {\n  display: flex;\n}\n\n"
             ".post-content {\n  width: 100%;\n}\n\n"
             ".post-aside {\n  order: -1;\n  min-width: 20%;\n}\n")
    css[12] = c
    # Task 13
    c = c + ("\n/* Post Meta\n    ============================= */\n\n"
             ".post-meta-list {\n  flex-direction: column;\n}\n\n"
             ".post-meta-list strong {\n  color: var(--color-primary);\n"
             "  font-size: var(--font-size-small);\n  text-transform: uppercase;\n  display: block;\n}\n\n"
             ".post-meta-list [class*='post-meta-'] {\n  margin-bottom: 1rem;\n"
             "  padding-bottom: 1rem;\n  border-bottom: 0.2rem solid var(--color-light-grey);\n}\n\n"
             ".post-meta-list [class*='post-meta']:last-child {\n  border: none;\n  margin-bottom: 3rem;\n}\n\n"
             "/* Tag list\n    ============================= */\n\n"
             ".tag-list {\n  padding: 0;\n  list-style: none;\n}\n\n"
             ".tag-list li {\n  display: inline;\n}\n\n"
             '.tag-list li::after {\n  content: ", ";\n}\n\n'
             ".tag-list li:last-child::after {\n  content: '';\n}\n")
    css[13] = c
    # Task 14
    css[14] = c
    return css

# ---------------------------------------------------------------------------
# INDEX build (cumulative)
# ---------------------------------------------------------------------------
SERVICES_TWO_UL = '''            <ul class="row">
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">Design & Concept</a></h3></div></li>
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">Digital Strategy</a></h3></div></li>
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">Content Strategy</a></h3></div></li>
            </ul>
            <ul class="row">
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">UX Design</a></h3></div></li>
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">Web Development</a></h3></div></li>
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">Social Media</a></h3></div></li>
            </ul>'''

SERVICES_ONE_UL = '''            <ul class="row">
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">Design & Concept</a></h3></div></li>
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">Digital Strategy</a></h3></div></li>
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">Content Strategy</a></h3></div></li>
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">UX Design</a></h3></div></li>
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">Web Development</a></h3></div></li>
              <li class="col-1-3"><div class="card-services"><h3 class="card-title"><a href="#">Social Media</a></h3></div></li>
            </ul>'''

HEADER_WRAP_OLD = '''      <div class="container">
        <div class="header-logo">
          <a href="#">
            <img src="images/logo-white.png" alt="Techium logo" width="160" height="40">
          </a>
        </div>
        <nav class="navbar-menu">
          <ul class="nav">
            <li class="nav-item"><a href="#" class="nav-link">Home</a></li>
            <li class="nav-item"><a href="#services" class="nav-link">Services</a></li>
            <li class="nav-item"><a href="#works" class="nav-link">Works</a></li>
            <li class="nav-item"><a href="#about" class="nav-link">About</a></li>
            <li class="nav-item"><a href="#latest_news" class="nav-link">Latest news</a></li>
            <li class="nav-item"><a href="#testimonials" class="nav-link">Testimonials</a></li>
            <li class="nav-item"><a href="#contact" class="nav-link">Contact</a></li>
          </ul>
        </nav>
      </div>'''

HEADER_WRAP_NEW = '''      <div class="container">
        <div class="header-container">
          <div class="header-logo">
            <a href="#">
              <img src="images/logo-white.png" alt="Techium logo" width="160" height="40">
            </a>
          </div>
          <nav class="navbar-menu">
            <ul class="nav">
              <li class="nav-item"><a href="#" class="nav-link">Home</a></li>
              <li class="nav-item"><a href="#services" class="nav-link">Services</a></li>
              <li class="nav-item"><a href="#works" class="nav-link">Works</a></li>
              <li class="nav-item"><a href="#about" class="nav-link">About</a></li>
              <li class="nav-item"><a href="#latest_news" class="nav-link">Latest news</a></li>
              <li class="nav-item"><a href="#testimonials" class="nav-link">Testimonials</a></li>
              <li class="nav-item"><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
          </nav>
        </div>
      </div>'''

def build_index(n, merge=False, wrap=False):
    h = base_index.replace('href="1-styles.css"', 'href="%d-styles.css"' % n)
    need(('%d-styles.css' % n) in h, "index link not updated for task %d" % n)
    if merge:
        need(SERVICES_TWO_UL in h, "services two-ul block not found (task %d)" % n)
        h = h.replace(SERVICES_TWO_UL, SERVICES_ONE_UL)
    if wrap:
        need(HEADER_WRAP_OLD in h, "header block to wrap not found (task %d)" % n)
        h = h.replace(HEADER_WRAP_OLD, HEADER_WRAP_NEW)
    return h

# ---------------------------------------------------------------------------
# ARTICLE build (cumulative)  -- reuses extracted SITE_HEADER + FOOTER
# ---------------------------------------------------------------------------
ARTICLE_HEADER = SITE_HEADER.replace(HEADER_WRAP_OLD, HEADER_WRAP_NEW) if HEADER_WRAP_OLD in SITE_HEADER else SITE_HEADER

def article_base(n):
    return ('''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
    <title>Article - Techium</title>
    <meta name="description" content="Description of the page less than 150 characters">
    <link rel="icon" type="image/png" href="images/favicon.jpg">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Raleway:700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="''' + str(n) + '''-styles.css">
  </head>
  <body>
    <!-- Header -->
''' + ARTICLE_HEADER + '''
    <!-- Main -->
    <main>
      <!-- Hero section -->
      <header class="section-hero" data-section-theme="dark">
        <div class="container">
          <div class="section-body">
            <section class="section-inner">
            </section>
          </div>
        </div>
      </header>
    </main>
    <!-- Footer -->
''' + FOOTER + '''
  </body>
</html>
''')

HERO_OLD = '''      <header class="section-hero" data-section-theme="dark">
        <div class="container">
          <div class="section-body">
            <section class="section-inner">
            </section>
          </div>
        </div>
      </header>'''

HERO_NEW = '''      <header class="section-hero hero-article" data-section-theme="dark" style="background-image: url('images/pic-article-02.jpg');">
        <div class="container">
          <div class="section-body">
            <section class="section-inner">
              <span class="section-category">Digital Life</span>
              <h1 class="section-title">Ut alios omittam, hunc appello, quem ille unum secutus est</h1>
            </section>
          </div>
        </div>
      </header>'''

MAIN_ARTICLE = '''
      <div class="main-article">
        <div class="container">
          <div class="post">
            <article class="post-content"></article>
            <!-- Aside section -->
            <aside class="post-aside">
              <div class="post-meta"></div>
              <div class="post-share"></div>
            </aside>
          </div>
        </div>
      </div>'''

POST_META_FILLED = '''<div class="post-meta">
                <ul class="post-meta-list row">
                  <li class="post-meta-author">
                    <strong>Written by:</strong>
                    <a href="#" rel="author">William Attaway</a>
                  </li>
                  <li class="post-meta-date">
                    <strong>Posted on:</strong>
                    <time datetime="2019-10">October 2019</time>
                  </li>
                  <li class="post-meta-tag">
                    <strong>Tags:</strong>
                    <ul class="tag-list">
                      <li><a href="#" rel="tag">Web Design</a></li>
                      <li><a href="#" rel="tag">UX</a></li>
                    </ul>
                  </li>
                </ul>
              </div>'''

def social_two(fb_tw_source):
    # Build a Facebook+Twitter share list (no Instagram, href="#") reusing the
    # SVGs already present in the extracted footer.
    import re
    # grab first two <svg>...</svg> blocks from footer
    svgs = re.findall(r'<svg .*?</svg>', fb_tw_source, re.S)
    need(len(svgs) >= 2, "could not find Facebook/Twitter SVG in footer")
    fb, tw = svgs[0], svgs[1]
    return ('<div class="post-share">\n'
            '                <ul class="social nav">\n'
            '                  <li class="social-item nav-item"><a href="#" class="social-link">' + fb + '</a></li>\n'
            '                  <li class="social-item nav-item"><a href="#" class="social-link">' + tw + '</a></li>\n'
            '                </ul>\n'
            '              </div>')

def build_article(n, hero=False, main=False, meta=False, share=False):
    h = article_base(n)
    if hero:
        need(HERO_OLD in h, "article hero block not found (task %d)" % n)
        h = h.replace(HERO_OLD, HERO_NEW)
    if main:
        need("      </header>\n    </main>" in h, "main hero close not found (task %d)" % n)
        h = h.replace("      </header>\n    </main>", "      </header>" + MAIN_ARTICLE + "\n    </main>")
    if meta:
        need('<div class="post-meta"></div>' in h, "empty post-meta not found (task %d)" % n)
        h = h.replace('<div class="post-meta"></div>', POST_META_FILLED)
    if share:
        need('<div class="post-share"></div>' in h, "empty post-share not found (task %d)" % n)
        h = h.replace('<div class="post-share"></div>', social_two(FOOTER))
    return h

# ---------------------------------------------------------------------------
def w(path, content):
    if not content.endswith("\n"):
        content += "\n"
    open(path, "w").write(content)

css = build_css()
for n in range(2, 15):
    w("%d-styles.css" % n, css[n])

w("2-index.html", build_index(2))
w("3-index.html", build_index(3, merge=True))
w("4-index.html", build_index(4, merge=True))
w("5-index.html", build_index(5, merge=True, wrap=True))
w("6-index.html", build_index(6, merge=True, wrap=True))
w("7-index.html", build_index(7, merge=True, wrap=True))
w("8-index.html", build_index(8, merge=True, wrap=True))
w("9-index.html", build_index(9, merge=True, wrap=True))
w("10-article.html", build_article(10))
w("11-article.html", build_article(11, hero=True))
w("12-article.html", build_article(12, hero=True, main=True))
w("13-article.html", build_article(13, hero=True, main=True, meta=True))
w("14-article.html", build_article(14, hero=True, main=True, meta=True, share=True))

# also repair the already-pushed 1-index.html cites in place
w("1-index.html", base_index)

print("Done: generated tasks 2-14 (and repaired 1-index.html cites).")
