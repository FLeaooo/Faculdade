# Calcular a area a baixo de uma curva 
# Metodo de monte carlo

import numpy as np

# Quantidade de pontos sorteados
n_sorteados = 900000

Nin = 0
for i in range(n_sorteados):
    x = np.random.rand(1) # 0 - 1
    y = np.random.rand(1) # 0 - 1

    if y**2 + x**2 <= 1:
        Nin = Nin + 1

PI = 4*Nin / n_sorteados

print(PI)