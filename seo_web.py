import re
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

BASE_URL = "https://ccrismel-beep.github.io/guillaume-berge-immo/"
ROBOTS_URL = BASE_URL + "robots.txt"
SITEMAP_URL = BASE_URL + "sitemap.xml"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; SEOAuditBot/1.0; +https://ccrismel-beep.github.io/guillaume-berge-immo/)"
}

def fetch(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        return r
    except Exception as e:
        print(f"[ERREUR] Impossible de récupérer {url} : {e}")
        return None

def get_meta(soup, attr_name, attr_value, content_attr="content"):
    tag = soup.find("meta", attrs={attr_name: attr_value})
    return tag.get(content_attr, "").strip() if tag else None

def text_or_none(el):
    if not el:
        return None
    return " ".join(el.get_text(" ", strip=True).split())

def score_label(ok):
    return "OK" if ok else "NON"

def length_status(value, min_len, max_len):
    if not value:
        return "absent"
    n = len(value)
    if n < min_len:
        return f"trop court ({n})"
    if n > max_len:
        return f"trop long ({n})"
    return f"correct ({n})"

def parse_robots_for_sitemap(content):
    for line in content.splitlines():
        if line.lower().startswith("sitemap:"):
            return line.split(":", 1)[1].strip()
    return None

def parse_sitemap_urls(xml_text):
    urls = []
    try:
        root = ET.fromstring(xml_text)
        ns = {"sm": "https://www.sitemaps.org/schemas/sitemap/0.9"}
        for loc in root.findall(".//sm:loc", ns):
            if loc.text:
                urls.append(loc.text.strip())
    except Exception:
        pass
    return urls

def find_visible_address(text):
    patterns = [
        r"\b\d{1,4}\s+[A-Za-zÀ-ÿ0-9'’\-\s]+,\s*\d{5}\s+[A-Za-zÀ-ÿ'’\-\s]+\b",
        r"\b\d{1,4}\s+[A-Za-zÀ-ÿ0-9'’\-\s]+\s+\d{5}\s+[A-Za-zÀ-ÿ'’\-\s]+\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return " ".join(match.group(0).split())
    return None

def main():
    print("=" * 72)
    print("AUDIT SEO WEB")
    print("=" * 72)
    print(f"URL analysée : {BASE_URL}\n")

    page_response = fetch(BASE_URL)
    if not page_response:
        return

    print("[PAGE]")
    print(f"HTTP status           : {page_response.status_code}")
    print(f"URL finale            : {page_response.url}")
    print(f"Contenu HTML reçu     : {score_label('text/html' in page_response.headers.get('Content-Type', ''))}")
    print()

    soup = BeautifulSoup(page_response.text, "html.parser")
    page_text = soup.get_text(" ", strip=True)

    title = text_or_none(soup.title)
    meta_description = get_meta(soup, "name", "description")
    robots_meta = get_meta(soup, "name", "robots")
    canonical_tag = soup.find("link", rel="canonical")
    canonical = canonical_tag.get("href", "").strip() if canonical_tag else None

    og_title = get_meta(soup, "property", "og:title")
    og_description = get_meta(soup, "property", "og:description")
    og_url = get_meta(soup, "property", "og:url")
    twitter_card = get_meta(soup, "name", "twitter:card")

    h1_tags = soup.find_all("h1")
    h2_tags = soup.find_all("h2")
    h3_tags = soup.find_all("h3")
    first_h1 = text_or_none(h1_tags[0]) if h1_tags else None

    internal_anchor_links = []
    nav_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith("#"):
            internal_anchor_links.append(href)
    nav = soup.find("nav")
    if nav:
        for a in nav.find_all("a", href=True):
            nav_links.append(a["href"].strip())

    json_ld_blocks = soup.find_all("script", type="application/ld+json")
    json_ld_contains_realestate = any("RealEstateAgent" in (block.string or "") for block in json_ld_blocks)
    json_ld_contains_faq = any("FAQPage" in (block.string or "") for block in json_ld_blocks)
    json_ld_contains_website = any('"@type":"WebSite"' in re.sub(r"\s+", "", block.string or "") for block in json_ld_blocks)

    visible_address = find_visible_address(page_text)

    print("[BALISES SEO]")
    print(f"Title                 : {title}")
    print(f"Longueur title        : {length_status(title, 30, 65)}")
    print(f"Meta description      : {meta_description}")
    print(f"Longueur description  : {length_status(meta_description, 80, 170)}")
    print(f"Meta robots           : {robots_meta}")
    print(f"Canonical             : {canonical}")
    print(f"Canonical cohérente   : {score_label(canonical == BASE_URL)}")
    print()

    print("[OPEN GRAPH / TWITTER]")
    print(f"OG title              : {og_title}")
    print(f"OG description        : {og_description}")
    print(f"OG url                : {og_url}")
    print(f"OG url cohérente      : {score_label(og_url == BASE_URL)}")
    print(f"Twitter card          : {twitter_card}")
    print()

    print("[STRUCTURE HTML]")
    print(f"Nombre de H1          : {len(h1_tags)}")
    print(f"H1 principal          : {first_h1}")
    print(f"H1 unique             : {score_label(len(h1_tags) == 1)}")
    print(f"Nombre de H2          : {len(h2_tags)}")
    print(f"Nombre de H3          : {len(h3_tags)}")
    print(f"Adresse visible       : {visible_address if visible_address else 'Non détectée'}")
    print()

    print("[LIENS INTERNES]")
    print(f"Ancres internes       : {len(internal_anchor_links)}")
    print(f"Liens de navigation   : {nav_links if nav_links else 'Aucun nav détecté'}")
    required_anchors = {"#services", "#secteurs", "#adresse", "#faq", "#contact"}
    print(f"Ancres clés présentes : {score_label(required_anchors.issubset(set(internal_anchor_links)))}")
    print()

    print("[JSON-LD]")
    print(f"Nombre de blocs       : {len(json_ld_blocks)}")
    print(f"WebSite présent       : {score_label(json_ld_contains_website)}")
    print(f"RealEstateAgent       : {score_label(json_ld_contains_realestate)}")
    print(f"FAQPage présent       : {score_label(json_ld_contains_faq)}")
    print()

    print("[ROBOTS.TXT]")
    robots_response = fetch(ROBOTS_URL)
    if robots_response:
        print(f"HTTP status           : {robots_response.status_code}")
        robots_sitemap = parse_robots_for_sitemap(robots_response.text)
        print(f"Sitemap déclaré       : {robots_sitemap}")
        print(f"Sitemap cohérent      : {score_label(robots_sitemap == SITEMAP_URL)}")
    else:
        print("Impossible de lire robots.txt")
    print()

    print("[SITEMAP.XML]")
    sitemap_response = fetch(SITEMAP_URL)
    if sitemap_response:
        print(f"HTTP status           : {sitemap_response.status_code}")
        sitemap_urls = parse_sitemap_urls(sitemap_response.text)
        print(f"URLs trouvées         : {len(sitemap_urls)}")
        print(f"Contient la home      : {score_label(BASE_URL in sitemap_urls)}")
        if sitemap_urls:
            print("Liste :")
            for u in sitemap_urls:
                print(f" - {u}")
    else:
        print("Impossible de lire sitemap.xml")
    print()

    print("[RÉSUMÉ]")
    checks = {
        "page_200": page_response.status_code == 200,
        "title_ok": title is not None and 30 <= len(title) <= 65,
        "description_ok": meta_description is not None and 80 <= len(meta_description) <= 170,
        "canonical_ok": canonical == BASE_URL,
        "og_url_ok": og_url == BASE_URL,
        "h1_unique": len(h1_tags) == 1,
        "jsonld_realestate": json_ld_contains_realestate,
        "jsonld_faq": json_ld_contains_faq,
        "visible_address": visible_address is not None,
        "anchors_ok": required_anchors.issubset(set(internal_anchor_links)),
    }

    passed = sum(1 for v in checks.values() if v)
    total = len(checks)

    for name, value in checks.items():
        print(f"{name:20} : {score_label(value)}")

    print()
    print(f"Score simple          : {passed}/{total}")

if __name__ == "__main__":
    main()
