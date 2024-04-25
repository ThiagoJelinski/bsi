#Pratica 07

class Usuario:
    pontos = 0
    num_art = 0

    def def_num_art(self, num):
        if isinstance(num, int):
            self.num_art = num
        else:
            print("Erro: O número de artigos deve ser um inteiro.")

    def get_num_art(self):
        return self.num_art

    def calc_point(self):
        pass

class Autor(Usuario):
    def calc_point(self):
        return self.num_art * 10 + 20

class Editor(Usuario):
    def calc_point(self):
        return self.num_art * 6 + 15

# Teste
autor1 = Autor()
autor1.def_num_art(8)
print("Pontuação do autor:", autor1.calc_point())

editor1 = Editor()
editor1.def_num_art(15)
print("Pontuação do editor:", editor1.calc_point())

#Lista 03

class Animal:
    def falar(self):
        return "O animal faz algum som."


class Cachorro(Animal):
    def falar(self):
        return "Au au!"


class Gato(Animal):
    def falar(self):
        return "Miau!"


class Peixe(Animal):
    def falar(self):
        return "Glub glub!"

cachorro = Cachorro()
gato = Gato()
peixe = Peixe()

print("Cachorro:", cachorro.falar())
print("Gato:", gato.falar())
print("Peixe:", peixe.falar())

class Animal:
    def falar(self):
        return "Som genérico de animal"


class Cachorro(Animal):
    def falar(self):
        return "Au au!"


class Gato(Animal):
    def falar(self):
        return "Miau!"


animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.falar())

class Carro:
    def dirigir(self):
        return "Carro dirigindo"


class CarroGasolina(Carro):
    def dirigir(self):
        return "Carro a gasolina dirigindo"


class CarroEletrico(Carro):
    def dirigir(self):
        return "Carro elétrico dirigindo"


def testar_carro(carro):
    print(carro.dirigir())


carro_gasolina = CarroGasolina()
carro_eletrico = CarroEletrico()

testar_carro(carro_gasolina)
testar_carro(carro_eletrico)

import math

class Forma:
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

formas = [Circulo(5), Quadrado(4)]

for forma in formas:
    print("Área:", forma.area())

class Empregado:
    def calcular_salario(self):
        pass

class EmpregadoHora(Empregado):
    def __init__(self, horas_trabalhadas, salario_por_hora):
        self.horas_trabalhadas = horas_trabalhadas
        self.salario_por_hora = salario_por_hora
    
    def calcular_salario(self):
        return self.horas_trabalhadas * self.salario_por_hora

class EmpregadoMes(Empregado):
    def __init__(self, salario_mensal):
        self.salario_mensal = salario_mensal
    
    def calcular_salario(self):
        return self.salario_mensal

def pagar_salarios(empresa):
    for empregado in empresa:
        salario = empregado.calcular_salario()
        print(f"Salário a pagar: {salario}")

funcionarios = [
    EmpregadoHora(horas_trabalhadas=40, salario_por_hora=20),
    EmpregadoMes(salario_mensal=3000)
]

pagar_salarios(funcionarios)

class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
    
    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")
    
    def retirada(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Retirada de R${valor} realizada. Novo saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente.")

    def calcular_juros(self):
        pass

class ContaPoupanca(ContaBancaria):
    TAXA_JUROS = 0.05
    
    def calcular_juros(self):
        juros = self.saldo * self.TAXA_JUROS
        self.deposito(juros)
        print(f"Juros de R${juros} creditados. Novo saldo: R${self.saldo}")

class ContaCorrente(ContaBancaria):
    TAXA_JUROS = 0.03

contas = [
    ContaPoupanca(saldo=1000),
    ContaCorrente(saldo=2000)
]

for conta in contas:
    conta.deposito(500)
    conta.calcular_juros()
