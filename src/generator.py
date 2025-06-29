import os
import openai
import json

# Récupération de la clé API depuis la variable d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_section(titre, thématique, contraintes, section):
    prompt = f"""
Tu es un assistant expert en marchés publics.
Génère la section suivante d’un appel d’offres : "{section}".

Contexte :
- Titre : {titre}
- Thématique : {thématique}
- Contraintes : {', '.join(contraintes) if isinstance(contraintes, list) else contraintes}

Consignes :
- Structure juridique
- Ton formel
- Langue : français
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",  # ou "gpt-4o" si disponible
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=600
    )

    return response["choices"][0]["message"]["content"]

def generate_ao(titre, theme, contraintes):
    sections = ["Objectif", "Prestations attendues", "Contraintes", "Critères de sélection"]
    texte_complet = ""
    for section in sections:
        texte = generate_section(titre, theme, contraintes, section)
        texte_complet += f"\n### {section}\n{texte.strip()}\n"
    return texte_complet

# Test local si lancé directement
if __name__ == "__main__":
    with open("../data/clean/ao_clean.json", encoding="utf-8") as f:
        ao_list = json.load(f)

    ao_sample = ao_list[0]
    resultat = generate_ao(
        titre=ao_sample["titre"],
        theme=ao_sample.get("thématique", "Informatique"),
        contraintes=ao_sample["contraintes"]
    )

    print(resultat)
