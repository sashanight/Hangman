# -*- coding: utf-8 -*-
"""The module play hangman console game with user."""

import random

MISTAKES_COUNT_CONSTANT = 8


def create_bag_of_vocabulary_words():
    """
    Form the array of words which can be conceived during the game.
    This words are stored in hangman/vocabulary.txt
    """
    words_array = []
    file_object = open("./hangman/vocabulary.txt")
    for line in file_object:
        for word in line.split():
            words_array.append(word)
    file_object.close()
    return words_array


def choose_the_word(vocabulary_array):
    """Return the word that was conceived from vocabulary for the game.

    Keyword arguments:
        vocabulary_array  - array of words from which to choose
    """
    word_index = random.randint(0, len(vocabulary_array) - 1)
    word = vocabulary_array[word_index]
    return word


def game_process(word, available_mistakes_count):
    """Function that is responsible for the game process.

    Keyword arguments:
        word  - word that need to guess
        mistake_count - count of mistakes that can do user
    """
    symbols_array = list(word)
    current_word = ["*"] * len(symbols_array)
    entered_letters = []
    mistakes_counter = 0

    flag = False
    while (not flag) and (mistakes_counter < available_mistakes_count):
        print("Guess a letter:")
        input_letter = list(str(input()))
        if len(input_letter) != 1:
            print("Enter error! Guess a letter:\n")
            continue
        else:
            letter = input_letter[0].upper()
            if letter.isalpha() is False:
                print("It is not a letter! Guess a letter:\n")
                continue

            if letter in entered_letters:
                print("Letter was checked! Guess a letter:\n")
                continue
            letter_was_fount = False
            for i, letter_i in enumerate(symbols_array):
                if letter_i == letter:
                    current_word[i] = letter
                    letter_was_fount = True
            if letter_was_fount is False:
                mistakes_counter += 1
                print("Missed, mistake {} out of {}. \n".format(
                    mistakes_counter, available_mistakes_count))
            else:
                print("Hit! \n")
                if "*" not in current_word:
                    flag = True

            entered_letters.append(letter)
            print("The word: {} \n".format("".join(current_word)))

    if mistakes_counter == available_mistakes_count:
        print("You are lost \n")
    else:
        print("You are won \n")


def start_the_game():  # pragma: no cover
    """Encapsulate all work of application."""
    bag_of_words = create_bag_of_vocabulary_words()
    chosen_word = choose_the_word(bag_of_words)
    game_process(chosen_word, MISTAKES_COUNT_CONSTANT)


# if __name__ == "__main__":
#     start_the_game()
