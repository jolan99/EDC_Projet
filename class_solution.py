import pandas as pd 
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
        
    def sol_to_df(self):
        df1 = pd.DataFrame(self.qtt_livree[0])
        df1.columns = self.nom_villes
        df1 = df1.T
        df1.columns = self.nom_usines
        df2 = pd.DataFrame(self.qtt_livree[1])
        df2.columns = self.nom_villes
        df2 = df2.T
        df2.columns = self.nom_usines
        df3 = pd.DataFrame(self.qtt_livree[2])
        df3.columns = self.nom_villes
        df3 = df3.T
        df3.columns = self.nom_usines
        
        df1bis = pd.concat([df1.Bordeaux,df2.Bordeaux,df3.Bordeaux],axis=1,keys = self.nom_casques)
        df2bis = pd.concat([df1.Lyon,df2.Lyon,df3.Lyon],axis=1,keys = self.nom_casques)
        df3bis = pd.concat([df1.Nanterre,df2.Nanterre,df3.Nanterre],axis=1,keys = self.nom_casques)
        sol = pd.concat([df1bis,df2bis,df3bis],axis=1,keys = self.nom_usines)
        return sol
    
    def print(self):
        
        print("La solution est la suivante : ")
        print("-----------")
       
        
        
        print(self.sol_to_df()) # affiche le dataframe
        with open('solutions.txt', 'w') as f:
            dfAsString = self.sol_to_df().to_string(header=True, index=True)
            f.write(dfAsString)
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