"""It is module of tests."""
from hangman import choose_the_word
from hangman import create_bag_of_vocabulary_words


def test_choose_the_word_function():
    """Test the correctness of choose_the_word function."""
    assert isinstance(choose_the_word(["hello", "word"]), str)


def test_create_bag_of_vocabulary_words_function():
    """Test the correctness of create_bag_of_vocabulary_words function."""
    assert create_bag_of_vocabulary_words()
