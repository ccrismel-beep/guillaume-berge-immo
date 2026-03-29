import re
import requests
from bs4 import BeautifulSoup

URL = "https://ccrismel-beep.github.io/guillaume-berge-immo/"

def get_meta(soup, attr_name, attr_value, content_attr="content"):
    tag = soup.find("meta", attrs={attr_name: attr_value})
    return tag.get(content_attr, "").strip() if tag else None

def text_or_none(el):
    if not el:
        return None
    return " ".join(el.get_text(" ", strip=True).split())

def main():
    print(f"Analyse SEO de : {URL}\n")

    r = requests.get(URL, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    print(f"HTTP status : {r.status_code}")
    print(f"URL finale  : {r.url}\n")

    soup = BeautifulSoup(r.text, "html.parser")

    title = text_or_none(soup.title)
    meta_description = get_meta(soup, "name", "description")
    robots = get_meta(soup, "name", "robots")
    canonical_tag = soup.find("link", rel="canonical")
    canonical = canonical_tag.get("href", "").strip() if canonical_tag else None

    og_title = get_meta(soup, "property", "og:title")
    og_description = get_meta(soup, "property", "og:description")
    og_url = get_meta(soup, "property", "og:url")

    h1 = text_or_none(soup.find("h1"))

    print("=== Balises principales ===")
    print("Title             :", title)
    print("Meta description  :", meta_description)
    print("Robots            :", robots)
    print("Canonical         :", canonical)
    print("H1                :", h1)
    print()

    print("=== Open Graph ===")
    print("OG title          :", og_title)
    print("OG description    :", og_description)
    print("OG url            :", og_url)
    print()

    json_ld_blocks = soup.find_all("script", type="application/ld+json")
    print("=== JSON-LD ===")
    print("Nombre de blocs   :", len(json_ld_blocks))
    for i, block in enumerate(json_ld_blocks, 1):
        content = block.string.strip() if block.string else ""
        preview = re.sub(r"\s+", " ", content)[:180]
        print(f"Bloc {i}           : {preview}")
    print()

    page_text = soup.get_text(" ", strip=True)
    address_patterns = [
        r"\b\d{1,4}\s+[A-Za-zÀ-ÿ0-9' -]+,\s*\d{5}\s+[A-Za-zÀ-ÿ' -]+\b",
        r"\b\d{1,4}\s+[A-Za-zÀ-ÿ0-9' -]+\s+\d{5}\s+[A-Za-zÀ-ÿ' -]+\b"
    ]

    found_address = None
    for pattern in address_patterns:
        match = re.search(pattern, page_text)
        if match:
            found_address = match.group(0)
            break

    print("=== Contrôles simples ===")
    print("Adresse visible   :", found_address if found_address else "Non détectée")
    print("Canonical OK      :", canonical == URL)
    print("OG URL OK         :", og_url == URL)
    print("Title present     :", bool(title))
    print("Description OK    :", bool(meta_description and len(meta_description) >= 80))
    print("H1 present        :", bool(h1))
    print("JSON-LD present   :", len(json_ld_blocks) > 0)

if __name__ == "__main__":
    main()
