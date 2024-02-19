import sys

import numpy as np
from termcolor import colored
import requests


def make_table(length, attempt):
    return [[['red', '?'] for _ in range(length)] for _ in range(attempt)]


def print_table(table, length):
    print('This is the current wordle!\n' + '-' * 4 * length + '-')
    for row in table:
        sys.stdout.write('| ')
        for column in row:
            sys.stdout.write(colored(column[1], column[0], force_color=True) + ' | ')
        print('\n' + '-' * 4 * length + '-')


def check_table(table, guess, word, attempt, length):
    correct = 0
    guess = guess.lower()
    for i, (current_letter, expected_letter) in enumerate(zip(guess, word)):
        table[len(table) - int(attempt)][i][1] = guess[i]
        if current_letter == expected_letter:
            table[len(table) - int(attempt)][i][0] = 'green'
            correct += 1
        elif guess[i] in word:
            table[len(table) - int(attempt)][i][0] = 'yellow'
    print_table(table, length)
    return correct != len(word)


def process_words():
    url = 'https://corpus.rae.es/frec/5000_formas.txt'  # Replace with the actual URL
    filename = '../wordslist.txt'
    response = requests.get(url, stream=True)

    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):  # Download in chunks
            if chunk:  # Filter out keep-alive new chunks
                f.write(chunk)

    file1 = open(filename, 'r')
    Lines = file1.readlines()
    word_array = {}

    for line in Lines:
        if not line.strip():
            continue
        word = (line.split())[1]
        if not line.__contains__('Frec.absoluta') and len(word) > 2 and word.isascii():
            if not word_array.keys().__contains__(int(len(word))):
                word_array[int(len(word))] = []
            word_array[int(len(word))].append(word)
    file1.close()
    return word_array


def play_again():
    while True:
        result = input("Do you want to play again? y/n\n")
        if result == 'y' or result == 'n':
            break
    return 1 if result == 'y' else 0
