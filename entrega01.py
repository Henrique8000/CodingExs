#Faça um programa em python que calcule e mostre o IMC (índice de massa corporal) de uma pessoa, c
# onsiderando que ela irá dizer qual o seu peso (em Kg) e a sua altura (em metros), nesta ordem exatamente.
#O valor de imc deverá ter, exatamente, 2 casas decimais
from math import pow

peso = int(input())
altura = float(input())


imc = peso / (altura ** 2)


print(f"{imc:.2f}")

menu = True