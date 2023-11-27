import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Filmes de "herois"
# -serie trilogia a filme unico
# antigo a recente
# mais infantil - romance(jovem) - Sombrio 



categoria = ctrl.Antecedent(np.arange(0, 11, 1), 'categoria')
tematica = ctrl.Antecedent(np.arange(0, 11, 1), 'tematica')
budget = ctrl.Antecedent(np.arange(0, 11, 1), 'budget')
recomendacao = ctrl.Consequent(np.arange(0, 101, 1) 'recomendacao')




