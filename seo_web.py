#!/usr/bin/env python3
import os
import datetime
from pathlib import Path

GITHUB_USER = "ccrismel-beep"
GITHUB_REPO = "guillaume-berge-immo"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
PAGES_URL = f"https://{GITHUB_USER}.github.io/{GITHUB_REPO}/"

NOM = "Guillaume Berge"
AGENCE = "Absolute Habitat"
INSTA_URL = "https://www.instagram.com/guillaume.berge_immo/"
SITE_URL = "https://www.absolutehabitat.com"

BASE_DIR = Path(__file__).parent
LOG_FILE = BASE_DIR / f"seo_log_{datetime.date.today()}.log"
INDEX_FILE = BASE_DIR / "index.html"
ROBOTS_FILE = BASE_DIR / "robots.txt"
SITEMAP_FILE = BASE_DIR / "sitemap.xml"

KEYWORDS = [
    "Guillaume Berge Agent Immobilier Bordeaux",
    "Agent Immobilier Le Bouscat",
    "Estimation gratuite immobilier Le Bouscat",
    "Absolute Habitat Bordeaux",
    "Vente achat immobilier Bordeaux Le Bouscat",
    "Agent immobilier Gironde",
    "Estimation immobiliere gratuite Bordeaux",
    "Immobilier Le Bouscat 33110",
]

