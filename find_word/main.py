from game_find_word import FindTheWord


def main():
    find_name = FindTheWord()
    find_name.infos()
    words = find_name.choice_level()
    find_name.shuffle_words(words)


if __name__ == "__main__":
    main()