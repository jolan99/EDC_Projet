import streamlit as st
import pandas as pd
import numpy as np
import time
from casques_audio import *
from io import StringIO

# ce qu'on pourrait faire ce serait de faire une fonction, où l'utilisateur entre les données comme 
# le nombre d'heures possible, le coût de production etc, et si rien n'est entré alors c'est les données du .txt

left_column, right_column = st.columns(2)


# Or even better, call Streamlit functions inside a "with" block:

# # Sous-titre
# st.header("Test")

# # Texte
# st.write("Ceci est un exemple de texte dans Streamlit.")

# # Bouton
# st.button("Cliquez ici pour exécuter une action")

# # Slider
# st.slider("Sélectionnez une valeur", 0, 10, step=1)

# # Selectbox
# options = ["Option 1", "Option 2", "Option 3"]
# selected_option = st.selectbox("Sélectionnez une option", options)

# # Checkbox
# if st.checkbox("Afficher les détails"):
#     st.write("Voici les détails de l'élément sélectionné : ", selected_option)


# def essai(x=2,y=3):
#     return(x+y)

# instance = lecture("data_etude_cas.txt")
# Sol = solve(instance)

# df1 = pd.DataFrame(Sol.qtt_livree[0])
# df1.columns = Sol.nom_villes
# df1 = df1.T
# df1.columns = Sol.nom_usines
# df2 = pd.DataFrame(Sol.qtt_livree[1])
# df2.columns = Sol.nom_villes
# df2 = df2.T
# df2.columns = Sol.nom_usines
# df3 = pd.DataFrame(Sol.qtt_livree[2])
# df3.columns = Sol.nom_villes
# df3 = df3.T
# df3.columns = Sol.nom_usines
        
# df1bis = pd.concat([df1.Bordeaux,df2.Bordeaux,df3.Bordeaux],axis=1,keys = Sol.nom_casques)
# df2bis = pd.concat([df1.Lyon,df2.Lyon,df3.Lyon],axis=1,keys = Sol.nom_casques)
# df3bis = pd.concat([df1.Nanterre,df2.Nanterre,df3.Nanterre],axis=1,keys = Sol.nom_casques)
# sol = pd.concat([df1bis,df2bis,df3bis],axis=1,keys = Sol.nom_usines)

# st.write(sol)

# st.dataframe(sol.style.highlight_max(axis=0))

# st.write("le line chart : ")
# st.line_chart(sol)

# st.write("st map :")
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

# st.write("widget : ")
# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# #Use checkboxes to show/hide data

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data

# # Use a selectbox for options

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# # un peu plus : 




# ####"" time : 
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)


######### ESSAIS  : 

# st.sidebar.write('Veuillez changer ici les données. Le calcul sera automatique.')
# instance = lecture("data_etude_cas.txt")  
# st.sidebar.info('Coût par kilomètre :', icon="💸")
# Cost_km = st.sidebar.number_input('Veuillez indiquer ci-dessous le coût estimé',min_value=0.000,value = 0.034,step = 0.001)
# instance.cost_km = Cost_km
# instance.Temps_max
# Sol = solve(instance)
# print("##########################")
# Sol.print()




# st.write(Sol.sol_to_df())  # affiche le tableau des résultats
# cout_total = 0
# for j in range(Sol.nb_usines):
#     cout_usine = 0
#     for i in range(Sol.nb_modeles):
#         for k in range(Sol.nb_villes):
#             cout_usine += Sol.qtt_livree[i][j][k]*Sol.cost_km * Sol.Distances[j][k]
#     cout_total += cout_usine
# st.write('la valeur de la solution est ',cout_total)
# # st.snow()
# st.sidebar.info('Modèles à l\'étude :', icon="🎧")
# st.success('This is a success message!', icon="✅")
with left_column:
    st.title('Production de Casques Audio')

