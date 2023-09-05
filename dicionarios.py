## 1- Crie um dicionário que contenha os nomes de 10 pessoas e suas respectivas idades.

person = { 
    'Joao' : 17 ,  
    'Marcia' : 18 , 
    'Gustavo' : 19
}

## 2- Imprima o nome e a idade de todas as pessoas no dicionário.

print(person)

## 3- Crie uma função que receba um nome como parâmetro e retorne a idade da pessoa correspondente no dicionário.

people = input('Digite um nome: ')
if people in person:
    age = person[people]
    print(f"A idade do(a) {people} é {age}")
else:
    print(f"Nome:''{people}'' não encontrado!")

## 4- Crie uma função que receba um nome e uma nova idade como parâmetros e atualize a idade da pessoa correspondente no dicionário.

people = input('Digite um nome: ')
if people in person:
    new_age = int(input('Digite uma nova idade: '))
    person[people] = new_age
print (person)

## 5- Crie uma função que remova uma pessoa do dicionário.

people = input('Digite um nome: ')
if people in person:
    del person[people]
    print(f"Dicionario atualizado!{people} foi removido com sucesso.")
else:
    print("Ninguem foi removido.")

## 6- Crie uma função que retorne a quantidade de pessoas no dicionário.

size_dict = len(person)
print(f"A quantidade de pessoas no dicionario é : {size_dict} pessoas.")

## 7- Crie uma função que retorne a média das idades das pessoas no dicionário.

ages = person.values()
print(f"A media das idades é: {sum(ages) / len(ages)}")

## 8- Crie uma função que retorne a pessoa mais velha do dicionário.

high_age = max(person.values())
print(f"A idade da pessoa mais velha é: {high_age}")