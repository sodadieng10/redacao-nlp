import streamlit as st
from generator import generate_ao

st.set_page_config(page_title="RédacAO - Assistant AO", layout="centered")

st.title("RédacAO – Assistant de rédaction d'appels d'offres")

st.markdown("Cet assistant génère une ébauche d'appel d'offres en se basant sur les informations que vous fournissez.")

# Entrée utilisateur
titre = st.text_input("**Titre de l'appel d'offres**")
theme = st.text_input("**Thématique**")
contraintes = st.text_area("**Contraintes spécifiques** (ex : budget, délais, exigences techniques)")

# Génération
if st.button("Générer l'appel d'offres"):
    if not titre or not theme:
        st.warning("Merci de remplir au moins le titre et la thématique.")
    else:
        with st.spinner("Génération en cours..."):
            try:
                ao = generate_ao(titre, theme, contraintes)
                st.subheader("Appel d'offres généré")
                st.text_area("", ao, height=400)

                # Téléchargement
                st.download_button(
                    label="Télécharger en .txt",
                    data=ao,
                    file_name="appel_offres_genere.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Erreur lors de la génération : {e}")
