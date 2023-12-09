#1- Crie um programa que crie um arquivo chamado "texto.txt" e escreva nele o seguinte texto: "Olá, mundo!"

with open("arquivos/texto.txt", "w") as f:
    f.write("Olá mundo!")
    f.close()

#2- Crie um programa que leia o conteúdo do arquivo "texto.txt" criado no exercício anterior e o exiba no console.

with open("arquivos/texto.txt") as f:
    print(f.read())

#3- Crie um programa que conte e exiba o número de linhas no arquivo "texto.txt".

with open("arquivos/texto.txt") as f:
    count = 0
    for line in f.readlines():
        count += 1
    print(f"O número de linhas é: {count}")

#4- Crie um programa que copie o conteúdo do arquivo "texto.txt" para um novo arquivo chamado "copia.txt".

new_arquivo = open("copia.txt", "w")

with open("texto.txt", "r") as n:
  for linha in n.readlines():
    new_arquivo.write(linha)

new_arquivo.close()

with open("copia.txt") as copia:
  print(copia.read())

#5- Crie um programa que leia o conteúdo dos arquivos "texto.txt" e "copia.txt", e escreva o conteúdo combinado em um terceiro arquivo chamado "combinado.txt".

with open("arquivos/texto.txt") as f:
    text = f.read()
with open("arquivos/copia.txt") as f:
    copy = f.read()
with open("arquivos/combinado.txt", "w") as f:
    text += "\n"
    f.write(text)
    f.write(copy)

#6- Crie um programa que conte e exiba o número de palavras no arquivo "texto.txt".

total_words = 0

with open("texto.txt", "r") as texto:
  for linha in texto.readlines():
    total_words += len(linha.split())

print(f"O arquivo texto.txt tem {total_words} palavra(s)")

#7- Crie um programa que leia o conteúdo do arquivo "texto.txt" e substitua todas as ocorrências da palavra "mundo" por "Python". O novo conteúdo deve ser escrito em um novo arquivo chamado "modificado.txt".

modificado = open("modificado.txt", "w")

with open("texto.txt", "r") as texto:
  for linha in texto.readlines():
    modificado.write(linha.replace("mundo", "Python"))

modificado.close()

with open("modificado.txt", "r") as modificado:
  print(modificado.read())

#8- Crie um programa que adicione a frase "Isso é incrível!" ao final do arquivo "texto.txt".

with open("texto.txt", "a") as text:
  text.write("\n" + "Isso é incrível!")

with open("texto.txt", "r") as text:
  print(text.read())

#9 - Crie um programa que leia o conteúdo do arquivo "texto.txt" e conte quantas letras (excluindo espaços) estão presentes no texto.

with open("arquivos/texto.txt") as f:
    lines = [line for line in f.readlines()]
    words = [word for line in lines for word in line.split()]
    count = 0
    for letter in words:
        count += len(letter)
    print(f"A quantidade de letras no texto.txt é: {count}")


#10- Crie um programa que leia o conteúdo do arquivo "numeros.txt" (contendo números inteiros separados por vírgula), some esses números e exiba o resultado.

with open("arquivos/numeros.txt", "w") as f:
    for line in range(0, 101):
        if line < 100:
            f.write(f"{line},")
        else:
            f.write(f"{line}\n") 

#11- Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
#200.135.80.9
#192.168.1.1
#8.35.67.74
#257.32.4.5
#85.345.1.2
#1.2.3.4
#9.8.234.5
#192.168.0.256
#O arquivo de saída possui o seguinte formato:
#[Endereços válidos:]
#200.135.80.9
#192.168.1.1
#8.35.67.74
#1.2.3.4
#[Endereços inválidos:]
#257.32.4.5
#85.345.1.2
#9.8.234.5
#192.168.0.256

with open("arquivos/numeros.txt", "w") as f:
    for line in range(0, 101):
        if line < 100:
            f.write(f"{line},")
        else:
            f.write(f"{line}")

with open("arquivos/numeros.txt") as f:
    lines = f.read()
    numbers = [int(number) for number in lines.split(",")]
    print(f"A soma de 0 a 100 é: {sum(numbers)}")
