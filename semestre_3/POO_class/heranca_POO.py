class Usuario:
    def __init__(self):
        self.__nomeUsuario = None

    def setNomeUsuario(self, nome):
        self.__nomeUsuario = nome

    def getNomeUsuario(self):
        return self.__nomeUsuario


class Admin(Usuario):
    def escrevaNome(self):
        return "Admin"

    def digaOla(self):
        return f"Olá {self.getNomeUsuario()}"


admin1 = Admin()
admin1.setNomeUsuario("Baltazar")

print(admin1.digaOla())
