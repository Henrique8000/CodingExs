"""
Lambda function = A small anonymous function for a one time use (throw away function)
They take any number of arguments, but have only 1 expression
Helps keep the namespace clean and is useful with higher-order functions
'sort()', 'map()', 'filter()', 'reduce()'
lambda parameters: expression
"""

p_ou_i = lambda x: "É par!" if x % 2 == 0 else "É ímpar"
add = lambda x, y: x + y

print(p_ou_i(2))
print("\n", add(2, 2))

#map (function, collection) = Applies a given function to all items in a collection
"""
def calc_fahrenheit(temp):
    return (temp * 9/5) + 32
"""

preco_bruto_ingressos = [30.00, 15.00, 10.00]

temps_celsius = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

temps_fahrenheit = list(map(lambda temp: (temp * 9 / 5) + 32, temps_celsius))
desconto_promo_cinema = list(map(lambda ing: ing - (ing * 5 / 100), preco_bruto_ingressos))
#temps_fahrenheit = list(map(calc_fahrenheit, temps_celsius))

print(desconto_promo_cinema)
print(temps_fahrenheit)

#filter(function, collection) = return all elements that pass a condition

"""
def is_passing(grade):
    return grade >= 60
"""

grades = [91, 32, 83, 44, 75, 56, 67]

#passing_grades = list(filter(is_passing, grades))
passing_grades = list(filter(lambda grade: grade >= 60, grades))

print(passing_grades)

#reduce(function, collection) = Reduces elements in a collection to a single value
#                           For loop is better in most cases
#                           Reduce is better for a functional approach + readability

from functools import reduce

"""
def soma(x, y):
    return x + y
"""

prices = [19.99, 1.00, 5.75, 12.99, 10.99]
nomes = ["Henrique", "Lucas", "Amanda", "Joao"]

#total = reduce(add, prices)
total = reduce(lambda x, y: x + y, prices)
nomes_juntos = reduce(lambda a, b: a + " " + b, nomes)

print(f"${total}")
print(nomes_juntos)

#SORTING IN PYTHON .sort() or sorted()
#Lists[], Tuples, Dictionaries{"":""}, Objects

#---------- LISTS ----------

fruits = ["banana", "orange", "apple", "cocomut"]

#fruits.sort()
fruits.sort(reverse=True)
print(fruits)

# ---------- TUPLES ----------

fruits2 = ("banana", "orange", "apple", "coconut")

fruits2 = tuple(sorted(fruits2, reverse=True))
print(fruits2)

#---------- DICTIONARIES ---------

fruits3 = {"banana": 105,
           "orange": 73,
           "apple": 72,
           "coconut": 354}

#fruits3 = dict(sorted(fruits3.items())) # as chaves do dicionario estão organizadas em ordem alfabética
#fruits3 = dict(sorted(fruits3.items(), key=lambda item: item[0], reverse=True)) # organizando as caheves em ordem
#                                                                                 alfabética reversa
#fruits3 = dict(sorted(fruits3.items(), key=lambda item: item[1])) # organizando os valores em ordem ascendente
fruits3 = dict(
    sorted(fruits3.items(), key=lambda item: item[1], reverse=True))  # organizando os valores em ordem reversa

print(fruits3)


# ---------- OBJECTS -----------

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories}"


fruits4 = [Fruit("banana", 105),
           Fruit("apple", 72),
           Fruit("orange", 73),
           Fruit("coconut", 354)]

#fruits4 = sorted(fruits4, key=lambda fruit: fruit.name)
#fruits4 = sorted(fruits4, key=lambda fruit: fruit.name, reverse=True)
#fruits4 = sorted(fruits4, key=lambda fruit: fruit.calories)
fruits4 = sorted(fruits4, key=lambda fruit: fruit.calories, reverse=True)

print(fruits4)
