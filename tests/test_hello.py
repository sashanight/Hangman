"""It is module of tests."""
from hangman import choose_the_word


def test_hello():
    """Test the correctness of choose_the_word function."""
    assert isinstance(choose_the_word(["hello", "word"]), str)
