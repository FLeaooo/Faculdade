import random

# Criando lista1 com 10 elementos de 1 a 10
L1 = []

for i in range(10):
    Num_str = str(i + 1)
    L1.append(Num_str)

print(L1)


# Criando dicionario 1 com 10 elementos chaves sendo int e valor string

D1 = {}
for i in range(10):
    D1[i] = str(i)

print(D1)



# Criando Dicionario 2 palavras aleatorias como chave e valor elas dividas na lista

with open(r"C:\FernandoLeao\Programacao\Faculdade\Python\tarefas\words.txt", "r") as file:
    # Lendo linhas do arquivo
    lines = file.readlines()

    #Embaralhando as linhas
    random.shuffle(lines)

    # Listas de palavras
    words_list = [word.strip() for word in lines[:10]]

print(words_list)

D2 = {}
for word in words_list:
    word_split_list = [char for char in word]
    D2[word] = word_split_list

print(D2)

# Dicionario 3, resolvi fazer diferente
D3 = {"Lista1":L1, "Dicionario1":D1, "Dicionario2":D2}
print(D3)