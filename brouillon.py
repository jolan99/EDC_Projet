# import localsolver
# # import sys
# from lecture_fichier import *
# from class_solution import *

# # regarder plus en détail les données, en utilisant dataframe par exemple 

# with localsolver .LocalSolver() as ls:
#     m = ls.model
#     #Dimensions
    
#     instance = lecture("data_etude_cas.txt") 

#     # variables 
#     x = [[[m.int(0,10000000000)for k in range(instance.nb_villes)]for j in range(instance.nb_usines)]for i in range(instance.nb_modeles)] # nb employés
    
#     for i in range(instance.nb_modeles):
#         for j in range(instance.nb_usines):
#             for k in range(instance.nb_villes):
#                 x[i][j][k].set_name('qtt_envoyee de casques {} depuis l usine de {} à  la ville de {}'.format(instance.nom_casques[i],instance.nom_usines[j],instance.nom_villes[k]))
                
#     #Data
   
#     for i in range(instance.nb_modeles): # on doit envoyer au moins la quantité demandée
#         for k in range(instance.nb_villes):
#             m.constraint(m.sum(x[i][j][k] for j in range(instance.nb_usines)) == instance.Demandes[i][k])

#     for j in range(instance.nb_usines):   # on ne doit pas dépasser le nombre d'heure de fabrication possible
#         m.constraint(m.sum(m.sum(x[i][j][k]*instance.Temps_fabrication[i][j] for i in range(instance.nb_modeles)) for k in range(instance.nb_villes)) <= instance.Temps_max[j])

#     # for j in range(instance.nb_usines):   # on ne doit pas dépasser le nombre d'heure de fabrication possible
#     #     for i in range(instance.nb_modeles):
#     #         m.constraint(m.sum(m.sum(x[i][j][k]*instance.Temps_fabrication[j][i] for i in range(instance.nb_modeles)) for k in range(instance.nb_villes)) <= instance.Temps_max[j])



#     m.minimize(m.sum(m.sum(m.sum(x[i][j][k]*instance.Distances[j][k]*instance.cost_km for i in range(instance.nb_modeles))for j in range(instance.nb_usines))for k in range(instance.nb_villes)))
    
#     m.close()
#     ls.param.time_limit = 30
   
#     ls.solve()
#     # import ipdb;ipdb.set_trace()
#     qtt_livree = np.zeros((instance.nb_modeles,instance.nb_usines,instance.nb_villes))
#     for k in range(instance.nb_villes):
#             for j in range(instance.nb_usines):
#                 for i in range(instance.nb_modeles):
#                     qtt_livree[i][j][k] = x[i][j][k].value

#     objective_value = ls.solution.get_objective_bound(0)

                   
#     Solution = solution(qtt_livree,objective_value, instance.nb_usines,instance.nb_modeles,instance.nb_villes, instance.nom_usines,instance.nom_casques,instance.nom_villes,instance.Temps_fabrication,instance.cost_km,instance.Distances)
#     Solution.print()

# ###########################
# # LECTURE FICHIER ######

# import numpy as np
# import pandas as pd 

# # vérifier qu'on a bien le bon ordre entre hauteur et largeur : villes/casques

# class data:
#     def __init__(self,Temps_fabrication,Temps_max,Demandes,Distances, nb_usines,nb_modeles,nb_villes, nom_usines,nom_casques,nom_villes,cost_km):
#         self.Temps_fabrication = Temps_fabrication
#         self.Temps_max = Temps_max
#         self.Demandes = Demandes
#         self.Distances = Distances
#         self.nb_usines = nb_usines
#         self.nb_modeles  = nb_modeles
#         self.nb_villes = nb_villes
#         self.nom_usines = nom_usines
#         self.nom_casques = nom_casques
#         self.nom_villes = nom_villes
#         self.cost_km = cost_km

#     def print(self):
#         print("######### INSTANCE : #########")
#         print(" Il y a {} usines, {} villes et {} modèles de casques audios".format(self.nb_usines,self.nb_villes,self.nb_modeles))
#         for v in range(self.nb_villes):
#             for m in range(self.nb_modeles):
#                 print("La ville de {} demande {} unités de {}".format(self.nom_villes[v],self.Demandes[m][v],self.nom_casques[m]))
#         print(" ")
#         for v in range(self.nb_villes):
#             for u in range(self.nb_usines):
#                 print("La ville de {} est à une distance de {}km de l'usine de {}".format(self.nom_villes[v],self.Distances[u][v],self.nom_usines[u]))
#         print(" ")
#         for u in range(self.nb_usines):
#             print("L'usine de {} dispose d'un total de {} heures disponibles".format(self.nom_usines[u], self.Temps_max[u]))
        
#         print(" ")
#         for u in range(self.nb_usines):
#             for m in range(self.nb_modeles):
#                 print("La production du casque {} dans l'usine de {} nécessite {}h en tout".format(self.nom_casques[m],self.nom_usines[u],self.Temps_fabrication[m][u]))





# def lecture(datafileName):

#     #ouverture du fichier, le ferme automatiquement à la fin et gère les exceptions
#     nom_usines=["Bordeaux","Lyon","Nanterre"]
#     nom_casques=["Grosson","Rapdeouf","Zoukafon"]
#     nom_villes = ["Lille","Clichy","Reims","Amiens","Strasbourg","Rennes","Clermont","Orléans","Nantes","Besançon","Vincennes","Marseille","Bordeaux","Dijon","Montpellier","Limoges","Metz","Toulouse","Caen","Poitiers","Bayonne"]
#     nb_usines = 3
#     nb_villes = 21
#     nb_modeles = 3
#     Temps_fabrication = np.zeros((nb_modeles,nb_usines))
#     Temps_max = np.zeros(nb_usines)
#     Demandes=np.zeros((3,nb_villes))
#     Distances=np.zeros((nb_usines,nb_villes))

