"""This is ex04 Utils."""

__author__ = "730560264"


from typing import Sized


def all(list: Sized, integer: int) -> bool:
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
    # function that goes over the list compared to the integer and if all the same returns true else returns false


def max(input: list[int]) -> int:
    """This is the max function which looks at all the indexes in a list and finds the max."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    else:
        max1: int = 0
        max2: int = 0
        max: int = 0
        c: int = 0
        i: int = 0
        x: int = 1
        while c < len(input) * 2 and i != len(input) and x != len(input):
            # outlines the function so that it loops but stops the loop once one of the variable reaches the end
            if input[i] >= input[x]:
                max1 = input[i]
                x = x + 1
            else:
                max2 = input[x]
                i = i + 1
            # sets up the two functions which keep adding and comparing to one another
            c += 1
        if max1 >= max2:
            max = max1
        elif max2 > max1:
            max = max2
        # compares the last two maxes to figure out the true max
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This is the is_equal function which compares two lists to make sure all indexes are the same between the two."""
    i = 0
    if len(list1) == 0 and len(list2) == 0:
        # if both lists are length 0 returns true
        return True
    elif len(list1) == 0 or len(list2) == 0:
        # if one list is length 0 return false
        return False
    while i < len(list1) and len(list1) == len(list2):
        if list1[i] == list2[i]:
            i += 1
            # compares all the indexes in the list
        else:
            return False
    if len(list1) != len(list2):
        return False
        # if the lengths of the two list aren't the same prints false
    else: 
        return True
        # if the code traverses the whole function it returns true