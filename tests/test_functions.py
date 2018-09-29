"""
Tests for Hangman game
"""
import pytest

import hangman

SCENARIOS = [
    {
        'status': 'fail',
        'input_data': ['a', 'b', 'c', 'd', 'f', 'e', 'g'],
        'word': 'HELLO',
        'guesses_count': 6
    },
    {
        'status': 'fail',
        'input_data': ['a', 'a', 't', 'c', 'd', 'f', 'e', 'g'],
        'word': 'HELLO',
        'guesses_count': 6
    },
    {
        'status': 'fail',
        'input_data': ['a', 'br', 'b', 'c', 'd', 'f', 'e', 'g'],
        'word': 'HELLO',
        'guesses_count': 6
    },
    {
        'status': 'fail',
        'input_data': ['a', '2', 'b', 'c', 'd', 'f', 'e', 'g'],
        'word': 'HELLO',
        'guesses_count': 6
    },
    {
        'status': 'success',
        'input_data': ['h', 'e', 'l', 'o'],
        'word': 'HELLO',
        'guesses_count': 6
    },
]

SCENARIOS_MOCKED_INPUT = [(scenario, scenario) for scenario in SCENARIOS]


@pytest.fixture(scope="function")
def redefine_input(request):
    """
    Pytest fixture for redefining input() function
    :param request:
    :return:
    """

    class Input:
        """
        Redefined input object
        """

        def __init__(self, data):
            self.data = data
            self.count = 0

        def __call__(self):
            self.count += 1
            if self.count > len(self.data):
                raise Exception("Not enough input!")
            return self.data[self.count - 1]

        def get_data(self):
            """
            returns Input data
            :return:
            """
            return self.data

    hangman.input = Input(request.param['input_data'])

    def back():
        hangman.input = input

    request.addfinalizer(back)


def test_choose_the_word_function():
    """Test the correctness of choose_the_word function."""
    assert isinstance(hangman.choose_the_word(["hello", "word"]), str)


def test_create_bag_of_vocabulary_words_function():
    """Test the correctness of create_bag_of_vocabulary_words function."""
    assert hangman.create_bag_of_vocabulary_words()


@pytest.mark.parametrize('scenario, redefine_input', SCENARIOS_MOCKED_INPUT,
                         indirect=['redefine_input'])
@pytest.mark.usefixtures('redefine_input')
def test_game_process_function_function(capsys, scenario):
    """Test the correctness of game_process function."""
    hangman.game_process(scenario['word'], scenario['guesses_count'])
    captured = capsys.readouterr()
    if scenario['status'] == 'fail':
        assert "You are lost" in str(captured.out)
    elif scenario['status'] == 'success':
        assert "You are won" in str(captured.out)
