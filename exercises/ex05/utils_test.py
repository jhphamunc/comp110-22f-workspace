"""This is ex05 utils_test."""

__author__ = "730560264"

from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Test the only_evens function for an empty list."""
    given_list: list[int] = []
    assert only_evens(given_list) == []


def test_only_evens_two_terms() -> None:
    """Test the only_evens function for two terms."""
    given_list: list[int] = [1, 2, 3, 4]
    assert only_evens(given_list) == [2, 4]


def test_only_evens_three_terms() -> None:
    """Test the only_evens function for three terms."""
    given_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(given_list) == [2, 4, 6]


def test_concat_empty() -> None:
    """Test the concat function for an empty list."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_concat_five_terms() -> None:
    """Test the concat function for 5 terms."""
    list1: list[int] = [1, 2]
    list2: list[int] = [3, 4, 5]
    assert concat(list1, list2) == [1, 2, 3, 4, 5]


def test_concat_seven_terms() -> None:
    """Test the concat function for 7 terms."""
    list1: list[int] = [1, 2, 3, 4]
    list2: list[int] = [5, 6, 7]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6, 7]


def test_sub_empty() -> None:
    """Test the sub function for an empty list."""
    list: list[int] = [1, 2, 3, 4]
    start_index: int = 1
    end_index: int = 0
    assert sub(list, start_index, end_index) == []


def test_sub_two_terms() -> None:
    """Test the sub function for two terms."""
    list: list[int] = [1, 2, 3, 4]
    start_index: int = 1
    end_index: int = 3
    assert sub(list, start_index, end_index) == [2, 3]


def test_sub_three_terms() -> None:
    """Test the sub function for three terms."""
    list: list[int] = [1, 2, 3, 4]
    start_index: int = 0
    end_index: int = 3
    assert sub(list, start_index, end_index) == [1, 2, 3]