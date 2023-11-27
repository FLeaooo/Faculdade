fat = int(input("Insira o fatorial: "))
result = 1

for i in range(1, fat+1):
    result *= i
    print(result)