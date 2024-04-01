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
    
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def area(self):
        return self.comprimento * self.largura

    def perimetro(self):
        return 2 * (self.comprimento + self.largura)


def main():
    comprimento = float(input("Informe o comprimento do local em metros: "))
    largura = float(input("Informe a largura do local em metros: "))

    local = Retangulo(comprimento, largura)

    area_local = local.area()
    perimetro_local = local.perimetro()

    quantidade_pisos = area_local
    quantidade_rodapes = perimetro_local * 0.1

    print("Quantidade de pisos necessários:", quantidade_pisos)
    print("Quantidade de rodapés necessários:", quantidade_rodapes)


if __name__ == "__main__":
    main()
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        self.idade += anos
        if self.idade < 21:
            self.altura += 0.5 * anos

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso


def main():
    pessoa = Pessoa("João", 18, 70, 170)  # Exemplo de uma pessoa chamada João, com 18 anos, 70 kg e 170 cm

    print("Altura inicial:", pessoa.altura)
    pessoa.envelhecer()
    print("Idade após um ano:", pessoa.idade)
    print("Altura após um ano:", pessoa.altura)


if __name__ == "__main__":
    main()

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente para saque.")


def main():
    conta = ContaCorrente("123456", "Fulano")

    print("Saldo inicial:", conta.saldo)
    conta.deposito(1000)
    print("Saldo após depósito:", conta.saldo)
    conta.saque(500)
    print("Saldo após saque:", conta.saldo)
    conta.alterar_nome("Ciclano")
    print("Nome do correntista após alteração:", conta.nome_correntista)


if __name__ == "__main__":
    main()

class TV:
    def __init__(self, canais_disponiveis, canal_atual=0, volume=5):
        self.canais_disponiveis = canais_disponiveis
        self.canal_atual = canal_atual
        self.volume = volume

    def mudar_canal(self, novo_canal):
        if 0 <= novo_canal < len(self.canais_disponiveis):
            self.canal_atual = novo_canal
            print("Canal alterado para:", self.canais_disponiveis[self.canal_atual])
        else:
            print("Canal inválido!")

    def aumentar_volume(self):
        if self.volume < 10:
            self.volume += 1
            print("Volume atual:", self.volume)
        else:
            print("Volume já está no máximo!")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume atual:", self.volume)
        else:
            print("Volume já está no mínimo!")


def exibir_menu(tv):
    print("\n--- MENU ---")
    print("1. Mudar canal")
    print("2. Aumentar volume")
    print("3. Diminuir volume")
    print("4. Desligar TV")
    print("Canais Disponíveis:")
    for indice, canal in enumerate(tv.canais_disponiveis):
        print(f"{indice}: {canal}")


def main():
    canais = ["Globo", "SBT", "Record", "Band", "RedeTV"]  # Exemplo de lista de canais disponíveis
    tv = TV(canais)

    while True:
        exibir_menu(tv)
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            novo_canal = int(input("Digite o número do novo canal: "))
            tv.mudar_canal(novo_canal)
        elif escolha == '2':
            tv.aumentar_volume()
        elif escolha == '3':
            tv.diminuir_volume()
        elif escolha == '4':
            print("Desligando TV...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()

class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def humor(self):
        return (self.fome + self.saude) / 2


def main():
    bichinho = BichinhoVirtual("BobCat", 5, 10, 1)

    print("Nome:", bichinho.retornar_nome())
    print("Fome:", bichinho.retornar_fome())
    print("Saúde:", bichinho.retornar_saude())
    print("Idade:", bichinho.retornar_idade())
    print("Humor:", bichinho.humor())


if __name__ == "__main__":
    main()

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.estomago = []

    def comer(self, alimento):
        self.estomago.append(alimento)
        print(f"{self.nome} comeu {alimento}.")

    def ver_estomago(self):
        if self.estomago:
            print(f"{self.nome} tem no estômago: {', '.join(self.estomago)}")
        else:
            print(f"{self.nome} está com o estômago vazio.")

    def digerir(self):
        if self.estomago:
            print(f"{self.nome} está digerindo...")
            self.estomago.clear()
            print(f"{self.nome} digeriu tudo.")
        else:
            print(f"{self.nome} não tem nada para digerir.")


def main():
    macaco1 = Macaco("Macaquinho")
    macaco2 = Macaco("Macacão")

    macaco1.comer("banana")
    macaco2.comer("maçã")
    macaco1.comer("laranja")

    macaco1.ver_estomago()
    macaco2.ver_estomago()

    macaco1.digerir()
    macaco2.digerir()

    macaco1.ver_estomago()
    macaco2.ver_estomago()

    macaco2.comer("Macaquinho")
    macaco2.ver_estomago()



if __name__ == "__main__":
    main()

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"({self.x}, {self.y})")


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


