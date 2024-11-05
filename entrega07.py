qntAluno = int(input())
i = 0
soma = 0

if qntAluno <= 0:
    print("NÃO HOUVE PROCESSAMENTO")
else:
    while(i < qntAluno):
        nota = int(input())
        if nota >= 6:
            print("PARABÉNS, VOCÊ ESTÁ APROVADO")
        i +=1
        soma += nota
    media = soma / i
    print(f"{media:.2f}")