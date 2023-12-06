from faker import Faker
import random


class FindTheWord:
    def __init__(self):
        self.level = None
        self.category = None
        self.word = None

    def infos(self):
        self.level = input("Informe a dificuldade: ")
        self.category = input("Informe a categoria: ")

    def dicts(self, num_items):
        faker = Faker("pt-br")
        countries = [faker.country() for _ in range(num_items)]
        names = [faker.first_name() for _ in range(num_items)]
        colors = [faker.color_name() for _ in range(num_items)]

        processed_colors = [color.split()[0] for color in colors]
        processed_names = [name.split()[0] for name in names]
        processed_countries = [country.split()[0] for country in countries]

        data = {
            "Países": processed_countries,
            "Nomes": processed_names,
            "Cores": processed_colors,
        }
        return data

    def choice_level(self):
        data = self.dicts(20)
        if self.level == "Fácil":
            return data[self.category][:5]
        elif self.level == "Médio":
            return data[self.category][:10]
        elif self.level == "Difícil":
            return data[self.category][:20]
        else:
            print("Erro! As opções de dificuldade são: 'Fácil', 'Médio' e 'Difícil'")

    def shuffle_words(self, words):
        word = random.choice(words)
        shuffle_word = "".join(random.sample(word, len(word)))

        if self.level == "Fácil":
            count = 20
        elif self.level == "Médio":
            count = 10
        else:
            count = 5

        for attemp in range(count):
            print(f"Essa é a palavra para descobrir: {shuffle_word}")
            self.word = input(f"Tentativa: {count}\nEscreva: ")
            count -= 1
            if self.word == word:
                print("Você acertou! ")
                break
            if count == 0:
                print(f"Você perdeu! A palavra era: {word}")
        return self.word