def alterar_retangulo(retangulo):
    novo_x = input("Digite o novo valor de x para o ponto inicial: ")
    novo_y = input("Digite o novo valor de y para o ponto inicial: ")
    nova_largura = input("Digite a nova largura: ")
    nova_altura = input("Digite a nova altura: ")

    if not (novo_x.isdigit() and novo_y.isdigit() and nova_largura.isdigit() and nova_altura.isdigit()):
        print("Valor inválido!")
        return

    retangulo.ponto_inicial.x = float(novo_x)
    retangulo.ponto_inicial.y = float(novo_y)
    retangulo.largura = float(nova_largura)
    retangulo.altura = float(nova_altura)


def exibir_menu():
    print("\n--- MENU ---")
    print("1. Alterar valores do retângulo")
    print("2. Imprimir centro do retângulo")
    print("3. Sair")


def main():
    ponto_inicial = Ponto(0, 0)
    retangulo = Retangulo(ponto_inicial, 4, 3)

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            alterar_retangulo(retangulo)
        elif escolha == '2':
            centro = retangulo.encontrar_centro()
            print("Centro do retângulo:")
            centro.imprimir()
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        litros_abastecidos = min(litros_abastecidos, self.quantidade_combustivel)
        self.quantidade_combustivel -= litros_abastecidos
        return litros_abastecidos

    def abastecer_por_litro(self, litros):
        valor_pagar = litros * self.valor_litro
        litros_abastecidos = min(litros, self.quantidade_combustivel)
        self.quantidade_combustivel -= litros_abastecidos
        return valor_pagar

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade


def main():
    bomba = BombaCombustivel("Gasolina", 4.50, 1000)

    print("Abastecendo por valor...")
    litros_abastecidos = bomba.abastecer_por_valor(50)
    print(f"Foram abastecidos {litros_abastecidos:.2f} litros.")

    print("\nAbastecendo por litro...")
    valor_pagar = bomba.abastecer_por_litro(30)
    print(f"O cliente deve pagar R${valor_pagar:.2f}.")

    print("\nAlterando o valor do litro...")
    novo_valor_litro = float(input("Digite o novo valor do litro: "))
    bomba.alterar_valor(novo_valor_litro)
    print("Novo valor do litro:", bomba.valor_litro)

    print("\nAlterando o tipo de combustível...")
    novo_tipo_combustivel = input("Digite o novo tipo de combustível: ")
    bomba.alterar_combustivel(novo_tipo_combustivel)
    print("Novo tipo de combustível:", bomba.tipo_combustivel)

    print("\nAlterando a quantidade de combustível na bomba...")
    nova_quantidade_combustivel = float(input("Digite a nova quantidade de combustível: "))
    bomba.alterar_quantidade_combustivel(nova_quantidade_combustivel)
    print("Nova quantidade de combustível:", bomba.quantidade_combustivel)


if __name__ == "__main__":
    main()

class Carro:
    def __init__(self, nome, consumo_km_por_litro):
        self.nome = nome
        self.consumo_km_por_litro = consumo_km_por_litro
        self.nivel_combustivel = 0

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo_km_por_litro
        if combustivel_necessario <= self.nivel_combustivel:
            self.nivel_combustivel -= combustivel_necessario
            print(f"O {self.nome} percorreu {distancia} km.")
        else:
            print("Não há combustível suficiente para percorrer essa distância.")

    def obter_gasolina(self):
        return self.nivel_combustivel

    def adicionar_gasolina(self, quantidade):
        self.nivel_combustivel += quantidade
        print(f"Tanque do {self.nome} abastecido com {quantidade} litros de gasolina.")


def main():
    nome_carro = "300C V8"
    consumo_carro = 8
    meu_carro = Carro(nome_carro, consumo_carro)
    meu_carro.adicionar_gasolina(50)
    meu_carro.andar(200)
    print(f"Combustível restante no tanque do {nome_carro}: {meu_carro.obter_gasolina()} litros.")


if __name__ == "__main__":
    main()

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100

    def adicione_juros(self):
        self.saldo *= (1 + self.taxa_juros)

    def get_saldo(self):
        return self.saldo


def main():
    saldo_inicial = 1000.00
    taxa_juros = 10.0
    conta = ContaInvestimento(saldo_inicial, taxa_juros)

    for _ in range(5):
        conta.adicione_juros()

    print(f"Saldo final após 5 aplicações de juros: R${conta.get_saldo():.2f}")


if __name__ == "__main__":
    main()

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def aumentar_salario(self, porcentual_de_aumento):
        self.salario *= (1 + porcentual_de_aumento / 100)


