""" EX04 Utils"""

__author__ = "730560264"

import numbers


def all(list: int, integer: int) -> bool:
    i = 0
    print(list)
    print(integer)
    while i < 3:
        if list[i] == integer:
            i += 1
        else: 
            return False
            

sa: list[int] = [1,1,1]
all(sa, 1)

