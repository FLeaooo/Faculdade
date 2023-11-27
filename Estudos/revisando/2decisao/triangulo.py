A = float(input("Lado A:"))
B = float(input("Lado B:"))
C = float(input("Lado C:"))

if A + B >= C and A + C >= B and B + C >= A:
    print("É triangulo")
    if A == B and A == C:
        print("Equilatero")
    elif A == B or A == C or B == C:
        print("Isoceles")
    else:
        print("Escaleno")
else:
    print("Não é triangulo")
