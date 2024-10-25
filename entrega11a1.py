def main():
    kmi = int(input())  #quilometragem inicial
    kmf = int(input())  #quilometragem final
    ql = int(input())  #quantidade em litros de gasolina gasta
    preco = float(input())  #valor gasto em gasolina (6,26 o litro) dia 25/10/2024

    calcula(kmi, kmf, ql, preco)


def calcula(a, b, c, d):
    total_distancia = b - a
    comsumo_medio = total_distancia / c
    valor_gasto = c * d

    print(f"{total_distancia}\n{comsumo_medio:.2f}\n{valor_gasto:.2f}")


main()
