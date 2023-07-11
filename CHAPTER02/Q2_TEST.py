import random


def alphabet_game():
    while True:
        random_letter = chr(random.randint(65, 90))
        print(random_letter)

        if random_letter == "N":
            print("終了")
            break


alphabet_game()
