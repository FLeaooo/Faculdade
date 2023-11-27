import matplotlib.pyplot as plt

"""Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
 Valide a entrada e permita repetir a operação."""



habitantes_A = int(input("Habitantes do pais A:"))
taxa_A = float(input("Taxa pais A:"))


habitantes_B = int(input("Habitantes do pais B:"))
taxa_B = float(input("Taxa do pais B:"))

anos = []
polulacao_A = []
polulacao_B = []

if habitantes_A == habitantes_B:
    print("A população ja é igual")
elif taxa_A == taxa_B:
    print("A taxa de crescimento é igual ninguem irar ultrapassar ninguem")
elif habitantes_A > habitantes_B and taxa_A > taxa_B:
    print("Pais A tem mais habitantes e taxa maior entao nunca sera ultrapassado")
elif habitantes_B > habitantes_A and taxa_B > taxa_A:
    print("Pais B tem mais habitantes e taxa maior entao nunca sera ultrapassado")
else:
    ano = 0
    while True:
        habitantes_A += habitantes_A * taxa_A / 100
        habitantes_B += habitantes_B * taxa_B / 100

        ano += 1

        anos.append(ano)
        polulacao_A.append(habitantes_A)
        polulacao_B.append(habitantes_B)
        if habitantes_A <= habitantes_B:
            break
    print(f"População total pais A: {habitantes_A}")
    print(f"População total pais B: {habitantes_B}")
    print(f"Pais B ultrapassou em {ano} anos")


plt.plot(anos, polulacao_A, label='Pais A')
plt.plot(anos, polulacao_B, label='Pais B')
plt.legend()
plt.show()