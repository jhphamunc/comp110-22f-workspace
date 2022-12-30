"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify

__author__ = "730560264"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)
    

def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_none() -> None:
    with pytest.raises(IndexError):
        value_at(Node(10, None), 1)


def test_value_at_int() -> None:
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 2) == 30


def test_max_none() -> None:
    with pytest.raises(ValueError):
        max(None)


def test_max_value() -> None:
    linked_list = Node(10, Node(40, Node(30, None)))
    assert max(linked_list) == 40


def test_linktify_none() -> None:
    list1: list[int] = []
    assert linkify(list1) == None


# def test_linktify_two() -> None:
#     list1: list[int] = [0, 1]
#     assert linkify(list1) == 1