import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd

def cluster_aos(path="data/clean/ao_clean.json", n_clusters=3):
    with open(path, "r") as f:
        data = json.load(f)

    corpus = [" ".join(ao["objectifs"] + ao["prestations"] + ao["contraintes"]) for ao in data]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(X)

    df = pd.DataFrame(data)
    df["cluster"] = kmeans.labels_
    return df