import streamlit as st
import pandas as pd
import numpy as np
from casques_audio import *

# ce qu'on pourrait faire ce serait de faire une fonction, où l'utilisateur entre les données comme 
# le nombre d'heures possible, le coût de production etc, et si rien n'est entré alors c'est les données du .txt

st.title('Production Casques Audio')

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





Sol = solve()

df1 = pd.DataFrame(Sol.qtt_livree[0])
df1.columns = Sol.nom_villes
df1 = df1.T
df1.columns = Sol.nom_usines
df2 = pd.DataFrame(Sol.qtt_livree[1])
df2.columns = Sol.nom_villes
df2 = df2.T
df2.columns = Sol.nom_usines
df3 = pd.DataFrame(Sol.qtt_livree[2])
df3.columns = Sol.nom_villes
df3 = df3.T
df3.columns = Sol.nom_usines
        
df1bis = pd.concat([df1.Bordeaux,df2.Bordeaux,df3.Bordeaux],axis=1,keys = Sol.nom_casques)
df2bis = pd.concat([df1.Lyon,df2.Lyon,df3.Lyon],axis=1,keys = Sol.nom_casques)
df3bis = pd.concat([df1.Nanterre,df2.Nanterre,df3.Nanterre],axis=1,keys = Sol.nom_casques)
sol = pd.concat([df1bis,df2bis,df3bis],axis=1,keys = Sol.nom_usines)

st.write(sol)

       