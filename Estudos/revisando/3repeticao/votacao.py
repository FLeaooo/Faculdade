n_votos = 0
media = 0
maior = 0
menor = 10

while True:
    voto = float(input("Valor do voto (-1 para): "))

    if voto < 0:
        break

    n_votos += 1
    media += voto
    if voto > maior:
        maior = voto

    if voto < menor:
        menor = voto
    
print(f"Total de votos: {n_votos}")
print(f"Media dos votos: {media/n_votos}")
print(f"Menor nota: {menor}")
print(f"Maior nota: {maior}")



