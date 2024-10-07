preco = float(input())

def desconto_de_10(preco):
    calc_desct = preco - (preco * 5 / 100)
    return calc_desct


print(f"{desconto_de_10(preco):.2f}")
