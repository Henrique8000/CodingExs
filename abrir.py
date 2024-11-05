def main():
    caminho = input("Insira o caminho do arquivo que você deseja abrir: ").strip()
    plv = input("Qual palavra você deseja contar? ").strip()

    if plv != "" and caminho != "":
        arq = abre_arquivo(caminho)
        qtd = caca_palavra(plv, arq)
        print(f"Achei {qtd} vezes a palavra '{plv}'")
    else:
        print("Obrigado, volte sempre!")


def abre_arquivo(path):
    with open(f"{path}", "r", encoding="utf-8") as arquivo:
        texto = arquivo.readlines()
        return texto


def caca_palavra(palavra, arquivo):
    n = 0
    for i in arquivo:
        if palavra in i:
            n += 1
    return n


main()
