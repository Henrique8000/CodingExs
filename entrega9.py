qtd_empregados = int(input())
qtd_emp10 = 0
total_salario = 0
soma = 0

for i in range(0, qtd_empregados, 1):
    salario_func = float(input())

    if salario_func >= 3000.00:
        reajuste1 = (salario_func * 8 / 100) + salario_func
        total_salario += reajuste1
        print(f'{reajuste1:.2f}')

    elif salario_func < 3000.00 and salario_func >= 2000.00:
        qtd_emp10 += 1
        reajuste2 = (salario_func * 10 / 100) + salario_func
        total_salario += reajuste2
        print(f'{reajuste2:.2f}')

    else:
        reajuste3 = (salario_func * 12 / 100) + salario_func
        total_salario += reajuste3
        print(f'{reajuste3:.2f}')
    soma += 1

print(qtd_emp10)

media = total_salario / soma
print(f'{media:.2f}')