with right_column:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGeMirkdLwm5s1uOr1kEIj-VMuAPPKpREl-2OcnNE8rXK74AS7MJTNc4fedXMdAHyiI7M&usqp=CAU",caption = "@mehmetbuma")

st.sidebar.write('### **Sur quelles données voulez-vous tester le modèle ?**')
chosen = st.sidebar.radio(
        'Veuillez choisir ci-dessous :',
        ("Je veux utiliser le fichier exemple \"data_etude_cas.txt\"", "Je veux modifier les données manuellement", "Je veux utiliser un autre fichier de données .txt"))

if chosen == "Je veux utiliser le fichier exemple \"data_etude_cas.txt\"":
    #ici qqchose 
    instance = lecture("data_etude_cas.txt") 
elif chosen == "Je veux modifier les données manuellement":
    st.sidebar.write('Veuillez changer ici les données. Le calcul sera automatique.')
    instance = lecture("data_etude_cas.txt")  
    # def reset():
    #     st.session_state = lecture("data_etude_cas.txt") 
    # st.sidebar.button('Réinitialiser le coût', on_click=reset)
    # cost_km:
    st.sidebar.info('Coût par kilomètre (en centimes):', icon="💸")
    Cost_km = st.sidebar.number_input('Veuillez indiquer ci-dessous le coût estimé',min_value=0.0,value = 3.4,step = 0.1,key='cost')
    instance.cost_km = Cost_km*0.01
    # def reset1():
    #     st.session_state.cost = 3.4
    # st.sidebar.button('Réinitialiser le coût', on_click=reset1)

    # Distances :
    st.sidebar.info('Distances en km :', icon="🚄")
    dist = pd.DataFrame(instance.Distances)
    dist.columns = instance.nom_villes
    dist = dist.T
    dist.columns = instance.nom_usines
    dist = st.sidebar.experimental_data_editor(dist)
    instance.Distances = dist.to_numpy().T
    # def reset():
    #     st.session_state.dist = lecture("data_etude_cas.txt").Distances
    # st.sidebar.button('Réinitialiser les distances', on_click=reset)
    
    # Demandes :
    st.sidebar.info('Demandes :', icon="🚄")
    dem = pd.DataFrame(instance.Demandes)
    dem.columns = instance.nom_villes
    dem = dem.T
    dem.columns = instance.nom_casques
    dem = st.sidebar.experimental_data_editor(dem)
    instance.Demandes = dem.to_numpy().T
    # def reset():
    #     st.session_state.demandes = lecture("data_etude_cas.txt").Demandes
    # st.sidebar.button('Réinitialiser les demandes', on_click=reset)

    # Temps disponible  :
    st.sidebar.info('Total heures disponibles  :', icon="👍")
    for i in range(instance.nb_usines):
        # j = st.slider(f'Usine de {instance.nom_usines[i]} : ', 0, 100000, instance.Temps_max[i])
        value_depart = int(instance.Temps_max[i])
        j = st.sidebar.slider(f'Usine de {instance.nom_usines[i]} : ', 0, 100000, value_depart)
        instance.Temps_max[i] = j
    # def reset():
    #     for i in range(instance.nb_usines):
    #         st.session_state.i= lecture("data_etude_cas.txt").Temps_max
    # st.sidebar.button('Réinitialiser les Temps disponibles', on_click=reset)

    # Temps de fabrications :
    st.sidebar.info('Durées de fabrication par modèle :', icon="🔨")
    temps_fab = pd.DataFrame(instance.Temps_fabrication)
    temps_fab.columns = instance.nom_usines
    temps_fab = temps_fab.T
    temps_fab.columns = instance.nom_casques
    temps_fab = st.sidebar.experimental_data_editor(temps_fab)
    instance.Temps_fabrication = temps_fab.to_numpy().T
    # def reset():
    #     st.session_state.demanes = lecture("data_etude_cas.txt").Temps_fabrication
    # st.sidebar.button('Réinitialiser les temps de fabrication', on_click=reset)

    # def reset():
    #     st.session_state.instance = lecture("data_etude_cas.txt")
    # st.sidebar.button('Reset', on_click=reset)

    
        

