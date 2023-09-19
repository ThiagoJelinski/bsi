## 1- Crie um dicionário que contenha os nomes de 10 pessoas e suas respectivas idades.

person = { 
    'Joao' : 17 ,  
    'Marcia' : 18 , 
    'Gustavo' : 19
}

## 2- Imprima o nome e a idade de todas as pessoas no dicionário.

print(person)

## 3- Crie uma função que receba um nome como parâmetro e retorne a idade da pessoa correspondente no dicionário.

def search_age():
    people = input('Digite um nome: ')
    if people in person:
        age = person[people]
        return f"A idade do(a) {people} é {age}"
    else:
        return f"Nome:''{people}'' não encontrado!"
    

print(search_age())

## 4- Crie uma função que receba um nome e uma nova idade como parâmetros e atualize a idade da pessoa correspondente no dicionário.
def new_age():
    people = input('Digite um nome: ')
    if people in person:
        new_age = int(input('Digite uma nova idade: '))
        person[people] = new_age
    return new_age
print(new_age())

## 5- Crie uma função que remova uma pessoa do dicionário.

def remove_person():
    people = input('Digite um nome: ')
    if people in person:
        del person[people]
        return f"Dicionario atualizado!{people} foi removido com sucesso."
    else:
        return "Ninguem foi removido."
print(remove_person())

## 6- Crie uma função que retorne a quantidade de pessoas no dicionário.
def size():
    size_dict = len(person)
    return f"A quantidade de pessoas no dicionario é : {size_dict} pessoas."
print(size())
## 7- Crie uma função que retorne a média das idades das pessoas no dicionário.
def avarege_age():
    ages = person.values()
    return f"A media das idades é: {sum(ages) / len(ages)}"
print(avarege_age())
## 8- Crie uma função que retorne a pessoa mais velha do dicionário.
def high_ages():
    high_age = max(person.values())
    return f"A idade mais velha é: {high_age} anos"
print(high_ages())

## 9 - Crie uma função que retorne a pessoa mais nova do dicionário.
def lower_ages():
    lower_age = min(person.values())
    return f"A idade mais nova é: {lower_age} anos"
print(lower_ages())

## 10 - Crie uma função que retorne uma lista com as pessoas cujo nome começa com a letra "J".
def search_J(person):
    names_J = []
    for name in person:
        if name.startswith("J"):
            names_J.append(name)
    return f"Lista com os nomes que começam com J: {names_J}"
print(search_J(person)) 
    