import math
a = int(input('Entre a:'))
b = int(input("Entre b:"))
c = int(input("Entre c:"))

delta = b**2 - 4*a*c

print(f"Valor de delta = {delta}")
if delta < 0:
    print("Nao tem raizes reais")
elif delta == 0:
    x = -b /(2*a)
    print(f"Duas raizes iguais = {x}")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
