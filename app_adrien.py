import streamlit as st
import pandas as pd
import numpy as np

st.title('Dwidwi App')

# Sous-titre
st.header("Test")

# Texte
st.write("Ceci est un exemple de texte dans Streamlit.")

# Bouton
st.button("Cliquez ici pour exécuter une action")

# Slider
st.slider("Sélectionnez une valeur", 0, 10, step=1)

# Selectbox
options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Sélectionnez une option", options)

# Checkbox
if st.checkbox("Afficher les détails"):
    st.write("Voici les détails de l'élément sélectionné : ", selected_option)
