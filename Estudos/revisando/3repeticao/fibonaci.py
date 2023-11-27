#1,1,2,3,5,8 =  F1(1) F2(1) F3(2)
#fn+2 = fn+1 + fn


fib = 1
B = 1
C = 0
fib_list = [1]

for i in range(1, 100, 1):
    fib = B + C
    C = B
    B = fib
    fib_list.append(fib)
    print(fib)

"""
    Ta vendo, vtnc seu fdp, pega o negocio, faz no papel, pensa como deve funcionar
eae escreve o codigo, tu ficou 20 min tentando entendenr para resolver, quando para para 
pensar e resolver faz em 1 min  
"""