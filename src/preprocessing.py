import json
import os
import spacy

nlp = spacy.load("fr_core_news_md")

def preprocess_ao(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    clean_data = []

    for ao in data:
        doc = nlp(ao["contenu"])
        sections = {
            "titre": ao["titre"],
            "objectifs": "",
            "prestations": "",
            "contraintes": ""
        }

        for sent in doc.sents:
            sent_text = sent.text.lower()
            if "objectif" in sent_text or "objet" in sent_text:
                sections["objectifs"] += sent.text + " "
            elif "prestations" in sent_text or "livraison" in sent_text:
                sections["prestations"] += sent.text + " "
            elif "contraintes" in sent_text or "critères" in sent_text:
                sections["contraintes"] += sent.text + " "

        clean_data.append(sections)

    # Assure-toi que le dossier existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clean_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_file = os.path.join(base_dir, "data", "raw", "ao_data.json")
    output_file = os.path.join(base_dir, "data", "clean", "ao_clean.json")

    preprocess_ao(input_file, output_file)
