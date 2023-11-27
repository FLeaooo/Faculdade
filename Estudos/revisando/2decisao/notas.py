# -*- coding: utf-8 -*-

name = input("Name:")
nota1 = float(input("Nota 1:"))
nota2 = float(input("Nota 2:"))

media = (nota1 + nota2) / 2 


if media >= 9.0:
    print("Sua nota é A\nEsta aprovado")
elif media >= 7.5:
    print("Sua nota é B\nEsta aprovado")
elif media >= 6.0:
    print("Sua nota é C\nEsta aprovado ")
elif media >= 4.0:
    print("Sua nota é D\nEsta de recuperação ")
else:
    print("Sua nota é E\nEsta reprovado")
