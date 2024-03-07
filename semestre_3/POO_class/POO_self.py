
#1. Qual palavra-chave (keyword) você usaria para ter acesso às propriedades e métodos de uma classe estando dentro dela?
#R: c) A palavra-chave self

#Codificação:

class Usuario():
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def hello(self):
        return f"Olá, {self.nome}"

nome = "Jonnie"
sobrenome = "Bravo"

Usuario1 = Usuario(nome, sobrenome)
print(Usuario1.hello())