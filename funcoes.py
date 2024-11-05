from math import sqrt, gcd


def recebe_dois_nuemros(n1, n2):
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um numero: '))

def soma_dois_numeros(n1, n2):
    recebe_dois_nuemros(n1, n2)
    soma = n1 + n2
    return soma


def multiplica_dois_numeros(n1, n2):
    mult = n1 * n2
    return mult


def divisao_dois_numeros(n1, n2):
    divisao = n1 / n2
    return divisao


def divsao_dois_n_truncada(n1, n2):
    divtrunc = n1 // n2
    return divtrunc


def raiz_de_dois_numeros(n1, n2):
    raiz1 = sqrt(n1)
    raiz2 = sqrt(n2)
    return raiz1, raiz2


def subtracao_de_dois_numeros(n1, n2):
    sub = n1 - n2
    return sub


def algoritmo_de_euclides(n1, n2):
    mdc = gcd(n1, n2)
    return mdc


main_menu = True

while main_menu:
    print("==========")
    print("Digite uma opção\n")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisao")
    print("5. Divisao Truncada")
    print("6. Raiz Quadrada")
    print("7. MDC de dois Números")
    print("8. Sair")
    opcao = int(input(">>>"))

    if opcao == 1:
        s = soma_dois_numeros(n1, n2)
        print(f"{n1} + {n2} = {s}")

    elif opcao == 2:
        print(f"\nResultado da subtração entre os números: {subtracao_de_dois_numeros(n1, n2)}\n")

    elif opcao == 7:
        print(f"\nMDC entre {n1} e {n2} = {algoritmo_de_euclides(n1, n2)}\n")

    elif opcao == 8:
        print("Finalizando o programa....")
        break

    else:
        print("Digite uma opção entre 1 e 8")