#     with open(datafileName, "r") as file:

#         line = file.readline()  #inutiles, c'est #demande_ville_gamme
#         for v in range (nb_villes): # on lit les demandes par ville et pour chaque gamme 
#             line = file.readline() 
#             lineTab = line.split(", ")
#             Demandes[0][v] = lineTab[0]
#             Demandes[1][v] = lineTab[1]
#             Demandes[2][v] = lineTab[2]

#         line = file.readline()  #inutiles, c'est #distance_ville_usine
#         for v in range (nb_villes): # on lit les demandes par ville et pour chaque gamme 
#             line = file.readline() 
#             lineTab = line.split(", ")
#             for u in range(nb_usines):
#                 Distances[u][v] = lineTab[u]
               

#         line = file.readline()  #inutiles, c'est #capacite_max_production_usine
#         for u in range (nb_usines): # on lit les demandes par ville et pour chaque gamme 
#             line = file.readline() 
#             # lineTab = line.split(", ")
#             Temps_max[u] = line

#         line = file.readline()  #inutiles, c'est #temps_production_usine_gamme
#         for u in range (nb_usines): # on lit les demandes par ville et pour chaque gamme 
#             line = file.readline() 
#             lineTab = line.split(", ")
#             for m in range(nb_modeles):
#                 Temps_fabrication[m][u] = lineTab[m]
                
#         instance = data(Temps_fabrication,Temps_max,Demandes,Distances, nb_usines,nb_modeles,nb_villes,nom_usines,nom_casques,nom_villes,0.034)
#     return instance 


# # data = lecture("data_etude_cas.txt")
# # print(data.Temps_fabrication[0][2])
# # df1 = pd.DataFrame(data.Temps_fabrication)
# # df1.columns = data.nom_casques
# # df2 = pd.DataFrame(data.Temps_max)
# # # df2.rows = data.nom_usines
# # df3 = pd.DataFrame(data.Demandes)
# # df4 = pd.DataFrame(data.Distances)
# # print("essai:",data.Distances[1][15])
# # print("les temps de fabrication : ")
# # print(df1)
# # print("le temps max dispo par usine")
# # print(df2)
# # print("Les demandes : ")
# # print(df3)
# # print("les distances entre usine et magasin : ")
# # print(df4)


# ##########
# # CLASSE SOLUTION 
# import pandas as pd 

# class solution:
#     def __init__(self,qtt_livree,objective_value, nb_usines,nb_modeles,nb_villes, nom_usines,nom_casques,nom_villes,Temps_fabrication,cost_km,Distances):
#         self.qtt_livree = qtt_livree
#         self.objective_value = objective_value
#         self.nb_usines = nb_usines
#         self.nb_modeles  = nb_modeles
#         self.nb_villes = nb_villes
#         self.nom_usines = nom_usines
#         self.nom_casques = nom_casques
#         self.nom_villes = nom_villes
#         self.Temps_fabrication = Temps_fabrication
#         self.cost_km = cost_km
#         self.Distances = Distances
    
#     def print(self):
#         print("La valeur de la solution est : {}".format(self.objective_value))
#         print("-----------")
#         print("La solution est la suivante : ")
#         print("-----------")
#         df1 = pd.DataFrame(self.qtt_livree[0])
#         df1.columns = self.nom_villes
#         df1 = df1.T
#         df1.columns = self.nom_usines
#         df2 = pd.DataFrame(self.qtt_livree[1])
#         df2.columns = self.nom_villes
#         df2 = df2.T
#         df2.columns = self.nom_usines
#         df3 = pd.DataFrame(self.qtt_livree[2])
#         df3.columns = self.nom_villes
#         df3 = df3.T
#         df3.columns = self.nom_usines
#         sol = pd.concat([df1,df2,df3],axis=1,keys = self.nom_casques)
#         print(sol)
#         # for k in range(self.nb_villes):
#         #     print("Le magasin de {} a recu ".format(self.nom_villes[k]))
#         #     for j in range(self.nb_usines):
#         #         print("      depuis l'usine de {}".format(self.nom_usines[j]))
#         #         for i in range(self.nb_modeles):
#         #             print("      {} unités de {}".format(self.qtt_livree[i][j][k],self.nom_casques[i]))
#         #     print(" ")
#         print("------------ temps par usine : ")
#         for j in range(self.nb_usines):
#             nb_heure = 0
#             for i in range(self.nb_modeles):
#                 for k in range(self.nb_villes):
#                     nb_heure += self.qtt_livree[i][j][k] * self.Temps_fabrication[i][j]
#             print("L'usine de {} a travaillé {} heures ".format(self.nom_usines[j],nb_heure))


#         print("------------ demande satisfaite par modele de casque : ")
#         for i in range(self.nb_modeles):
#             nb_casques = 0
#             for j in range(self.nb_usines):
#                 for k in range(self.nb_villes):
#                     nb_casques += self.qtt_livree[i][j][k]
#             print("Il a été fabriqué {} du modele {} ".format(nb_casques,self.nom_casques[i],))

#         print("------------ le cout par usine : ")
#         cout_total = 0
#         for j in range(self.nb_usines):
#             cout_usine = 0
#             for i in range(self.nb_modeles):
#                 for k in range(self.nb_villes):
#                     cout_usine += self.qtt_livree[i][j][k]*self.cost_km * self.Distances[j][k]
#             cout_total += cout_usine
#             print("Le cout de transport depuis l'usine de {} est {} ".format(self.nom_usines[j],cout_usine))
#         print("---------------")
#         print("Le cout total est {} ".format(cout_total))




                
                    

def essai(x=2,y=3):
    return(x+y)

x = 2
y = 2
print(essai(x,y))