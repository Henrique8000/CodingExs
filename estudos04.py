#Um usuário deseja um algoritmo em que possa escolher que tipo de média deseja
#calcular a partir de 3 notas.
#Faça um algoritmo que leia as notas, a opção escolhida pelo usuário e calcule a média.

n1 = float(input('Insira a nota: '))
n2 = float(input('Insira a nota: '))
n3 = float(input('Insira a nota: '))

mA = (n1 + n2 + n3) / 3

mP = ((n1 * 3) + (n2 * 4) + (n3 * 5)) / (3 + 4 + 5)

menu = True


while menu:
    print('[1] Média aritmética')
    print('[2] Média ponderada')
    print('[3] Sair')
    opcao = int(input('\nDigite uma opção: '))

    if opcao == 1:
        print(f'{mA:.2f}')

    elif opcao == 2:
        print(f'{mP:.3f}')

    elif opcao == 3:
        print('Finalizando....')
        break

    else:
        print('\nDigite uma opção válida\n')
