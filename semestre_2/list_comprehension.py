import random

#1- Crie uma lista com os números de 1 a 10 usando compreensão de lista.

lista = [n for n in range(1, 11)]
print(lista)

#2- Crie uma lista com os números ímpares de 1 a 50.

impares = [n for n in range(1, 51, 2)]
print(impares)

#3- Crie uma lista com as letras maiúsculas de uma string qualquer.

fruits = ["apple", "banana", "grape", "fig"]
capitalize_string = [x.capitalize() for x in fruits]
print(capitalize_string)

#4- Crie uma lista com o comprimento de cada palavra em uma string.

length_words = len([x for x in fruits])
print(length_words)

#5- Crie uma lista com os números divisíveis por 3 e 5 de 1 a 30.

divisiveis = [n for n in range(1, 31) if n % 3 == 0 and n % 5 == 0]
print(divisiveis)

#6- Crie uma lista com as palavras de uma string que tenham mais de 3 letras.

more_three_words = [x for x in fruits if len(x) > 3]
print(more_three_words)

#7- Crie uma lista com os números primos de 1 a 20. Dica: use uma função para verificar se o número é primo ou não.

duplicated_numbers = [n for n in range(2, 21) for i in range(2, n) if n % i != 0]

primes = []
[primes.append(num) for num in duplicated_numbers if num not in primes and duplicated_numbers.count(num) == num - 2]

print(primes)

#8- Crie uma lista com as datas de todos os dias de janeiro em um ano bissexto (considerando que um ano bissexto é divisível por 4).

january_dates = [f"{f'0{day}' if day < 10 else day}/01/2020" for day in range(1, 32)]
print(january_dates)

#9- Crie uma lista de strings com os primeiros 10 nomes da lista de nomes.

nomes = [
    "Alice", "Bob", "Carlos", "Diana", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Julia",
    "Lara", "Miguel", "Natália", "Oscar", "Priscila",
    "Quiteria", "Rafael", "Sofia", "Thiago", "Ursula"
]

first_ten_names = [x for x in nomes[:10]]
print(first_ten_names)

#10- Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de nomes, mas com as primeiras letras maiúsculas.

first_10_capitalized_names = [name.capitalize() for name in nomes[:11]]
print(first_10_capitalized_names)

#11- Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de nomes, mas sem as vogais.

def remove_vowels(name):
    vowels = "aeiou"
    return "".join([char for char in name if char not in vowels])


first_ten_names = [remove_vowels(name) for name in nomes[:10]]
print(first_ten_names)


#12- Concatenar elementos de sub-listas em uma única lista

fruits_and_names = [y for x in [fruits, nomes] for y in x]
print(fruits_and_names)

#13- Criar um dicionário a partir de duas listas

automobiles = {
    "Carros": [input("Informe um carro: ") for _ in range(2)],
    "Motos": [input("Informe uma moto: ") for _ in range(2)],
}

print(f"Esse é o dicionário: {automobiles}")