elif chosen == "Je veux utiliser un autre fichier de données .txt" :
    uploaded_file = st.file_uploader("Choisissez un fichier .txt")
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        instance = lecture(stringio)

# st.write('debug 1')
Sol = solve(instance)
# st.write('debug 2')
st.write('### Voici la répartition de production optimale pour avoir un coût total de transport minimal : ')
st.write('Sur les lignes sont les magasins, et sur les colonnes sont les modèles de casque et les usines.')
st.write(f'Par exemple : Il faudra envoyer au magasin de Lille {int(Sol.qtt_livree[0][2][0])} casques de modèle Grosson depuis l\'usine de Nanterre.')
st.write(Sol.sol_to_df())  # affiche le tableau des résultats
cout_total = 0
for j in range(Sol.nb_usines):
    cout_usine = 0
    for i in range(Sol.nb_modeles):
        for k in range(Sol.nb_villes):
            cout_usine += Sol.qtt_livree[i][j][k]*Sol.cost_km * Sol.Distances[j][k]
    cout_total += cout_usine
st.write('### Le coût total de cette solution est ',cout_total,' €')
# st.snow()
st.sidebar.info('Modèles à l\'étude :', icon="🎧")

'Affichage sélectif : '
options_casques = st.multiselect(
    'Quel(s) modèle(s) voulez-vous sélctionner ?',
    instance.nom_casques,
    instance.nom_casques)

options_villes = st.multiselect(
    'Quelle(s) ville(s) voulez-vous sélctionner ?',
    instance.nom_villes,
    instance.nom_villes)

options_usines = st.multiselect(
    'Quelle(s) usine(s) voulez-vous sélctionner ?',
    instance.nom_usines,
    instance.nom_usines)

l1 = []
for i in (options_casques):
    l1.append(instance.nom_casques.index(i))

l2 = []
for i in (options_villes):
    l2.append(instance.nom_villes.index(i))

l3 = []
for i in (options_usines):
    l3.append(instance.nom_usines.index(i))

if len(l1) == 1 : 
    df1 = pd.DataFrame(Sol.qtt_livree[l1[0]])
    df1.columns = instance.nom_villes
    df1 = df1.T
    df1.columns = instance.nom_usines

    # for i in options_usines:
    #     df1 = pd.concat([df1[f'{i}']],axis=1,keys = options_casques)
    
    # # st.write(f'debug {4}: ',df1)
    
    if len(options_usines) == 1 :
        df1bis = pd.concat([df1[options_usines[0]]],axis=1,keys = options_casques)
        final = pd.concat([df1bis],axis=1,keys = options_usines)
        # st.write(f'debug {4}: ',final)
    elif  len(options_usines) == 2 :
        df1bis = pd.concat([df1[options_usines[0]]],axis=1,keys = options_casques)
        df2bis = pd.concat([df1[options_usines[1]]],axis=1,keys = options_casques)
        final = pd.concat([df1bis,df2bis],axis=1,keys = options_usines)
        # st.write(f'debug {4}: ',final)

    elif len(options_usines) == 3 :
        df1bis = pd.concat([df1[options_usines[0]]],axis=1,keys = options_casques)
        df2bis = pd.concat([df1[options_usines[1]]],axis=1,keys = options_casques)
        df3bis = pd.concat([df1[options_usines[2]]],axis=1,keys = options_casques)
        final = pd.concat([df1bis,df2bis,df3bis],axis=1,keys = options_usines)
        # st.write(f'debug {4}: ',final)

