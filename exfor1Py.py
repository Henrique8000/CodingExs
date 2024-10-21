#Escreva um programa que exiba todos os números
#pares de 0 até o número informado pelo usuário.

def imprime_n_par(n):
    for i in range(0, n + 1, 2):
        print(i)


n = int(input())
imprime_n_par(n)