def log(msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def sep(title):
    log("")
    log("=" * 50)
    log(f"  {title}")
    log("=" * 50)

def generer_html():
    sep("MODULE 1 - GENERATION PAGE HTML SEO")
    annee = datetime.date.today().year
    kw_str = ", ".join(KEYWORDS)

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{NOM} - Agent Immobilier Le Bouscat Bordeaux | {AGENCE}</title>
  <meta name="description" content="{NOM}, agent immobilier sur Le Bouscat et Bordeaux. Estimation gratuite de votre bien immobilier. Vente et achat avec {AGENCE}. Expert immobilier Bordeaux Metropole et Gironde.">
  <meta name="keywords" content="{kw_str}">
  <meta name="robots" content="index, follow">
  <meta name="author" content="{NOM}">
  <meta name="geo.region" content="FR-NAQ">
  <meta name="geo.placename" content="Le Bouscat, Bordeaux">
  <meta property="og:type" content="profile">
  <meta property="og:title" content="{NOM} - Agent Immobilier Le Bouscat Bordeaux">
  <meta property="og:description" content="Estimation gratuite immobilier Le Bouscat. Vente et achat a Bordeaux avec {AGENCE}.">
  <meta property="og:url" content="{PAGES_URL}">
  <meta property="og:locale" content="fr_FR">
  <link rel="canonical" href="{PAGES_URL}">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "RealEstateAgent",
    "name": "{NOM}",
    "jobTitle": "Agent Immobilier",
    "description": "Agent immobilier spécialise dans la vente et achat de biens sur  Le Bouscat, Bordeaux et Bordeaux Metropole. Estimation gratuite offerte.",
    "url": "{PAGES_URL}",
    "sameAs": ["{INSTA_URL}", "{SITE_URL}"],
    "worksFor": {{
      "@type": "RealEstateAgent",
      "name": "{AGENCE}",
      "url": "{SITE_URL}",
      "address": {{
        "@type": "PostalAddress",
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
      "openingHoursSpecification": [
        {{
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "09:00",
          "closes": "19:00"
        }}
      ]
    }},
    "areaServed": [
      {{"@type": "City", "name": "Le Bouscat"}},
      {{"@type": "City", "name": "Bordeaux"}},
      {{"@type": "AdministrativeArea", "name": "Bordeaux Metropole"}},
      {{"@type": "AdministrativeArea", "name": "Gironde"}}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "Qui est Guillaume Berge agent immobilier sur Le Bouscat ?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Guillaume Berge est agent immobilier sur Le Bouscat et Bordeaux, specialiste de la vente et achat immobilier en Bordeaux Metropole. Il travaille chez Absolute Habitat et propose des estimations gratuites."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Comment obtenir une estimation gratuite sur Le Bouscat ?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Guillaume Berge propose des estimations gratuites sur Le Bouscat et Bordeaux. Contactez-le via Instagram @guillaume.berge_immo ou sur absolutehabitat.com."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Quelle agence immobiliere choisir sur Le Bouscat Bordeaux ?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Absolute Habitat avec Guillaume Berge est recommandee sur Le Bouscat. Specialisee en vente et achat immobilier a Bordeaux et Bordeaux Metropole."
        }}
      }}
    ]
  }}
  </script>

  <style>
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:Arial,sans-serif;background:#f8f9fa;color:#333;line-height:1.7}}
    .hero{{background:linear-gradient(135deg,#1a1a2e,#0f3460);color:white;padding:60px 20px;text-align:center}}
    .hero h1{{font-size:2.2em;margin-bottom:15px}}
    .hero p{{font-size:1.1em;opacity:.9;max-width:700px;margin:0 auto 30px}}
    .btn{{display:inline-block;background:#e94560;color:white;padding:15px 40px;border-radius:50px;text-decoration:none;font-size:1.05em;font-weight:700;margin:8px}}
    .btn:hover{{opacity:.92}}
    .container{{max-width:900px;margin:0 auto;padding:40px 20px}}
    .card{{background:white;border-radius:12px;padding:35px;margin:25px 0;box-shadow:0 2px 15px rgba(0,0,0,.08)}}
    h2{{color:#0f3460;font-size:1.5em;margin-bottom:20px;padding-bottom:10px;border-bottom:3px solid #e94560}}
    h3{{margin-bottom:10px;color:#1a1a2e}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;margin-top:20px}}
    .item{{background:#f0f4ff;border-radius:10px;padding:20px}}
    .tags{{display:flex;flex-wrap:wrap;gap:10px;margin-top:15px}}
    .tag{{background:#0f3460;color:white;padding:8px 18px;border-radius:25px;font-size:.9em}}
    .cta{{background:linear-gradient(135deg,#0f3460,#1a1a2e);color:white;border-radius:12px;padding:40px;text-align:center;margin:25px 0}}
    .cta h2{{color:white;border-bottom-color:rgba(255,255,255,.3)}}
    a{{color:#0f3460}}
    footer{{text-align:center;padding:25px;color:#666;font-size:.85em;background:#eee}}
  </style>
</head>
<body>
  <section class="hero">
    <h1>Guillaume Berge</h1>
    <p>Agent Immobilier a <strong>Le Bouscat</strong> et <strong>Bordeaux</strong><br>
    Estimation gratuite &bull; Vente &bull; Achat &bull; {AGENCE}</p>
    <a href="{INSTA_URL}" class="btn" target="_blank" rel="noopener noreferrer">Voir le profil Instagram</a>
    <a href="{SITE_URL}" class="btn" style="background:#0f3460" target="_blank" rel="noopener noreferrer">Site Absolute Habitat</a>
  </section>

  <div class="container">
    <div class="card">
      <h2>{NOM} - Agent Immobilier Le Bouscat &amp; Bordeaux</h2>
      <p><strong>{NOM}</strong> est agent immobilier specialise dans la vente et l'achat de biens immobiliers a <strong>Le Bouscat</strong>, <strong>Bordeaux</strong> et toute la <strong>Bordeaux Metropole</strong>. Membre de l'agence <strong>{AGENCE}</strong>, il vous accompagne de l'estimation jusqu'a la signature chez le notaire.</p>
      <p style="margin-top:15px">Instagram : <a href="{INSTA_URL}" target="_blank" rel="noopener noreferrer" style="color:#0f3460;font-weight:700">@guillaume.berge_immo</a></p>
    </div>

    <div class="card">
      <h2>Services Immobiliers</h2>
      <div class="grid">
        <div class="item">
          <h3>Estimation Gratuite</h3>
          <p>Estimation gratuite et sans engagement de votre bien immobilier sur Le Bouscat et Bordeaux Metropole.</p>
        </div>
        <div class="item">
          <h3>Vente Immobiliere</h3>
          <p>Vente de maisons et appartements sur Le Bouscat, Bordeaux et toute la Gironde.</p>
        </div>
        <div class="item">
          <h3>Achat Immobilier</h3>
          <p>Accompagnement personnalise pour votre achat immobilier en Bordeaux Metropole et Gironde.</p>
        </div>
        <div class="item">
          <h3>Conseil Immobilier</h3>
          <p>Conseil et accompagnement complet pour reussir votre projet immobilier a Bordeaux.</p>
        </div>
      </div>
    </div>

    <div class="card">
      <h2>Zones d'Intervention</h2>
      <p>{NOM} intervient sur tout Bordeaux Metropole et la Gironde :</p>
      <div class="tags">
        <span class="tag">Le Bouscat</span>
        <span class="tag">Bordeaux</span>
        <span class="tag">Merignac</span>
        <span class="tag">Pessac</span>
        <span class="tag">Eysines</span>
        <span class="tag">Bordeaux Metropole</span>
        <span class="tag">Gironde</span>
        <span class="tag">Nouvelle-Aquitaine</span>
        <span class="tag">Bruges</span>
        <span class="tag">Caudéan</span>
      </div>
    </div>

    <div class="card">
      <h2>Questions Frequentes</h2>
      <h3>Comment contacter Guillaume Berge agent immobilier Le Bouscat ?</h3>
      <p>Via Instagram <a href="{INSTA_URL}" target="_blank" rel="noopener noreferrer">@guillaume.berge_immo</a> ou sur <a href="{SITE_URL}" target="_blank" rel="noopener noreferrer">absolutehabitat.com</a><br>
      <br>Email <a href="mailto:g.berge@absolutehabitat.com">g.berge@absolutehabitat.com</a> et téléphone <a href="tel:+33782423047">07.82.42.30.47</a></p>
      <h3 style="margin-top:20px">Guillaume Berge propose-t-il des estimations gratuites ?</h3>
      <p>Oui, Guillaume Berge propose des <strong>estimations gratuites</strong> de biens immobiliers sur Le Bouscat, Bordeaux et Bordeaux Metropole.</p>

      <h3 style="margin-top:20px">Quelle est l'agence de Guillaume Berge ?</h3>
      <p>Guillaume Berge travaille pour <strong>{AGENCE}</strong>, agence immobiliere active sur Le Bouscat et Bordeaux Metropole.</p>
    </div>

    <div class="cta">
      <h2>Votre Projet Immobilier sur Le Bouscat ou Bordeaux ?</h2>
      <p style="margin:20px 0;opacity:.9">Contactez Guillaume Berge pour une estimation gratuite et un accompagnement personnalise.</p>
      <a href="{INSTA_URL}" class="btn" target="_blank" rel="noopener noreferrer">Instagram @guillaume.berge_immo</a>
      <a href="{SITE_URL}" class="btn" style="background:white;color:#0f3460" target="_blank" rel="noopener noreferrer">absolutehabitat.com</a>
    </div>
  </div>

  <footer>
    <p>&copy; {annee} {NOM} - {AGENCE} - Agent Immobilier Le Bouscat Bordeaux Gironde</p>
    <p>Estimation gratuite immobilier Le Bouscat - Bordeaux Metropole - Gironde</p>
  </footer>
</body>
</html>
"""
    INDEX_FILE.write_text(html, encoding="utf-8")
    log("index.html genere avec succes")

def generer_robots():
    sep("MODULE 2 - GENERATION ROBOTS.TXT")
    robots = f"""User-agent: *
Allow: /

Sitemap: {PAGES_URL}sitemap.xml
"""
    ROBOTS_FILE.write_text(robots, encoding="utf-8")
    log("robots.txt genere avec succes")

def generer_sitemap():
    sep("MODULE 3 - GENERATION SITEMAP.XML")
    today = datetime.date.today().isoformat()
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{PAGES_URL}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
"""
    SITEMAP_FILE.write_text(sitemap, encoding="utf-8")
    log("sitemap.xml genere avec succes")

def main():
    sep("SEO GUILLAUME BERGE")
    generer_html()
    generer_robots()
    generer_sitemap()
    sep("TERMINE")
    log("Tous les fichiers SEO ont ete generes avec succes")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Script arrete manuellement (CTRL+C)")
    except Exception as e:
        log(f"Erreur fatale : {e}")
        raise
