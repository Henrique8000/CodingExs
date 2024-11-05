#Escreva um programa que exiba todos os números
#pares de 0 até o número informado pelo usuário.

def imprime_n_par(x1, x):
    c = 0
    t = x
    # verifica se a contagem será em ordem crescente ou decrecente
    if x1 > x:
        c -= 2  # decrecente
        t -= 1
    else:
        c = 2   # crecente
        t += 1

    if x1 % 2 == 1:
        x1 -= 1

    for i in range(x1, t, c):
        print(i)


def imprime_n_impar(x1, x):
    w = 0
    #verifica se a contagem será em ordem crescente ou decrecente
    if x1 > x:
       w -= 2
    else:
        w = 2
    #verifica se o x1 é par, se for, vai somar mais um e contar.
    if x1 % 2 == 0:
        x1 += 1

    for a in range(x1, x+1, w):
        print(a)


n = int(input())
x1 = int(input())
x = int(input())
v_seq = int(input("Digite 0 para PAR e 1 para IMPAR: "))

if v_seq == 0:
    imprime_n_par(x1, x)

elif v_seq == 1:
    imprime_n_impar(x1, x)

'''
print()
imprime_n_par(n)
print()
imprime_n_impar(x1, x)
'''