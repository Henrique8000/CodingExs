#Uma determinada marca de TV apresenta duas linhas - série 100 e série 200. A distância ideal entre o sofá e a TV
#depende do tamanho da tela da TV e também da própria série, conforme mostram as tabelas, a seguir.
#Implemente um programa, em python, onde o cliente digita a distância (float) ideal entre o sofá e o TV e, também, a série (inteiro)
#escolhida, nesta ordem. O programa deve calcular o tamanho ideal da tela da TV, de acordo com as informações das tabelas acima.
#Se o usuário digitar um número de série que não existe, deverá aparecer, exatamente, a seguinte mensagem: "Esta série não existe" .


d = float(input())
s = int(input())

if s == 100:
    if d <= 1.4 and d >= 0.1:
        print("32")
    elif d <= 2.6 and d >= 1.5:
        print("37")
    elif d > 42:
        print("42")
elif s == 200:
    if d >= 0.1 and d <= 2.8:
        print("42")
    elif d >= 2.9 and d <= 3.6:
        print("50")
    elif d > 3.6:
        print("61")

else:
    print("Esta série não existe")