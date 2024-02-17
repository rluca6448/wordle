import random
from functions import *

words = {
    3: ["uva", "uso", "oso", "dos"],
    4: ["toro", "casa", "sapo"],
    5: ["cinco", "siete"],
}

while True:
    length = int(input("Con cuantas letras queres jugar?\n"))
    if min(words.keys()) <= length <= max(words.keys()):
        break

attempt = int(input("Cuantos intentos te gustaria tener?\n"))

word = random.choice(words[length])

table = make_table(length, attempt)

not_guessed = True

while not_guessed and attempt > 0:
    while True:
        guess = input(f"Input a word with {len(word)} characters: \n")
        if len(guess) == length:
            break
    not_guessed = check_table(table, guess, word, attempt, length)
    attempt -= 1
    if attempt == 0:
        print("You lost! No more attempts for you :(")
        exit()
print("Congrats! You won at the attempt number", len(table) - attempt)