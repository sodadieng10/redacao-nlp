import streamlit as st
from generator_ex import generate_ao

st.title("RédacAO - Assistant de rédaction d'appels d'offres")

titre = st.text_input("Titre de l'appel d'offres")
theme = st.text_input("Thématique")
contraintes = st.text_area("Contraintes spécifiques")

if st.button("Générer l'appel d'offres"):
    if not titre or not theme:
        st.warning("Merci de remplir au moins le titre et la thématique.")
    else:
        ao = generate_ao(titre, theme, contraintes)
        st.subheader("Appel d'Offres généré")
        st.text_area("", ao, height=300)
