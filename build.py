#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates every HTML page of the portfolio from shared header/footer
partials + per-page content, so markup stays consistent across pages."""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

LINKEDIN = "https://www.linkedin.com/in/giulia-la-paglia-03b08a221/"
EMAIL = "mail.giulia.lapaglia@gmail.com"

LINKEDIN_SVG = '''<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.11 1 2.48 1 4.98 2.12 4.98 3.5zM.5 8.25h4V23h-4V8.25zM8.5 8.25h3.83v2.01h.05c.53-1 1.84-2.06 3.79-2.06 4.05 0 4.8 2.67 4.8 6.14V23h-4v-6.75c0-1.61-.03-3.68-2.24-3.68-2.25 0-2.6 1.76-2.6 3.56V23h-4V8.25z"/></svg>'''

ASTERISK_SVG = '''<svg class="ast ast--spin" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M12 2v20M4 7l16 10M20 7L4 17"/></svg>'''


def nav(depth, active):
    """depth: '' for root pages, '../' for pages inside /projects/"""
    home = f"{depth}index.html"
    cv = f"{depth}curriculum.html"
    projects = f"{home}#work"
    contacts = f"{home}#contacts"
    links = [
        ("home", home, "Home"),
        ("curriculum", cv, "Curriculum"),
        ("projects", projects, "Projects"),
        ("contacts", contacts, "Contacts"),
    ]
    items = []
    for key, href, label in links:
        current = ' aria-current="page"' if key == active else ""
        items.append(f'<a href="{href}"{current}>{label}</a>')
    return "\n        ".join(items)


def header(depth, active):
    return f"""  <header class="site-header">
    <div class="container">
      <a class="brand" href="{depth}index.html">Giulia La Paglia</a>
      <nav class="nav-links">
        {nav(depth, active)}
      </nav>
      <div class="nav-social">
        <a class="icon-btn" href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{LINKEDIN_SVG}</a>
      </div>
      <button class="nav-toggle" aria-label="Apri il menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>"""


def footer(depth):
    return f"""  <footer class="site-footer">
    <div class="container">
      <span>&copy; 2025 Giulia La Paglia. All rights reserved.</span>
      <nav>
        <a href="{depth}index.html">Home</a>
        <a href="{depth}curriculum.html">Curriculum</a>
      </nav>
      <a class="icon-btn" href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{LINKEDIN_SVG}</a>
    </div>
  </footer>"""


def contact_section(depth):
    return f"""  <section class="contact section" id="contacts">
    <div class="container">
      <span class="eyebrow"><span class="ast">*</span> Get in touch</span>
      <h2 class="contact__title">Let&rsquo;s create<br>something together.</h2>
      <a class="contact__email" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </section>"""


def page_shell(title, description, depth, active, body):
    fonts = '''<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,500;1,9..144,600&family=Space+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">'''
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  {fonts}
  <link rel="stylesheet" href="{depth}css/style.css">
</head>
<body>
{header(depth, active)}
{body}
{footer(depth)}
  <script src="{depth}js/script.js"></script>
