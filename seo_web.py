#!/usr/bin/env python3
import os, requests, datetime, subprocess
from pathlib import Path

# ─── CONFIG ────────────────────────────────────────────────
GITHUB_USER  = "ccrismel-beep"
GITHUB_REPO  = "guillaume-berge-immo"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")  # ← colle ton nouveau token ici
GITHUB_URL   = f"https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{GITHUB_REPO}.git"
PAGES_URL    = f"https://{GITHUB_USER}.github.io/{GITHUB_REPO}/"

NOM          = "Guillaume Berge"
AGENCE       = "Absolute Habitat"
INSTA_URL    = "https://www.instagram.com/guillaume.berge_immo/"
SITE_URL     = "https://www.absolutehabitat.com"
BASE_DIR     = Path(__file__).parent
LOG_FILE     = BASE_DIR / f"seo_log_{datetime.date.today()}.log"

KEYWORDS = [
    "Guillaume Berge Agent Immobilier Bordeaux",
    "Agent Immobilier Le Bouscat",
    "Estimation gratuite immobilier Le Bouscat",
    "Absolute Habitat Bordeaux",
    "Vente achat immobilier Bordeaux Le Bouscat",
    "Agent immobilier Gironde",
    "Estimation immobilière gratuite Bordeaux",
    "Immobilier Le Bouscat 33110",
]

