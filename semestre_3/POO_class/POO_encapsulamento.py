#1) Nós usamos o modificador de acesso private a fim de:
#R: d)B e C estão corretas

#Codificação:

#2)

class Usuario:
    def __init__(self, nome):
        self.__nome = nome

    def getnome(self):
        return "O nome é" + self.__nome
    
User = Usuario("Joe")
print(User.__nome)

class Usuario:
    def __init__(self, nome=""):
        self.nome = nome

    def getnome(self):
        return f"O nome é {self.nome}"
        
user = Usuario("Joe")
print(user.getnome())

#3) 
class Colaborador():
    def __init__(self, nome, salario, projeto):
        self.nome = nome
        self.salario = salario
        self.projeto = projeto

    def trabalho(self):
        return f"O {self.nome} esta trabalhando na area de{self.projeto}"
    
    def mostrar(self):
        return f" Nome: {self.nome} | Salario: {self.salario} "
    
colaboradorA = Colaborador("Joe", 2000, "Analista de Sistemas")
print(colaboradorA.trabalho())
print(colaboradorA.mostrar())

#4)

class Robo():
    def __init__(self, nome, ano):
        self__nome = nome
        self__ano = ano
    
    def diga_alo(self):
        return f"Nome: {self.nome} | Ano de construção: {self.ano}"
    
robot = Robo("XRL8", 2100)
print(robot.diga_alo())

#5)

class Laptop():
    def __init__(self):
        self.preco = None
    
    def get__preco(self):
        return self.preco
    
laptop = Laptop()
print("Preço inicial do laptop:" , laptop.get__preco())

laptop.set__preco(5000)
print("O novo preço é:" , laptop.get__preco())

#6)

class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__sobrenome = ""
    
    def getnome(self):
        return self.__nome
    
    def getsobrenome(self):
        return self.__sobrenome

    def setnome(self, nome):
        self.__nome = nome
    
    def setsobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

pessoa = Pessoa()
pessoa.setnome("Joe")
pessoa.setsobrenome("Bravo")

print (f"O nome completo é {pessoa.nome} {pessoa.sobrenome}")
    
