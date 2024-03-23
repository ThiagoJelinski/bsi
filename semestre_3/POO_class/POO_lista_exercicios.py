class Bola:
    def __init__(self,cor ,circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostrarCor(self):
        return f"A cor da bola é {self.cor}"
    
    def trocarCor(self, nova_cor):
        self.cor = nova_cor
        return f"A nova cor da bola é {self.cor}"
    
cor = "Vermelho"
circunferencia = 10
material = "Borracha" 

cor1 = Bola(cor, circunferencia, material)

print(cor1.mostrarCor())

nova_cor = "Azul"
print(cor1.trocarCor(nova_cor))

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def retornarValordoLado(self):
        return f"O valor do lado é : {self.lado}"
    
    def mudarValordoLado(self, novo_lado):
        self.lado = novo_lado
        return f"O novo valor do lado é: {novo_lado}"
    
    def calcularArea (self, lado):
        area = lado ** 2
        return f"O valor da area é: {area}"

quadrado = Quadrado(2)

print(quadrado.retornarValordoLado())

novo_lado = 5
print(quadrado.mudarValordoLado(novo_lado))

print(quadrado.calcularArea(novo_lado))

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def retornarBaseAltura(self):
        return f"O valor da base: {self.base} | O valor da altura: {self.altura}"
    
        

