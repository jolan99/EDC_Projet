class solution:
    def __init__(self,qtt_livree,objective_value, nb_usines,nb_modeles,nb_villes, nom_usines,nom_casques,nom_villes,Temps_fabrication,cost_km,Distances):
        self.qtt_livree = qtt_livree
        self.objective_value = objective_value
        self.nb_usines = nb_usines
        self.nb_modeles  = nb_modeles
        self.nb_villes = nb_villes
        self.nom_usines = nom_usines
        self.nom_casques = nom_casques
        self.nom_villes = nom_villes
        self.Temps_fabrication = Temps_fabrication
        self.cost_km = cost_km
        self.Distances = Distances
    
    def print(self):
        print("La valeur de la solution est : {}".format(self.objective_value))
        print("-----------")
        print("La solutione est la suivante : ")
        print("-----------")
        for k in range(self.nb_villes):
            print("Le magasin de {} a recu ".format(self.nom_villes[k]))
            for j in range(self.nb_usines):
                print("      depuis l'usine de {}".format(self.nom_usines[j]))
                for i in range(self.nb_modeles):
                    print("      {} unités de {}".format(self.qtt_livree[i][j][k],self.nom_casques[i]))
            print(" ")
        print("------------ temps par usine : ")
        for j in range(self.nb_usines):
            nb_heure = 0
            for i in range(self.nb_modeles):
                for k in range(self.nb_villes):
                    nb_heure += self.qtt_livree[i][j][k] * self.Temps_fabrication[i][j]
            print("L'usine de {} a travaillé {} heures ".format(self.nom_usines[j],nb_heure))


        print("------------ demande satisfaite par modele de casque : ")
        for i in range(self.nb_modeles):
            nb_casques = 0
            for j in range(self.nb_usines):
                for k in range(self.nb_villes):
                    nb_casques += self.qtt_livree[i][j][k]
            print("Il a été fabriqué {} du modele {} ".format(nb_casques,self.nom_casques[i],))

        print("------------ le cout par usine : ")
        cout_total = 0
        for j in range(self.nb_usines):
            cout_usine = 0
            for i in range(self.nb_modeles):
                for k in range(self.nb_villes):
                    cout_usine += self.qtt_livree[i][j][k]*self.cost_km * self.Distances[j][k]
            cout_total += cout_usine
            print("Le cout de transport depuis l'usine de {} est {} ".format(self.nom_usines[j],cout_usine))
        print("---------------")
        print("Le cout total est {} ".format(cout_total))




                
                    
