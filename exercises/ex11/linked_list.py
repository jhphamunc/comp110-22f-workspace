"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730560264"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next == None:
            return head.data
        else:
            return last(head.next)


def value_at(lhs: Optional[Node], rhs: int) -> int:
    if lhs is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if rhs == 0:
            return lhs.data
        else:
            return value_at(lhs.next, rhs - 1)


def max(head: Optional[Node]) -> int:
    if head is None:
        raise ValueError("Cannot call max with none")
    else: 
        max_int: int = head.data
        if head.data > max_int:
            max_int: int = head.data
            return max(head.next)
        if head.data == None:
            return max_int
        else:
            return max(head.next)

    
def linkify(items: list[int]) -> Optional[Node]:
    if len(items) == 3:
        return Node(items[0], Node(items[1], Node(items[2], None)))
    if len(items) == 2:
        return Node(items[0], Node(items[1], None))
    if len(items) == 1:
        return Node(items[0], None)


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
        if head is None:
            return None
        else:
            if head.next is not None:
                head.data *= factor
                return scale(head.next)
            else:
                