salaria_atual = float(input("Qual é o seu salário atual?: R$"))

# usuário irá ganhar um almento de 15% no salario
while salaria_atual != 0:

    if salaria_atual < 4000:
        almento = salaria_atual + (salaria_atual * 15 / 100)
        print(f"Com o aumento de 15% no salário, você agora ganha R${almento:.2f}")

    else:
        print("Pelo seu salário informado, você não se enquadra nas condições de almento")

    salaria_atual = float(input("Qual é o seu salário atual?: R$"))