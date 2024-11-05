#Crie um algoritmo que faça a conversão de graus celsius para Farenheint e Kelvin. Para
#isso, pergunte ao usuário o valor em Celsius e retorne os correspondentes calculados
#em Farenheint e Kelvin

celsius = int(input('Digite a temperatura atual em Celsius: '))

converte_em_farenheint = (celsius * (9 / 5)) + 32
converte_em_kelvin = celsius + 273.15

print(f'{celsius}°C em Farenheint são {converte_em_farenheint}°F\nEm Kelvin é {converte_em_kelvin}')
