class Usuario():
    def __init__(self, nome, sobrenome):
        self.nome = nome    
        self.sobrenome = sobrenome
    
    def getNomeCompleto(self):
        return "Olá, " + self.nome + self.sobrenome


user = Usuario("Jonnie", "Bravo")
print(user.getNomeCompleto())