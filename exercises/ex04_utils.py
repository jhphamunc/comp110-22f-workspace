"""This is ex04 Utils."""

__author__ = "730560264"


def all(list: int, integer: int) -> bool:
    """This is the all function which makes sure all the variables in a list are the same as the integer."""
    if len(list) == 0:
        return False
    i = 0
    while i < len(list):
        if list[i] == integer:
            i += 1
        else:
            return False
    else:
        return True


def max(input: list[int]) -> int:
    """This is the max function which looks at all the indexes in a list and finds the max."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    else:
        max1: int = 0
        max2: int = 0
        c = 0
        i = 0
        x = 1
        while c < len(input) * 2 and i != len(input) and x != len(input):
            if input[i] >= input[x]:
                max1 = input[i]
                x = x + 1
            else:
                max2 = input[x]
                i = i + 1
            c += 1
        if max1 >= max2:
            return max1
        elif max2 > max1:
            return max2


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This is the is_equal function which compares two lists to make sure all indexes are the same between the two."""
    i = 0
    if len(list1) == 0 or len(list2) == 0:
        return False
    while i < len(list1) and len(list1) == len(list2):
        if list1[i] == list2[i]:
            i += 1
        else:
            return False
    if len(list1) != len(list2):
        return False
    else: 
        return True