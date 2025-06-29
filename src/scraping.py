import requests
import xml.etree.ElementTree as ET
import json
import os

def scrape_ted_ai(keyword="Assistant intelligent de rédaction d'appels d'offres", max_results=50):
    # Encodage du mot-clé pour l'URL
    encoded_keyword = keyword.replace(" ", "%20")
    base_url = f"https://ted.europa.eu/TED/rss/en/rdf_search_result.xml?query={encoded_keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(base_url, headers=headers)
    if r.status_code != 200:
        print("❌ Erreur lors de la récupération du flux RSS")
        return

    root = ET.fromstring(r.content)
    items = root.findall(".//{http://purl.org/rss/1.0/}item")

    results = []
    for item in items[:max_results]:
        title = item.find("{http://purl.org/dc/elements/1.1/}title").text
        link = item.find("{http://purl.org/rss/1.0/}link").text
        desc = item.find("{http://purl.org/rss/1.0/}description")
        description = desc.text if desc is not None else ""

        results.append({
            "titre": title,
            "lien": link,
            "description": description
        })

    # Respect du chemin ../data/raw
    os.makedirs("../data/raw", exist_ok=True)
    with open("../data/raw/ted_ai_data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(results)} avis enregistrés dans ../data/raw/ted_ai_data.json avec le mot-clé : {keyword}")

if __name__ == "__main__":
    for kw in [
        "assistant intelligent",
        "rédaction appels d'offres",
        "outil automatique",
        "intelligence artificielle"
    ]:
        print(f"\n🔍 Recherche : {kw}")
        scrape_ted_ai(keyword=kw)