def log(msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def sep(t): log(f"\n{'='*50}\n  {t}\n{'='*50}")

# ─── MODULE 1 : GÉNÉRATION HTML SEO ────────────────────────
def generer_html():
    sep("MODULE 1 — GÉNÉRATION PAGE HTML SEO")
    today  = datetime.date.today().isoformat()
    annee  = datetime.date.today().year
    kw_str = ", ".join(KEYWORDS)

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{NOM} - Agent Immobilier Le Bouscat Bordeaux | {AGENCE}</title>
  <meta name="description" content="{NOM}, Agent Immobilier a Le Bouscat et Bordeaux. Estimation gratuite de votre bien immobilier. Vente, achat avec {AGENCE}. Expert immobilier Bordeaux Metropole et Gironde.">
  <meta name="keywords" content="{kw_str}">
  <meta name="robots" content="index, follow">
  <meta name="author" content="{NOM}">
  <meta name="geo.region" content="FR-NAQ">
  <meta name="geo.placename" content="Le Bouscat, Bordeaux">
  >
  <meta property="og:type" content="profile">
  <meta property="og:title" content="{NOM} - Agent Immobilier Le Bouscat Bordeaux">
  <meta property="og:description" content="Estimation gratuite immobilier Le Bouscat. Vente et achat a Bordeaux avec {AGENCE}.">
  <meta property="og:url" content="{PAGES_URL}">
  <meta property="og:locale" content="fr_FR">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "RealEstateAgent",
    "name": "{NOM}",
    "jobTitle": "Agent Immobilier",
    "description": "Agent immobilier specialise dans la vente et achat de biens a Le Bouscat, Bordeaux et Bordeaux Metropole. Estimation gratuite offerte.",
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
      "geo": {{"@type": "GeoCoordinates", "latitude": 44.8637, "longitude": -0.5897}},
      "openingHoursSpecification": [{{"@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
        "opens": "09:00", "closes": "19:00"}}]
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
        "name": "Qui est Guillaume Berge agent immobilier a Le Bouscat ?",
        "acceptedAnswer": {{"@type": "Answer",
          "text": "Guillaume Berge est agent immobilier a Le Bouscat et Bordeaux, specialiste de la vente et achat immobilier en Bordeaux Metropole. Il travaille chez Absolute Habitat et propose des estimations gratuites."}}
      }},
      {{
        "@type": "Question",
        "name": "Comment obtenir une estimation gratuite a Le Bouscat ?",
        "acceptedAnswer": {{"@type": "Answer",
          "text": "Guillaume Berge propose des estimations gratuites a Le Bouscat et Bordeaux. Contactez-le via Instagram @guillaume.berge_immo ou sur absolutehabitat.com."}}
      }},
      {{
        "@type": "Question",
        "name": "Quelle agence immobiliere choisir a Le Bouscat Bordeaux ?",
        "acceptedAnswer": {{"@type": "Answer",
          "text": "Absolute Habitat avec Guillaume Berge est recommandee a Le Bouscat. Specialisee vente et achat immobilier a Bordeaux et Bordeaux Metropole."}}
      }}
    ]
  }}
  </script>
  <style>
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:Arial,sans-serif;background:#f8f9fa;color:#333;line-height:1.7}}
    .hero{{background:linear-gradient(135deg,#1a1a2e,#0f3460);color:white;padding:60px 20px;text-align:center}}
    .hero h1{{font-size:2.2em;margin-bottom:15px}}
    .hero p{{font-size:1.1em;opacity:.9;max-width:600px;margin:0 auto 30px}}
    .btn{{display:inline-block;background:#e94560;color:white;padding:15px 40px;border-radius:50px;text-decoration:none;font-size:1.1em;font-weight:700;margin:8px}}
    .btn:hover{{opacity:.9}}
    .container{{max-width:900px;margin:0 auto;padding:40px 20px}}
    .card{{background:white;border-radius:12px;padding:35px;margin:25px 0;box-shadow:0 2px 15px rgba(0,0,0,.08)}}
    h2{{color:#0f3460;font-size:1.5em;margin-bottom:20px;padding-bottom:10px;border-bottom:3px solid #e94560}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;margin-top:20px}}
    .item{{background:#f0f4ff;border-radius:10px;padding:20px;border-left:4px solid #0f3460}}
    .tags{{display:flex;flex-wrap:wrap;gap:10px;margin-top:15px}}
    .tag{{background:#0f3460;color:white;padding:8px 18px;border-radius:25px;font-size:.9em}}
    .cta{{background:linear-gradient(135deg,#0f3460,#1a1a2e);color:white;border-radius:12px;padding:40px;text-align:center;margin:25px 0}}
    .cta h2{{color:white;border-bottom-color:rgba(255,255,255,.3)}}
    footer{{text-align:center;padding:25px;color:#666;font-size:.85em;background:#eee}}
  </style>
</head>
<body>
  <section class="hero">
    <h1>Guillaume Berge</h1>
    <p>Agent Immobilier a <strong>Le Bouscat</strong> et <strong>Bordeaux</strong><br>
    Estimation gratuite &bull; Vente &bull; Achat &bull; {AGENCE}</p>
    <a href="{INSTA_URL}" class="btn">Voir le profil Instagram</a>
    <a href="{SITE_URL}" class="btn" style="background:#0f3460">Site Absolute Habitat</a>
  </section>

  <div class="container">
    <div class="card">
      <h2>Guillaume Berge - Agent Immobilier Le Bouscat & Bordeaux</h2>
      <p><strong>Guillaume Berge</strong> est agent immobilier specialise dans la vente
      et l'achat de biens immobiliers a <strong>Le Bouscat</strong>, <strong>Bordeaux</strong>
      et toute la <strong>Bordeaux Metropole</strong>. Membre de l'agence
      <strong>Absolute Habitat</strong>, il vous accompagne de l'estimation jusqu'a
      la signature chez le notaire.</p>
      <p style="margin-top:15px">Instagram :
      <a href="{INSTA_URL}" style="color:#0f3460;font-weight:700">@guillaume.berge_immo</a></p>
    </div>

    <div class="card">
      <h2>Services Immobiliers</h2>
      <div class="grid">
        <div class="item">
          <h3>Estimation Gratuite</h3>
          <p>Estimation gratuite et sans engagement de votre bien immobilier
          a Le Bouscat et Bordeaux Metropole.</p>
        </div>
        <div class="item">
          <h3>Vente Immobiliere</h3>
          <p>Vente de maisons et appartements a Le Bouscat, Bordeaux
          et toute la Gironde.</p>
        </div>
        <div class="item">
          <h3>Achat Immobilier</h3>
          <p>Accompagnement personnalise pour votre achat immobilier
          en Bordeaux Metropole et Gironde.</p>
        </div>
        <div class="item">
          <h3>Conseil Immobilier</h3>
          <p>Conseil et accompagnement complet pour reussir votre projet
          immobilier a Bordeaux.</p>
        </div>
      </div>
    </div>

    <div class="card">
      <h2>Zones d'Intervention</h2>
      <p>Guillaume Berge intervient sur toute la Bordeaux Metropole et Gironde :</p>
      <div class="tags">
        <span class="tag">Le Bouscat</span>
        <span class="tag">Bordeaux</span>
        <span class="tag">Merignac</span>
        <span class="tag">Pessac</span>
        <span class="tag">Talence</span>
        <span class="tag">Bordeaux Metropole</span>
        <span class="tag">Gironde</span>
        <span class="tag">Nouvelle-Aquitaine</span>
      </div>
    </div>

    <div class="card">
      <h2>Questions Frequentes</h2>
      <h3>Comment contacter Guillaume Berge agent immobilier Le Bouscat ?</h3>
      <p>Via Instagram <a href="{INSTA_URL}">@guillaume.berge_immo</a>
      ou sur <a href="{SITE_URL}">absolutehabitat.com</a></p>
      <h3 style="margin-top:20px">Guillaume Berge propose-t-il des estimations gratuites ?</h3>
      <p>Oui, Guillaume Berge propose des <strong>estimations gratuites</strong>
      de biens immobiliers a Le Bouscat, Bordeaux et Bordeaux Metropole.</p>
      <h3 style="margin-top:20px">Quelle est l'agence de Guillaume Berge ?</h3>
      <p>Guillaume Berge travaille pour <strong>Absolute Habitat</strong>,
      agence immobiliere situee a Le Bouscat, specialisee sur Bordeaux Metropole.</p>
    </div>

    <div class="cta">
      <h2>Votre Projet Immobilier a Le Bouscat ou Bordeaux ?</h2>
      <p style="margin:20px 0;opacity:.9">Contactez Guillaume Berge pour une
      estimation gratuite et un accompagnement personnalise.</p>
      <a href="{INSTA_URL}" class="btn">Instagram @guillaume.berge_immo</a>
      <a href="{SITE_URL}" class="btn" style="background:white;color:#0f3460">
      absolutehabitat.com</a>
    </div>
  </div>

  <footer>
    <p>&copy; {annee} {NOM} - {AGENCE} - Agent Immobilier Le Bouscat Bordeaux Gironde</p>
    <p>Estimation gratuite immobilier Le Bouscat
