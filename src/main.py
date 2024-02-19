import random
from functions import *

words = process_words()
min_letters = min(words.keys())
max_letters = max(words.keys())

wanna_play = True

while wanna_play:
    while True:
        length = int(input(f"Con cuantas letras queres jugar ({min_letters}-{max_letters})?\n"))
        if min_letters <= length <= max_letters:
            break

    attempt = 8

    word = random.choice(words[length])

    table = make_table(length, attempt)

    not_guessed = True

    while not_guessed and attempt > 0:
        while True:
            guess = input(f"Input a word with {len(word)} characters: \n")
            if len(guess) != length:
                print("Please input a guess of valid length!")
            elif guess.lower() not in words[length]:
                print("That word is not available!")
            else:
                break
        not_guessed = check_table(table, guess, word, attempt, length)
        attempt -= 1

    if not_guessed:
        print("You lost! No more attempts for you :(")
        print(f"The correct word was {word}!")
    else:
        print("Congrats! You won at the attempt number", len(table) - attempt)

    again = play_again()
    if again == 1:
        continue
    else:
        break