elif len(l1) == 2 :
    df1 = pd.DataFrame(Sol.qtt_livree[l1[0]])
    df1.columns = instance.nom_villes
    df1 = df1.T
    df1.columns = instance.nom_usines

    df2 = pd.DataFrame(Sol.qtt_livree[l1[1]])
    df2.columns = instance.nom_villes
    df2 = df2.T
    df2.columns = instance.nom_usines

    # for i in options_usines:
    #     df1 = pd.concat([df1[f'{i}'],df2[f'{i}']],axis=1,keys = options_casques)
    
    # st.write(f'debug {4}: ',df1)
    
    if len(options_usines) == 1 :
        df1bis = pd.concat([df1[options_usines[0]],df2[options_usines[0]]],axis=1,keys = options_casques)
        final = pd.concat([df1bis],axis=1,keys = options_usines)
        # st.write(f'debug {4}: ',final)
    elif  len(options_usines) == 2 :
        df1bis = pd.concat([df1[options_usines[0]],df2[options_usines[0]]],axis=1,keys = options_casques)
        df2bis = pd.concat([df1[options_usines[1]],df2[options_usines[1]]],axis=1,keys = options_casques)
        final = pd.concat([df1bis,df2bis],axis=1,keys = options_usines)
        # st.write(f'debug {4}: ',final)

    elif len(options_usines) == 3 :
        df1bis = pd.concat([df1[options_usines[0]],df2[options_usines[0]]],axis=1,keys = options_casques)
        df2bis = pd.concat([df1[options_usines[1]],df2[options_usines[1]]],axis=1,keys = options_casques)
        df3bis = pd.concat([df1[options_usines[2]],df2[options_usines[2]]],axis=1,keys = options_casques)
        final = pd.concat([df1bis,df2bis,df3bis],axis=1,keys = options_usines)
        # st.write(f'debug {4}: ',final)

elif len(l1) == 3 :
    df1 = pd.DataFrame(Sol.qtt_livree[l1[0]])
    df1.columns = instance.nom_villes
    df1 = df1.T
    df1.columns = instance.nom_usines
    # st.write('debug 1: ',df1)

    df2 = pd.DataFrame(Sol.qtt_livree[l1[1]])
    df2.columns = instance.nom_villes
    df2 = df2.T
    df2.columns = instance.nom_usines
    # st.write('debug 2: ',df2)

    df3 = pd.DataFrame(Sol.qtt_livree[l1[2]])
    df3.columns = instance.nom_villes
    df3 = df3.T
    df3.columns = instance.nom_usines
    # st.write('debug 3: ',df3)

    if len(options_usines) == 1 :
        df1bis = pd.concat([df1[options_usines[0]],df2[options_usines[0]],df3[options_usines[0]]],axis=1,keys = options_casques)
        final = pd.concat([df1bis],axis=1,keys = options_usines)
        # st.write(f'debug {4}: ',final)
    elif  len(options_usines) == 2 :
        df1bis = pd.concat([df1[options_usines[0]],df2[options_usines[0]],df3[options_usines[0]]],axis=1,keys = options_casques)
        df2bis = pd.concat([df1[options_usines[1]],df2[options_usines[1]],df3[options_usines[1]]],axis=1,keys = options_casques)
        final = pd.concat([df1bis,df2bis],axis=1,keys = options_usines)
        # st.write(f'debug {4}: ',final)

    elif len(options_usines) == 3 :
        df1bis = pd.concat([df1[options_usines[0]],df2[options_usines[0]],df3[options_usines[0]]],axis=1,keys = options_casques)
        df2bis = pd.concat([df1[options_usines[1]],df2[options_usines[1]],df3[options_usines[1]]],axis=1,keys = options_casques)
        df3bis = pd.concat([df1[options_usines[2]],df2[options_usines[2]],df3[options_usines[2]]],axis=1,keys = options_casques)
        final = pd.concat([df1bis,df2bis,df3bis],axis=1,keys = options_usines)
        # st.write(f'debug {4}: ',final)


        

st.write(final)
# st.write('You selected:', options_villes)

