import localsolver
import sys
from lecture_fichier import *
from class_solution import *

with localsolver .LocalSolver() as ls:
    m = ls.model
    #Dimensions
    
    instance = lecture("data_etude_cas.txt") 

    # variables 
    x = [[[m.int(0,10000000000)for k in range(instance.nb_villes)]for j in range(instance.nb_usines)]for i in range(instance.nb_modeles)] # nb employés
    
    for i in range(instance.nb_modeles):
        for j in range(instance.nb_usines):
            for k in range(instance.nb_villes):
                x[i][j][k].set_name('qtt_envoyee de casques {} depuis l usine de {} à  la ville de {}'.format(i,j,k))
                
    #Data
   
    for i in range(instance.nb_modeles): # on doit envoyer au moins la quantité demandée
        for k in range(instance.nb_villes):
            m.constraint(m.sum(x[i][j][k] for j in range(instance.nb_usines)) >= instance.Demandes[i][k])

    for j in range(instance.nb_usines):   # on ne doit pas dépasser le nombre d'heure de fabrication possible
        m.constraint(m.sum(m.sum(x[i][j][k]*instance.Temps_fabrication[i][j] for i in range(instance.nb_modeles)) for k in range(instance.nb_villes)) <= instance.Temps_max[j])



    m.minimize(m.sum(m.sum(m.sum(x[i][j][k]*instance.Distances[j][k]*instance.cost_km for i in range(instance.nb_modeles))for j in range(instance.nb_usines))for k in range(instance.nb_villes)))

    m.close()

    if len(sys.argv) >= 3:
        ls.param.time_limit = int(sys.argv[2])
    else:
        ls.param.time_limit = 2
    ls.solve()
    # import ipdb;ipdb.set_trace()
    qtt_livree = np.zeros((instance.nb_modeles,instance.nb_usines,instance.nb_villes))
    for k in range(instance.nb_villes):
            for j in range(instance.nb_usines):
                for i in range(instance.nb_modeles):
                    qtt_livree[i][j][k] = x[i][j][k].value

    objective_value = ls.solution.get_objective_bound(0)

                   
    Solution = solution(qtt_livree,objective_value, instance.nb_usines,instance.nb_modeles,instance.nb_villes, instance.nom_usines,instance.nom_casques,instance.nom_villes,instance.Temps_fabrication,instance.cost_km,instance.Distances)
    Solution.print()
                    