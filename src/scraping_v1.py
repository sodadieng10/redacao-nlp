import requests
from bs4 import BeautifulSoup
import os
import json

def scrape_boamp(n_pages=5):
    base_url = "https://www.boamp.fr/pages/avis/?page={}"  # Exemple simplifié
    all_data = []
    
    for i in range(1, n_pages + 1):
        url = base_url.format(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        # Hypothèse : les avis sont dans des blocs <article>
        articles = soup.find_all("article")
        for art in articles:
            titre = art.find("h2").get_text(strip=True)
            contenu = art.get_text(strip=True)
            all_data.append({"titre": titre, "contenu": contenu})

    os.makedirs("../data/raw", exist_ok=True)
    with open("../data/raw/ao_data.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)


# 👉 C’est ici qu’on ajoute le main
if __name__ == "__main__":
    scrape_boamp(n_pages=3)