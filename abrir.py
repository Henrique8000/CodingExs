def main():
    exibe_msg()
    arquivo_path()
    caminho_arquivo = arquivo_path()
    abre_arquivo(caminho_arquivo)
    arquivo = abre_arquivo()
    caca_palavra(arquivo)

def exibe_msg():
     print('vai começar o caça palavras!!!\n')


def arquivo_path():
    caminho = input("Insira o caminho relativo do arquivo: ")

def abre_arquivo(n_arq):
    with open(n_arq, "r") as arquivo:
        arq = arquivo.readlines()
        return arq


def caca_palavra(arquivo, recebe):
    n = 0
    for frase in arquivo:
        if recebe in frase:
            n += 1
    if n != 0:
        print(f"\nAchei tantos '{frase}': {n}")
    return n



main()

