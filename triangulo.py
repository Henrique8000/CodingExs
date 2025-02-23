def triangulo():
    for i in range(1, 6):
        print(i * "*")


def quadrado():
    print()
    for k in range(0, 8):
        if k == 0 or k == 7:
            print("*" * 8)
        else:
            print("*      *")


def triangulo_de_costas():
    print()
    c = 0
    for i in range(6, 0, -1):
        c += 1
        print((" " * i) + ("*" * c))


def triangulo_duplo():
    print()
    c = 0
    for i in range(6, 0, -1):
        c += 2
        print((" " * i) + ("*" * c))


triangulo()
quadrado()
triangulo_de_costas()
triangulo_duplo()
