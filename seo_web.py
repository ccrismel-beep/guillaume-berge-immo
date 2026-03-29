#!/usr/bin/env python3
import os, datetime, subprocess
from pathlib import Path

# ─── CONFIG ────────────────────────────────────────────────
GITHUB_USER  = "ccrismel-beep"
GITHUB_REPO  = "guillaume-berge-immo"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_URL   = f"https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{GITHUB_REPO}.git"
PAGES_URL    = f"https://{GITHUB_USER}.github.io/{GITHUB_REPO}/"

NOM          = "Guillaume Berge"
AGENCE       = "Absolute Habitat"
INSTA_URL    = "https://www.instagram.com/guillaume.berge_immo/"
SITE_URL     = "https://www.absolutehabitat.com"
TEL          = "+33782423074"
TEL_DISPLAY  = "07 82 42 30 74"
EMAIL        = "g.berge@absolutehabitat.com"
OG_IMAGE     = "https://www.absolutehabitat.com/og-image.jpg"
BASE_DIR     = Path(__file__).parent
LOG_FILE     = BASE_DIR / f"seo_log_{datetime.date.today()}.log"

def log(msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def sep(t):
    log(f"\n{'='*50}\n  {t}\n{'='*50}")

# ─── MODULE 1 : GÉNÉRATION SITEMAP ─────────────────────────
def generer_sitemap():
    sep("MODULE 1 — GÉNÉRATION SITEMAP")
    today = datetime.date.today().isoformat()
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    oc>{PAGES_URL}</loc>
    astmod>{today}</lastmod>
    hangefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>"""
    path = BASE_DIR / "sitemap.xml"
    path.write_text(sitemap, encoding="utf-8")
    log(f"✅ sitemap.xml généré → {path}")

# ─── MODULE 2 : GÉNÉRATION ROBOTS.TXT ──────────────────────
def generer_robots():
    sep("MODULE 2 — GÉNÉRATION ROBOTS.TXT")
    robots = f"User-agent: *\nAllow: /\n\nSitemap: {PAGES_URL}sitemap.xml\n"
    path = BASE_DIR / "robots.txt"
    path.write_text(robots, encoding="utf-8")
    log(f"✅ robots.txt généré → {path}")

# ─── MODULE 3 : GÉNÉRATION HTML SEO ────────────────────────
def generer_html():
    sep("MODULE 3 — GÉNÉRATION PAGE HTML SEO")
    today = datetime.date.today().isoformat()
    annee = datetime.date.today().year

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{NOM} – Agent Immobilier Le Bouscat &amp; Bordeaux | {AGENCE}</title>
  <meta name="description" content="{NOM}, agent immobilier à Le Bouscat et Bordeaux. Estimation gratuite de votre bien immobilier. Vente, achat avec {AGENCE}. Expert Bordeaux Métropole et Gironde.">
  <meta name="robots" content="index, follow">
  <meta name="author" content="{NOM}">
  <meta name="geo.region" content="FR-NAQ">
  <meta name="geo.placename" content="Le Bouscat, Bordeaux">
  >

  <!-- Open Graph -->
  <meta property="og:type" content="profile">
  <meta property="og:title" content="{NOM} – Agent Immobilier Le Bouscat &amp; Bordeaux">
  <meta property="og:description" content="Estimation gratuite immobilier Le Bouscat. Vente et achat à Bordeaux avec {AGENCE}.">
  <meta property="og:url" content="{PAGES_URL}">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:image" content="{OG_IMAGE}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{NOM} – Agent Immobilier Le Bouscat &amp; Bordeaux">
  <meta name="twitter:description" content="Estimation gratuite immobilier Le Bouscat. Vente et achat à Bordeaux avec {AGENCE}.">
  <meta name="twitter:image" content="{OG_IMAGE}">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "{NOM}",
    "jobTitle": "Agent Immobilier",
    "telephone": "{TEL}",
    "email": "{EMAIL}",
    "url": "{PAGES_URL}",
    "image": "{OG_IMAGE}",
    "sameAs": [
      "{INSTA_URL}",
      "{SITE_URL}"
    ],
    "worksFor": {{
      "@type": "RealEstateAgent",
      "name": "{AGENCE}",
      "url": "{SITE_URL}",
      "telephone": "{TEL}",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "Le Bouscat",
        "addressLocality": "Le Bouscat",
        "postalCode": "33110",
        "addressRegion": "Nouvelle-Aquitaine",
        "addressCountry": "FR"
      }},
      "geo": {{
        "@type": "GeoCoordinates",
        "latitude": 44.8637,
        "longitude": -0.5897
      }},
      "openingHoursSpecification": [{{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
        "opens": "09:00",
        "closes": "19:00"
      }}],
      "areaServed": [
        {{"@type": "City", "name": "Le Bouscat"}},
        {{"@type": "City", "name": "Bordeaux"}},
        {{"@type": "City", "name": "Mérignac"}},
        {{"@type": "City", "name": "Pessac"}},
        {{"@type": "City", "name": "Eysines"}},
        {{"@type": "City", "name": "Bruges"}},
        {{"@type": "AdministrativeArea", "name": "Bordeaux Métropole"}},
        {{"@type": "AdministrativeArea", "name": "Gironde"}}
      ]
    }}
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "Qui est Guillaume Berge, agent immobilier à Le Bouscat ?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Guillaume Berge est agent immobilier à Le Bouscat et Bordeaux, spécialiste de la vente et de l'achat immobilier en Bordeaux Métropole. Il travaille chez Absolute Habitat et propose des estimations gratuites et sans engagement."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Comment obtenir une estimation gratuite à Le Bouscat ?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Guillaume Berge propose des estimations gratuites à Le Bouscat et Bordeaux. Contactez-le via Instagram @guillaume.berge_immo, par email à g.berge@absolutehabitat.com ou sur absolutehabitat.com."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Quelle agence immobilière choisir à Le Bouscat ?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Absolute Habitat avec Guillaume Berge est spécialisée à Le Bouscat. Vente et achat immobilier sur Bordeaux et Bordeaux Métropole avec un accompagnement personnalisé de l'estimation à la signature."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Dans quelles zones intervient Guillaume Berge ?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Guillaume Berge intervient sur Le Bouscat, Bordeaux, Mérignac, Pessac, Eysines, Bruges, Caudéran et l'ensemble de Bordeaux Métropole et de la Gironde."
        }}
      }}
    ]
  }}
  </script>

  <style>
    *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: Arial, sans-serif; background: #f8f9fa; color: #333; line-height: 1.7; }}
    a {{ color: #0f3460; }}
    a:hover {{ opacity: .8; }}

    /* HERO */
    .hero {{ background: linear-gradient(135deg, #1a1a2e, #0f3460); color: white; padding: 60px 20px; text-align: center; }}
    .hero h1 {{ font-size: 2.2em; margin-bottom: 15px; }}
    .hero p {{ font-size: 1.1em; opacity: .9; max-width: 600px; margin: 0 auto 30px; }}
    .btn {{ display: inline-block; background: #e94560; color: white; padding: 14px 38px; border-radius: 50px; text-decoration: none; font-size: 1em; font-weight: 700; margin: 8px; transition: opacity .2s; }}
    .btn:hover {{ opacity: .85; color: white; }}
    .btn-secondary {{ background: white; color: #0f3460; }}
    .btn-secondary:hover {{ color: #0f3460; }}

    /* LAYOUT */
    .container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; }}
    .card {{ background: white; border-radius: 12px; padding: 35px; margin: 25px 0; box-shadow: 0 2px 15px rgba(0,0,0,.08); }}
    h2 {{ color: #0f3460; font-size: 1.5em; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 3px solid #e94560; }}
    h3 {{ color: #0f3460; margin-top: 20px; margin-bottom: 8px; }}

    /* GRID SERVICES */
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 20px; }}
    .item {{ background: #f0f4ff; border-radius: 10px; padding: 20px; border-left: 4px solid #0f3460; }}

    /* ZONES TAGS */
    .tags {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px; }}
    .tag {{ background: #0f3460; color: white; padding: 8px 18px; border-radius: 25px; font-size: .9em; }}

    /* CTA */
    .cta {{ background: linear-gradient(135deg, #0f3460, #1a1a2e); color: white; border-radius: 12px; padding: 40px; text-align: center; margin: 25px 0; }}
    .cta h2 {{ color: white; border-bottom-color: rgba(255,255,255,.3); }}
    .cta p {{ margin: 20px 0; opacity: .9; }}

    /* FOOTER */
    footer {{ text-align: center; padding: 25px; color: #666; font-size: .85em; background: #eee; }}
    footer p + p {{ margin-top: 6px; }}

    @media (max-width: 600px) {{
      .hero h1 {{ font-size: 1.6em; }}
      .btn {{ display: block; margin: 10px auto; max-width: 280px; }}
    }}
  </style>
</head>
<body>

  <section class="hero">
    <h1>{NOM}</h1>
    <p>Agent Immobilier à <strong>Le Bouscat</strong> et <strong>Bordeaux</strong><br>
    Estimation gratuite &bull; Vente &bull; Achat &bull; {AGENCE}</p>
    <a href="{INSTA_URL}" class="btn" rel="noopener noreferrer">Instagram @guillaume.berge_immo</a>
    <a href="{SITE_URL}" class="btn btn-secondary" rel="noopener noreferrer">Site Absolute Habitat</a>
  </section>

  <main class="container" id="main">

    <article class="card">
      <h2>{NOM} – Agent Immobilier Le Bouscat &amp; Bordeaux</h2>
      <p><strong>{NOM}</strong> est agent immobilier spécialisé dans la