</body>
</html>
"""


# =========================================================
# Home page
# =========================================================
ROLES = ["Web Designer", "Graphic Designer", "UI/UX Designer", "Event Designer", "Product Designer"]
CATEGORIES = ["UI/UX Design", "Web Design", "Graphic Design", "Event Design", "Product Design"]

PROJECTS = [
    dict(
        title="Fairly Tails",
        cat="Product Design",
        cat_class="product",
        slug="fairly-tails",
        img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e859b0b2771ec9c42e0c_FairlyTales-scatole-tutti.webp",
    ),
    dict(
        title="Genova Matsuri",
        cat="Event Design",
        cat_class="event",
        slug="genova-matsuri",
        img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e7a0033d31229b378980_Brochure%20copia.webp",
    ),
    dict(
        title="CurriCraft",
        cat="Web Design",
        cat_class="web",
        slug="curricraft",
        img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e89d6c7acfa242c7a69a_WebDesign_1.webp",
    ),
    dict(
        title="Ringo Tropicale",
        cat="Graphic Design",
        cat_class="graphic",
        slug="ringo-tropicale",
        img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8bed2100cf06d593ebe_cerchio%20mano.webp",
    ),
    dict(
        title="Iconography and Iconology",
        cat="Editorial Design",
        cat_class="editorial",
        slug="iconography-and-iconology",
        img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e913bcde832dc28edf3b_StoriaSocialeArte_2.webp",
    ),
]


def marquee(words, reverse=False):
    group = "".join(f"<span>{w}</span><span class=\"ast\">*</span>" for w in words)
    rev = " marquee--reverse" if reverse else ""
    return f"""  <div class="marquee{rev}">
    <div class="marquee__track">
      <div class="marquee__group">{group}</div>
      <div class="marquee__group" aria-hidden="true">{group}</div>
    </div>
  </div>"""


def build_home():
    rotator_spans = "\n          ".join(
        f'<span class="is-active">{r}</span>' if i == 0 else f"<span>{r}</span>"
        for i, r in enumerate(ROLES)
    )
    project_cards = "\n".join(
        f"""        <a class="p-card" href="projects/{p['slug']}.html">
          <div class="p-card__frame">
            <img src="{p['img']}" alt="{p['title']} &mdash; anteprima progetto" loading="lazy">
            <span class="p-card__view">View</span>
          </div>
          <div class="p-card__meta">
            <span class="p-card__title">{p['title']}</span>
            <span class="p-card__cat cat--{p['cat_class']}">{p['cat']}</span>
          </div>
        </a>"""
        for p in PROJECTS
    )

    body = f"""  <section class="hero">
    <div class="container">
      <p class="hero__kicker">Ciao, sono Giulia &mdash;</p>
      <h1 class="hero__title">I am a <span class="hero__rotator">{rotator_spans}</span></h1>
      <div class="hero__foot">
        <div class="hero__tags">
          <span class="tag">Genoa, Italy</span>
          <span class="tag">Product &amp; Event Design, Genoa Univ.</span>
          <span class="tag">Front-End Developer course, Talentform</span>
        </div>
        <a class="btn" href="curriculum.html">View my curriculum</a>
      </div>
    </div>
  </section>

{marquee(CATEGORIES)}

  <section class="section section--rule quote">
    <div class="container">
      <span class="quote__mark">&ldquo;</span>
      <p class="quote__text">Creativity is intelligence having fun.</p>
      <span class="quote__cite">&mdash; Albert Einstein</span>
    </div>
  </section>

{marquee(["Projects"] * 6, reverse=True)}

  <section class="section" id="work">
    <div class="container">
      <div class="section__head">
        <h2 class="section__title">Selected work</h2>
        <span class="eyebrow"><span class="ast">*</span> Five disciplines, one process</span>
      </div>
      <div class="grid-projects">
{project_cards}
      </div>
    </div>
  </section>

