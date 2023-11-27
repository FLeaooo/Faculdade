"""
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
"""

while True:
    nome = input("Nombre:")
    if len(nome) >= 3:
        break
    else:
        print("Nome precisa ser maior que 3 letras")
    

idade = int(input("Idade:"))
while idade <= 0 or idade > 150:
    print("Insira idade valida")
    idade = int(input("Idade:"))
    

