menu = True

while menu:
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    opcao = int(input())

    if opcao == 1:
        s1 = float(input())
        s2 = float(input())
        print(f'{s1 + s2:.2f}')

    elif opcao == 2:
        sub1 = float(input())
        sub2 = float(input())
        print(f'{sub1 - sub2:.2f}')

    elif opcao == 3:
        mult1 = float(input())
        mult2 = float(input())
        print(f'{mult1 * mult2:.2f}')

    elif opcao == 4:
        div1 = float(input())
        div2 = float(input())
        print(f'{div1 / div2:.2f}')

    elif opcao == 5:
        print("Saindo...")
        menu = False

    else:
        print("Digite uma opção válida de 1 até 5!")