{contact_section('')}"""

    html = page_shell(
        "Giulia La Paglia &mdash; Portfolio",
        "Portfolio di Giulia La Paglia: Web, Graphic, UI/UX, Event e Product Designer.",
        "", "home", body,
    )
    write("index.html", html)


# =========================================================
# Curriculum page
# =========================================================
WORK = [
    ("Apr 2025 &mdash; Today", "Web Designer", "Officine IADR &mdash; TheMeter, Genoa, Italy"),
    ("Oct 2024 &mdash; Apr 2025", "Internship in Web Design", "Officine IADR &mdash; TheMeter, Genoa, Italy"),
    ("Apr &mdash; Jul 2024", "Graphic Designer", "Centro Servizi S.E.F. srl, Rapallo (GE), Italy"),
    ("Mar &mdash; Apr 2021", "Internship in Graphic Design", "Centro Servizi S.E.F. srl, Rapallo (GE), Italy"),
]

EDUCATION = [
    ("Feb &mdash; Apr 2024", "Theoretical and Practical Course, Front End Developer", "Talentform"),
    ("Sep 2021 &mdash; Dec 2023", "Master&rsquo;s Degree, Product and Event Design", "University of Genoa &mdash; grade 109/110"),
    ("Sep 2018 &mdash; Oct 2021", "Bachelor&rsquo;s Degree, Product and Nautical Design", "Major in Product and Communication &mdash; University of Genoa &mdash; grade 105/110"),
    ("Sep 2013 &mdash; Jul 2018", "Linguistic High School Diploma", "Da Vigo Nicoloso, Rapallo (GE), Italy"),
]

SKILLS_GROUPS = [
    ("Design &amp; multimedia", ["Adobe Photoshop, Illustrator, InDesign", "Premiere Pro, After Effects, XD", "Figma", "Canva", "Microsoft Office"]),
    ("CAD software", ["Rhinoceros 3D", "AutoCAD 2D"]),
    ("Web development", ["HTML5, CSS3, JavaScript", "Bootstrap 5", "WordPress", "Webflow"]),
    ("Soft skills", ["Listening &amp; understanding diverse perspectives", "Effective collaboration in team settings", "Creativity in seeking innovative solutions", "Adaptability to change"]),
    ("Languages", ["Italian &mdash; native", "English &mdash; B2", "French &mdash; B1", "Spanish &mdash; B1", "Japanese &mdash; beginner"]),
    ("Hobbies &amp; other", ["Japanese culture", "Photography", "Traveling", "Sports", "Music"]),
]


def timeline(rows):
    return "\n".join(
        f"""        <div class="t-row">
          <time>{d}</time>
          <div><h3>{role}</h3><p>{place}</p></div>
        </div>"""
        for d, role, place in rows
    )


def build_curriculum():
    skills_cards = "\n".join(
        f"""        <div class="skill-card">
          <h3>{name}</h3>
          <ul>{''.join(f'<li>{item}</li>' for item in items)}</ul>
        </div>"""
        for name, items in SKILLS_GROUPS
    )

    body = f"""  <section class="p-hero">
    <div class="container">
      <span class="eyebrow"><span class="ast">*</span> Curriculum</span>
      <h1 class="p-hero__title">Experience, education<br>&amp; skills.</h1>
    </div>
  </section>

  <section class="section section--rule">
    <div class="container cv-block">
      <div class="section__head">
        <h2 class="section__title">Work experience</h2>
      </div>
      <div class="timeline">
{timeline(WORK)}
      </div>
    </div>
  </section>

  <section class="section section--rule">
    <div class="container cv-block">
      <div class="section__head">
        <h2 class="section__title">Education</h2>
      </div>
      <div class="timeline">
{timeline(EDUCATION)}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container cv-block">
      <div class="section__head">
        <h2 class="section__title">Skills</h2>
      </div>
      <div class="skill-grid">
{skills_cards}
      </div>
    </div>
  </section>

