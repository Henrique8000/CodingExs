"""
Script para ataque de força bruta que gera senhas aleatórias
sem caracteres especiais.
"""
import random


def main():
    senha: str = "1234"

    senha_gerada = brute_force_attk()

    count = 1

    while senha_gerada != senha:
        print(f"Tentativa {count} : {senha_gerada}")

        senha_gerada = brute_force_attk()
        count += 1

    print("\nACESSO VÁLIDO, BEM-VINDO(A)")
    print(f"A senha do usuário era: {senha_gerada}")


def brute_force_attk():
    l_caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
                    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    s = random.choices(l_caracteres, k=4)
    separador = ""
    senha_concatenada = separador.join(s)

    return senha_concatenada


main()
