#Escreva uma função python para imprimir todos os valores quadrados dos números entre
#1 e n (ambos incluídos). O usuário deve informar o valor de n.

def imprime_n_quadrado(n1, n2):
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    n = n1 + n2
    for i in range(1, n):
        print(n ** 2)

