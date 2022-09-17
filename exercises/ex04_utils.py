"""This is ex04 Utils."""

__author__ = "730560264"


def all(list: int, integer: int) -> bool:
    """This is the all function which makes sure all the variables in a list are the same as the integer."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty list")
    i = 0
    while i < len(list):
        if list[i] == integer:
            i += 1
        else:
            return False
    else:
        return True


def max(input: list[int]) -> int:
    """ This is the max function which looks at all the indexes in a list and finds the max. """
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    else:
        c = 0
        i = 0
        x = 0
        while c < len(input) - 1 and i != len(input) and x != len(input) + 1:
            if input[i] >= input[x]:
                x = i + 1
            else:
                i = x+ 1
            c += 1
        if input[i] > input[x]:
            return input[i]
        else:
            return input[x]


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This is the is_equal function which compares two lists to make sure all indexes are the same between the two."""
    i = 0
    while i < len(list1):
        if list1[i] == list2[i]:
            i += 1
        else:
            return False
    else: 
        return True