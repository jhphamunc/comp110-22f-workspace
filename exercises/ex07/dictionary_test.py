"""This is ex07 dictionary_test."""

__author__ = "730560264"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_zero_answers() -> None:
    """This test the invert function for no answers."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_two_answers() -> None:
    """This test the invert function for two answers."""
    test_dict: dict[str, str] = {'a': 'z', 'b': 'y'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b'}


def test_invert_three_answers() -> None:
    """This test the invert function for three answers."""
    test_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color_none() -> None:
    """This test the favorite color function for an open string."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_favorite_color_blue() -> None:
    """This test the favorite color function for the answer 'blue'."""
    test_dict: dict[str, str] = {'Joseph': 'blue', 'Anna': 'blue', 'John': 'red'}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_green() -> None:
    """This test the favorite color function for the answer 'green'."""
    test_dict: dict[str, str] = {'Anthony': 'green', 'KC': 'red', 'Darren': 'green'}
    assert favorite_color(test_dict) == "green"


def test_count_empty_dict() -> None:
    """This test the count function for no answer."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_two_terms() -> None:
    """This test the count function for two terms."""
    test_list: list[str] = ["code", "read", "code"]
    assert count(test_list) == {'code': 2, 'read': 1}


def test_count_three_terms() -> None:
    """This test the count function for three terms."""
    test_list: list[str] = ["code", "read", "sleep", "code"]
    assert count(test_list) == {'code': 2, 'read': 1, 'sleep': 1}