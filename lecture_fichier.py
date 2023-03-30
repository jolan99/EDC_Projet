import numpy as np 

# vérifier qu'on a bien le bon ordre entre hauteur et largeur : villes/casques

class data:
    def __init__(self,Temps_fabrication,Temps_max,Demandes,Distances, nb_usines,nb_modeles,nb_villes, nom_usines,nom_casques,nom_villes,cost_km):
        self.Temps_fabrication = Temps_fabrication
        self.Temps_max = Temps_max
        self.Demandes = Demandes
        self.Distances = Distances
        self.nb_usines = nb_usines
        self.nb_modeles  = nb_modeles
        self.nb_villes = nb_villes
        self.nom_usines = nom_usines
        self.nom_casques = nom_casques
        self.nom_villes = nom_villes
        self.cost_km = cost_km

    def print(self):
        print("######### INSTANCE : #########")
        print(" Il y a {} usines, {} villes et {} modèles de casques audios".format(self.nb_usines,self.nb_villes,self.nb_modeles))
        for v in range(self.nb_villes):
            for m in range(self.nb_modeles):
                print("La ville de {} demande {} unités de {}".format(self.nom_villes[v],self.Demandes[m][v],self.nom_casques[m]))
        print(" ")
        for v in range(self.nb_villes):
            for u in range(self.nb_usines):
                print("La ville de {} est à une distance de {}km de l'usine de {}".format(self.nom_villes[v],self.Distances[u][v],self.nom_usines[u]))
        print(" ")
        for u in range(self.nb_usines):
            print("L'usine de {} dispose d'un total de {} heures disponibles".format(self.nom_usines[u], self.Temps_max[u]))
        
        print(" ")
        for u in range(self.nb_usines):
            for m in range(self.nb_modeles):
                print("La production du casque {} dans l'usine de {} nécessite {}h en tout".format(self.nom_casques[m],self.nom_usines[u],self.Temps_fabrication[m][u]))





def lecture(datafileName):

    #ouverture du fichier, le ferme automatiquement à la fin et gère les exceptions
    nom_usines=["Bordeaux","Lyon","Nanterre"]
    nom_casques=["Grosson","Rapdeouf","Zoukafon"]
    nom_villes = ["Lille","Clichy","Reims","Amiens","Strasbourg","Rennes","Clermont","Orléans","Nantes","Besançon","Vincennes","Marseille","Bordaux","Dijon","Montpellier","Limoges","Metz","Toulouse","Caen","Poitiers","Bayonne"]
    nb_usines = 3
    nb_villes = 21
    nb_modeles = 3
    Temps_fabrication = np.zeros((nb_modeles,nb_usines))
    Temps_max = np.zeros(nb_usines)
    Demandes=np.zeros((3,nb_villes))
    Distances=np.zeros((nb_usines,nb_villes))

    with open(datafileName, "r") as file:

        line = file.readline()  #inutiles, c'est #demande_ville_gamme
        for v in range (nb_villes): # on lit les demandes par ville et pour chaque gamme 
            line = file.readline() 
            lineTab = line.split(", ")
            Demandes[0][v] = lineTab[0]
            Demandes[1][v] = lineTab[1]
            Demandes[2][v] = lineTab[2]

        line = file.readline()  #inutiles, c'est #distance_ville_usine
        for v in range (nb_villes): # on lit les demandes par ville et pour chaque gamme 
            line = file.readline() 
            lineTab = line.split(", ")
            for u in range(nb_usines):
                Distances[u][v] = lineTab[u]
               

        line = file.readline()  #inutiles, c'est #capacite_max_production_usine
        for u in range (nb_usines): # on lit les demandes par ville et pour chaque gamme 
            line = file.readline() 
            # lineTab = line.split(", ")
            Temps_max[u] = line

        line = file.readline()  #inutiles, c'est #temps_production_usine_gamme
        for u in range (nb_usines): # on lit les demandes par ville et pour chaque gamme 
            line = file.readline() 
            lineTab = line.split(", ")
            for m in range(nb_modeles):
                Temps_fabrication[m][u] = lineTab[m]
                
        instance = data(Temps_fabrication,Temps_max,Demandes,Distances, nb_usines,nb_modeles,nb_villes,nom_usines,nom_casques,nom_villes,0.034)
    return instance 


lecture("data_etude_cas.txt").print()