{contact_section('')}"""

    html = page_shell(
        "Curriculum &mdash; Giulia La Paglia",
        "Curriculum di Giulia La Paglia: esperienza, formazione e competenze.",
        "", "curriculum", body,
    )
    write("curriculum.html", html)


# =========================================================
# Project detail pages
# =========================================================
PROJECT_DETAILS = {
    "fairly-tails": dict(
        title="Fairly Tails",
        cat="Product Design",
        skills=["Ergonomics", "Material selection", "Brand identity", "Packaging"],
        tools=["Rhinoceros 3D", "Adobe Illustrator"],
        intro=[
            "Fairly Tails consists in the design of a series of tablets for children. These are true three-dimensional pages that narrate stories typical of different countries, featuring raised illustrations and descriptions in Braille.",
            "The idea creatively stems from the desire to make fairy tales from around the world accessible to visually impaired and blind children.",
        ],
        hero_img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e859b0b2771ec9c42e0c_FairlyTales-scatole-tutti.webp",
        pull="Children can actively and easily learn Braille by listening to audio files that read the text of the stories, provided as additional non-visual supports.",
        body=[
            "The raised illustrations also feature different textures to enhance the tactile experience.",
            "Each series is crafted with a specific colour, and the tablets are numbered in Braille, featuring raised illustrations and the text of the story.",
        ],
        mid_img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e95cd3e99c19b99658ee_FairlyTales-render.webp",
        gallery=[
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e85d81cb6e274e672714_Giappone_il%20matrimonio%20della%20topolina_rosa.webp",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e85e7462d1ffa5207efc_Danimarca_il%20principe%20biancorso_viola.webp",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e85ece8f7179fe785467_India_la%20volpe%20e%20il%20bramino_verde.webp",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e85dbd05c4ec28ea1949_Nord%20America_come%20il%20coyote%20rub%C3%B2%20il%20fuoco_verdeacqua.webp",
        ],
        next="genova-matsuri",
    ),
    "genova-matsuri": dict(
        title="Genova Matsuri",
        cat="Event Design",
        skills=["Organization of the festival", "Set-up", "Brand identity", "Social media campaign"],
        tools=["Adobe InDesign", "Adobe Photoshop", "Instagram"],
        intro=[
            "Genova Matsuri is a project for the realization of a festival based on three Japanese holidays: Hinamatsuri, Hanami, and Kodomo no Hi.",
            "Commissioned by the E. Chiossone Museum of Oriental Art, the event will take place in spring 2024 at Villetta Di Negro in Genoa.",
        ],
        hero_img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e7a0033d31229b378980_Brochure%20copia.webp",
        pull="During the three days of the festival, both free activities and paid creative workshops are planned, thanks to the involvement of local artisans and cultural associations.",
        body=[
            "To accompany the project, a communication campaign through social media channels has been conceived.",
            "The event&rsquo;s graphics are based on works exhibited in the museum, bringing to life characters and atmospheres that evoke the three Japanese holidays.",
        ],
        mid_img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e87773645b7c8c21e319_mockup%20social.webp",
        gallery=[
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8827462d1ffa520915e_ambiente01.webp",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f252ff/6846ef46b03ef850db46422c_02-image-gallery-our-team-brix-agency.jpg",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8821b9ff789277216b9_Tavola%20da%20disegno%202.webp",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f252ff/6846ef46b03ef850db464222_04-image-gallery-our-team-brix-agency.jpg",
        ],
        next="curricraft",
    ),
    "curricraft": dict(
        title="CurriCraft",
        cat="Web Design",
        skills=["UI Design", "UX Design", "Collaboration with developers"],
        tools=["Figma", "Adobe Illustrator"],
        intro=[
            "CurriCraft is a web design project aimed at simplifying the process of creating online resumes.",
            "Users are guided through a series of targeted questions that help in crafting their curriculum vitae, which will then be uploaded to their profiles.",
        ],
        hero_img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e89d6c7acfa242c7a69a_WebDesign_1.webp",
        pull="The created resumes are accessible to all users, creating an inclusive environment where potential employers or collaborators can search for profiles that meet their needs.",
        body=[
            "The design of this project stands out for its simplicity, intuitiveness, and freshness.",
            "No complications, just a smart design that makes the user experience a true pleasure.",
        ],
        mid_img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8a26f6a051ed0ddf3c4_WebDesign_2.webp",
        gallery=[
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e92bd847827794eaaa0e_WebDesign-pagine.webp",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f252ff/6846ef46b03ef850db46422c_02-image-gallery-our-team-brix-agency.jpg",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f252ff/6846ef46b03ef850db464227_03-image-gallery-our-team-brix-agency.jpg",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f252ff/6846ef46b03ef850db464222_04-image-gallery-our-team-brix-agency.jpg",
        ],
        next="ringo-tropicale",
    ),
    "ringo-tropicale": dict(
        title="Ringo Tropicale",
        cat="Graphic Design",
        skills=["Concept Design", "Benchmarking", "Packaging", "Visual communication"],
        tools=["Adobe Illustrator"],
        intro=[
            "On the request of the Italian multinational Barilla, a new food product with innovative and sustainable packaging has been conceived.",
            "Ringo Tropicale is a limited edition that combines the goodness of Ringo biscuits with the freshness of summer.",
        ],
        hero_img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8bed2100cf06d593ebe_cerchio%20mano.webp",
        pull="The key concept of this project is sharing. The segmented opening encourages group consumption, allowing individuals to access the desired quantity of the product.",
        body=[
            "Mini vanilla-flavoured biscuits, featuring the graphics of the compass rose; and cocoa-flavoured ones, marked by a tropical island.",
            "Both versions are coated with icing and filled with fruit cream.",
        ],
        mid_img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8cecda1f1354fb723e1_RingoTropicale_gusti.webp",
        gallery=[
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8d80f8bfcfce79386ef_cerchio%20aprendo.webp",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f252ff/6846ef46b03ef850db46422c_02-image-gallery-our-team-brix-agency.jpg",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e8d8c403085c1a9b3e16_cerchio%20render%20finale.webp",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f252ff/6846ef46b03ef850db464222_04-image-gallery-our-team-brix-agency.jpg",
        ],
        next="iconography-and-iconology",
    ),
    "iconography-and-iconology": dict(
        title="Iconography and Iconology",
        subtitle="A Visual Synthesis in the Social History of Art",
        cat="Editorial Design",
        skills=["Iconography and iconology", "Editorial research", "Typography", "Layout"],
        tools=["Adobe InDesign", "Adobe Photoshop"],
        intro=[
            "&ldquo;Iconography and Iconology. A Visual Synthesis in the Social History of Art.&rdquo;",
            "This book focuses on the distinction between iconography and iconology, exploring their historical developments through a timeline.",
        ],
        hero_img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e913bcde832dc28edf3b_StoriaSocialeArte_2.webp",
        pull="The book is presented through an editorial design project, with a focus on research, typography, and layout.",
        body=[
            "This attention to detail provides a clear immersion into the complexity of art.",
        ],
        mid_img="https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e91a4e6eeb8778232b58_StoriaSocialeArte_6.webp",
        gallery=[
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f2531e/6846e9227d0b7c41c3e59d90_StoriaSocialeArte_1.webp",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f252ff/6846ef46b03ef850db46422c_02-image-gallery-our-team-brix-agency.jpg",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f252ff/6846ef46b03ef850db464227_03-image-gallery-our-team-brix-agency.jpg",
            "https://cdn.prod.website-files.com/6845ecf9d61fca0679f252ff/6846ef46b03ef850db464222_04-image-gallery-our-team-brix-agency.jpg",
        ],
        next="fairly-tails",
    ),
}

CAT_CLASS = {
    "Product Design": "product",
    "Event Design": "event",
    "Web Design": "web",
    "Graphic Design": "graphic",
    "Editorial Design": "editorial",
}


def build_project(slug, p):
    intro_html = "\n            ".join(f"<p>{para}</p>" for para in p["intro"])
    body_html = "\n            ".join(f"<p>{para}</p>" for para in p["body"])
    skills_html = "".join(f"<li>{s}</li>" for s in p["skills"])
    tools_html = "".join(f"<li>{t}</li>" for t in p["tools"])
    gallery_html = "\n        ".join(
        f'<img src="{g}" alt="{p["title"]} &mdash; galleria {i+1}" loading="lazy">'
        for i, g in enumerate(p["gallery"])
    )
    next_title = PROJECT_DETAILS[p["next"]]["title"]
    subtitle = f'<br><span style="font-size:0.55em;">{p["subtitle"]}</span>' if p.get("subtitle") else ""

    body = f"""  <section class="p-hero">
    <div class="container">
      <span class="eyebrow"><span class="ast">*</span> {p['cat']}</span>
      <h1 class="p-hero__title">{p['title']}{subtitle}</h1>
      <div class="p-meta">
        <div>
          <h3>Skills</h3>
          <ul>{skills_html}</ul>
        </div>
        <div>
          <h3>Tools</h3>
          <ul>{tools_html}</ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <figure class="p-figure">
        <img src="{p['hero_img']}" alt="{p['title']} &mdash; immagine principale" loading="lazy">
      </figure>
    </div>
  </section>

  <section class="section section--rule">
    <div class="container">
      <div class="p-copy">
        <p class="p-quote">{p['pull']}</p>
        {intro_html}
        {body_html}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <figure class="p-figure">
        <img src="{p['mid_img']}" alt="{p['title']} &mdash; immagine di dettaglio" loading="lazy">
      </figure>
    </div>
  </section>

  <section class="section section--rule">
    <div class="container">
      <span class="eyebrow"><span class="ast">*</span> Gallery</span>
      <div class="gallery" style="margin-top:1.5rem;">
        {gallery_html}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container p-nav">
      <a class="btn btn--ghost" href="../index.html#work">&larr; All projects</a>
      <a class="btn" href="{p['next']}.html">Next project: {next_title} &rarr;</a>
    </div>
  </section>

{contact_section('../')}"""

    html = page_shell(
        f"{p['title']} &mdash; Giulia La Paglia",
        f"{p['title']}, {p['cat']} project by Giulia La Paglia.",
        "../", "projects", body,
    )
    write(f"projects/{slug}.html", html)


def write(rel_path, content):
    full = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel_path)


if __name__ == "__main__":
    build_home()
    build_curriculum()
    for slug, data in PROJECT_DETAILS.items():
        build_project(slug, data)
    print("done")
