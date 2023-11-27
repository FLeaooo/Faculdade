primo = int(input("Insira o primo:"))

flag = 0
for i in range(2, primo):
    if primo % i == 0:
        flag += 1
        break

if flag == 0:
    print("É primo")
else:
    print("Não é primo")