def main():
    funcionario = Funcionario("João", 3000.00)

    print("Nome do funcionário:", funcionario.get_nome())
    print("Salário do funcionário:", funcionario.get_salario())

    porcentual_de_aumento = 10
    funcionario.aumentar_salario(porcentual_de_aumento)

    print("\nApós aumento de", porcentual_de_aumento, "% no salário:")
    print("Salário do funcionário:", "{:.2f}".format(funcionario.get_salario()))


if __name__ == "__main__":
    main()

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade):
        self.fome -= quantidade

    def brincar(self, tempo):
        self.tedio -= tempo

    def humor(self):
        if self.fome <= 25 and self.tedio <= 25:
            return "Feliz"
        elif self.fome > 25 and self.tedio > 25:
            return "Normal"
        else:
            return "Triste"


def main():
    nome_bichinho = input("Digite o nome do bichinho: ")
    bichinho = BichinhoVirtual(nome_bichinho)

    print(f"{bichinho.nome} foi criado!")

    quantidade_comida = int(input("Quantidade de comida fornecida(em gramas): "))
    tempo_brincadeira = int(input("Tempo de brincadeira (em minutos): "))

    bichinho.alimentar(quantidade_comida)
    bichinho.brincar(tempo_brincadeira)

    print(f"\nHumor de {bichinho.nome}: {bichinho.humor()}")


if __name__ == "__main__":
    main()

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade):
        self.fome -= quantidade

    def brincar(self, tempo):
        self.tedio -= tempo

    def humor(self):
        if self.fome <= 25 and self.tedio <= 25:
            return "Feliz"
        elif self.fome > 25 and self.tedio > 25:
            return "Normal"
        else:
            return "Triste"

    def __str__(self):
        return f"Bichinho {self.nome}: Fome - {self.fome}, Tédio - {self.tedio}"


def main():
    nome_bichinho = input("Digite o nome do bichinho: ")
    bichinho = BichinhoVirtual(nome_bichinho)

    print(f"{bichinho.nome} foi criado!")

    while True:
        print("\nMenu:")
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            quantidade_comida = int(input("Quantidade de comida fornecida (em gramas): "))
            bichinho.alimentar(quantidade_comida)
        elif escolha == "2":
            tempo_brincadeira = int(input("Tempo de brincadeira (em minutos): "))
            bichinho.brincar(tempo_brincadeira)
        elif escolha == "3":
            break
        elif escolha == "segredo":
            print(bichinho)
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()

import random

class BichinhoVirtual:
    def __init__(self, nome, fome, tedio):
        self.nome = nome
        self.fome = fome
        self.tedio = tedio

    def alimentar(self, quantidade):
        self.fome -= quantidade

    def brincar(self, tempo):
        self.tedio -= tempo

    def humor(self):
        if self.fome <= 25 and self.tedio <= 25:
            return "Feliz"
        elif self.fome > 25 and self.tedio > 25:
            return "Normal"
        else:
            return "Triste"

    def __str__(self):
        return f"Bichinho {self.nome}: Fome - {self.fome}, Tédio - {self.tedio}"


def criar_bichinhos(num_bichinhos):
    bichinhos = []
    for i in range(num_bichinhos):
        nome = f"Bichinho{i+1}"
        fome = random.randint(0, 100)
        tedio = random.randint(0, 100)
        bichinho = BichinhoVirtual(nome, fome, tedio)
        bichinhos.append(bichinho)
    return bichinhos


def alimentar_todos(bichinhos, quantidade):
    for bichinho in bichinhos:
        bichinho.alimentar(quantidade)


def brincar_com_todos(bichinhos, tempo):
    for bichinho in bichinhos:
        bichinho.brincar(tempo)


def ouvir_todos(bichinhos):
    for bichinho in bichinhos:
        print(bichinho)


def main():
    num_bichinhos = int(input("Quantidade de bichinhos na fazenda: "))
    bichinhos = criar_bichinhos(num_bichinhos)

    while True:
        print("\nMenu:")
        print("1 - Alimentar todos os bichinhos")
        print("2 - Brincar com todos os bichinhos")
        print("3 - Ouvir todos os bichinhos")
        print("4 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            quantidade_comida = int(input("Quantidade de comida fornecida: "))
            alimentar_todos(bichinhos, quantidade_comida)
        elif escolha == "2":
            tempo_brincadeira = int(input("Tempo de brincadeira (em minutos): "))
            brincar_com_todos(bichinhos, tempo_brincadeira)
        elif escolha == "3":
            ouvir_todos(bichinhos)
        elif escolha == "4":
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()



