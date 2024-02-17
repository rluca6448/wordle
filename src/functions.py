import sys
from termcolor import colored


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
    i = 0
    correct = 0
    for i, (current_letter, expected_letter) in enumerate(zip(guess, word)):
        table[len(table) - int(attempt)][i][1] = guess[i]
        if current_letter == expected_letter:
            table[len(table) - int(attempt)][i][0] = 'green'
            correct += 1
        elif guess[i] in word:
            table[len(table) - int(attempt)][i][0] = 'yellow'
    print_table(table, length)
    return correct != len(word)
