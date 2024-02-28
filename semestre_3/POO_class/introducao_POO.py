#1. Qual das alternativas abaixo melhor define o termo classe?   
#R: c) É a personificação de um objeto da vida real.

#2. Qual das alternativas abaixo melhor define o termo “objeto”?
#R: a) Um objeto nos dá a capacidade de trabalhar com a classe e ter várias instâncias desta mesma classe.

#3. Qual das alternativas abaixo melhor explica o termo "propriedade"?
#R: b)Uma variável dentro de uma classe.

#4.Qual das alternativas abaixo melhor explica o termo "método"?
#R: c)A incorporação de uma ação real.

#5. Escreva o que você acha que deveria ser o nome da classe, os nomes das propriedades para o primeiro e último nome (sobrenome) e o nome do método que retorna “Olá”.
#Nome da classe:Usuario
#Propriedades: nome,sobrenome
#Método: print("Olá")


#Codificação:

class Usuario():
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def hello(self):
        return f"Olá , {self.nome} {self.sobrenome}"

nome = "Gustavo"
sobrenome = "Kubiack"

usuario1 = Usuario(nome,sobrenome)

print(usuario1.hello())

nome = "Jane"
sobrenome = "Silva"
usuario2 = Usuario(nome,sobrenome)

print(usuario2.hello())
