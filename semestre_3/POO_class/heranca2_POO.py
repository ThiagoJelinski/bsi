class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def person_data(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


class Aluno(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota
    
    def person_data(self):
        super().person_data()
        print(f"Nota: {self.nota}")


pessoa1 = Pessoa("Thiago", 25)
aluno1 = Aluno("Gustavo", 20, 8.5)

print("Informações da Pessoa:")
pessoa1.person_data()

print("\nInformações do Aluno:")
aluno1.person_data()

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def show_data(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, qtd_portas):
        super().__init__(marca, modelo, ano)
        self.qtd_portas = qtd_portas
    
    def show_data(self):
        super().show_data()
        print(f"Quantidade de portas: {self.qtd_portas}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def show_data(self):
        super().show_data()
        print(f"Cilindradas: {self.cilindradas}")


carro1 = Carro("Chrysler", "300C", 2022, 4)
moto1 = Moto("BMW", "Miliduke", 2020, 1100)

print("Informações do Carro:")
carro1.show_data()

print("\nInformações da Moto:")
moto1.show_data()

class Animal:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
    
    def comer(self):
        print(f"{self.nome} está comendo.")


class Cachorro(Animal):
    def latir(self):
        print("Au au!")


class Gato(Animal):
    def miar(self):
        print("Miau!")

animal1 = Animal("Animal", 10)
cachorro1 = Cachorro("Bob", 15)
gato1 = Gato("Cat", 5)

animal1.comer()
cachorro1.comer()
cachorro1.latir()
gato1.comer()
gato1.miar()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def aumento(self, percentual):
        aumento_valor = self.salario * (percentual / 100)
        self.salario += aumento_valor
        print(f"Salário aumentado em {percentual}%.\nNovo salário: R${self.salario:.2f}")


funcionario1 = Funcionario("Thiago", 20, 3000)

print("Informações do Funcionário:")
print(f"Nome: {funcionario1.nome}")
print(f"Idade: {funcionario1.idade}")
print(f"Salário: R${funcionario1.salario:.2f}")

funcionario1.aumento(10)

import math

class Forma:
    def area(self):
        pass


class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def area(self):
        return self.comprimento * self.largura


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * self.raio ** 2


retangulo1 = Retangulo(5, 3)
circulo1 = Circulo(4)

print("Área do Retângulo:", retangulo1.area())
print("Área do Círculo:", circulo1.area())

class CCorrente:
    def __init__(self, numero: int, saldo: float, cliente: str) -> None:
        self._numero = numero
        self._saldo = saldo
        self._cliente = cliente

    def creditar(self, valor: float) -> None:
        self._saldo += valor

    def debitar(self, valor: float) -> None:
        self._saldo -= valor

    def get_saldo(self) -> float:
        return self._saldo


class CEspecial(CCorrente):
    def __init__(self, numero: int, saldo: float, cliente: str, limite: float) -> None:
        super().__init__(numero, saldo, cliente)
        self.__limite = limite


class CPoupanca(CCorrente):
    def __init__(self, numero: int, saldo: float, cliente: str, saldo_minimo: float) -> None:
        super().__init__(numero, saldo, cliente)
        self.__saldo_minimo = saldo_minimo

    def atualizar_saldo(self) -> None:
        self._saldo = round(self._saldo * 1.05, 2)

    def creditar(self, valor: float) -> None:
        if self.__saldo_minimo < valor:
            print("\033[0;31mNão foi possível realizar a transação, credite no mínimo R$ {:.2f}\033[0m".format(self.__saldo_minimo))
            return None
        self._saldo += valor


class Investimento(CCorrente):
    def __init__(self, numero: int, saldo: float, cliente: str, data_investimento: str, periodo: str) -> None:
        super().__init__(numero, saldo, cliente)
        self.__data_investimento = data_investimento
        self.__periodo = periodo

    def atualizar_saldo(self) -> None:
        self._saldo = round(self._saldo * 1.1, 2)

class Empregado:
    def __init__(self, codigo: int, nome: str, email: str, salario: float) -> None:
        self._codigo = codigo
        self._nome = nome
        self._email = email
        self._salario = salario

    def get_salario(self) -> float:
        return self._salario

    def aumento_percentual(self, percentual: int) -> None:
        self._salario = round(self._salario * (1 + percentual / 100), 2)


class Chefe(Empregado):
    def __init__(self, codigo: int, nome: str, email: str, salario: float, beneficio: int) -> None:
        super().__init__(codigo, nome, email, salario)
        self.__beneficio = beneficio

    def aumento_percentual(self, percentual: int) -> None:
        super().aumento_percentual(percentual)
        self._salario += self.__beneficio


class Estagiario(Empregado):
    def __init__(self, codigo: int, nome: str, email: str, salario: float, desconto: int) -> None:
        super().__init__(codigo, nome, email, salario)
        self.__desconto = desconto

    def aumento_percentual(self, percentual: int) -> None:
        super().aumento_percentual(percentual)
        self._salario -= self.__desconto

class Ingresso:
    def __init__(self, valor: float) -> None:
        self._valor = valor

    def imprime_valor(self) -> None:
        print(f"Valor do Ingresso: R$ {self._valor:.2f}")


class VIP(Ingresso):
    def __init__(self, valor: float, adicional: float) -> None:
        super().__init__(valor)
        self._adicional = adicional

    def valor_ingresso_vip(self) -> float:
        return self._valor + self._adicional


class Normal(Ingresso):
    def imprime_tipo(self) -> None:
        print("Ingresso Normal")


class CamaroteInferior(VIP):
    def __init__(self, valor: float, adicional: float, localizacao: str) -> None:
        super().__init__(valor, adicional)
        self._localizacao = localizacao

    def imprime_localizacao(self) -> None:
        print(f"Localização do Ingresso: {self._localizacao}")


class CamaroteSuperior(VIP):
    def __init__(self, valor: float, adicional: float, valor_adicional_camarote: float) -> None:
        super().__init__(valor, adicional)
        self._valor_adicional_camarote = valor_adicional_camarote

    def valor_ingresso_camarote(self) -> float:
        return self.valor_ingresso_vip() + self._valor_adicional_camarote


ingresso_normal = Normal(50.0)
ingresso_normal.imprime_valor()
ingresso_normal.imprime_tipo()

ingresso_vip = VIP(100.0, 20.0)
print("Valor do Ingresso VIP:", ingresso_vip.valor_ingresso_vip())

camarote_inferior = CamaroteInferior(80.0, 30.0, "Setor A")
print("Valor do Ingresso Camarote Inferior:", camarote_inferior.valor_ingresso_vip())
camarote_inferior.imprime_localizacao()

camarote_superior = CamaroteSuperior(120.0, 40.0, 50.0)
print("Valor do Ingresso Camarote Superior:", camarote_superior.valor_ingresso_camarote())

class Funcionario:
    def __init__(self, nome: str, endereco: str, telefone: str, email: str) -> None:
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
    
    def exibeDados(self) -> None:
        print("Nome:", self.nome)
        print("Endereço:", self.endereco)
        print("Telefone:", self.telefone)
        print("Email:", self.email)


class Assistente(Funcionario):
    def __init__(self, nome: str, endereco: str, telefone: str, email: str, matricula: int) -> None:
        super().__init__(nome, endereco, telefone, email)
        self.__matricula = matricula

    def get_matricula(self) -> int:
        return self.__matricula


class Tecnico(Assistente):
    def __init__(self, nome: str, endereco: str, telefone: str, email: str, matricula: int, bonus: float) -> None:
        super().__init__(nome, endereco, telefone, email, matricula)
        self.bonus = bonus

    def exibeDados(self) -> None:
        super().exibeDados()
        print("Matrícula:", self.get_matricula())


class Administrativo(Assistente):
    def __init__(self, nome: str, endereco: str, telefone: str, email: str, matricula: int, turno: str, adicional_noturno: float) -> None:
        super().__init__(nome, endereco, telefone, email, matricula)
        self.turno = turno
        self.adicional_noturno = adicional_noturno

    def exibeDados(self) -> None:
        super().exibeDados()
        print("Matrícula:", self.get_matricula())


funcionario1 = Funcionario("João", "Rua A, 123", "123456789", "joao@example.com")
funcionario1.exibeDados()

assistente_tecnico = Tecnico("Maria", "Rua B, 456", "987654321", "maria@example.com", 1001, 500.0)
assistente_tecnico.exibeDados()

assistente_administrativo = Administrativo("Carlos", "Rua C, 789", "456789123", "carlos@example.com", 1002, "Noite", 100.0)
assistente_administrativo.exibeDados()

from random import randrange

class Pessoa():
  _nome: str
  _idade: int

  def _init_(self, nome: str, idade: int) -> None:
    self._nome = nome
    self._idade = idade

class Rico(Pessoa):
  __dinheiro: float

  def _init_(self, nome: str, idade: int, dinheiro: float) -> None:
    super()._init_(nome, idade)
    self.__dinheiro = dinheiro

  def faz_compras(self) -> None:
    gasto = randrange(100)
    self.__dinheiro -= gasto

    print(f"Fiz uma compra de R$ {gasto:.2f}")

class Pobre(Pessoa):
  def trabalha(self):
    print("dias de luta, dias de luta e dias de luta")

class Miseravel(Pessoa):
  def mendigo(self):
    print("tem dois real ai moço?")

pobre1 = Pobre("Malamecio", 47)
pobre1.trabalha()

rico1 = Rico("Turcomano", 36, 15420)
rico1.faz_compras()
rico1.faz_compras()
rico1.faz_compras()
rico1.faz_compras()

miseravel1 = Miseravel("Moeiro", 53)
miseravel1.mendigo()

