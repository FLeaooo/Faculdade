import math
import matplotlib.pyplot as plt

def outra_lista(Lista):
    lista_retornar = []
    for x in Lista:
        lista_retornar.append(x*x)
    
    return lista_retornar


L0 = list(range(101))

L1 = outra_lista(L0)


lista_seno = [math.sin(math.radians(x)) for x in L0]
lista_cos = [math.cos(math.radians(x)) for x in L0]

l1_quadrado = [x**2 for x in L0]
L1_raiz = [math.sqrt(x) for x in L0]

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8,10))

ax1.plot(L0, lista_seno, label="Seno")
ax1.plot(L0, lista_cos, label="Coseno")


ax2.plot(L0, l1_quadrado, label="Ao quadrado")
ax2.legend()

ax3.plot(L0, L1_raiz, label="Raiz")
ax3.set_ylim(0, 100)
ax3.legend()



plt.tight_layout()
plt.show()



print(f"Lista 0 = {L0}")
print(f"Lista 1 = {L1}")
print(f"Seno da Lista 0 = {lista_seno}")
print(f"Coseno da Lista 0 = {lista_cos}")