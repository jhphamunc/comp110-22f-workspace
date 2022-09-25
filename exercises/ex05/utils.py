"""This is ex05 Utils."""

__author__ = "730560264"


def only_evens(given_list: list[int]) -> list[int]:
    """Defines the only_even function with given parameter of a list."""
    i: int = 0
    even_list: list[int] = []
    while i < len(given_list):
        if given_list[i] % 2 == 0:
            even_list.append(given_list[i])
            i += 1
            # sets up the function to see if the values of given indexes are positive
            # if positive adds them to the list
        else:
            i += 1
            # if not positive goes into the next index
    return even_list
    # returns the even list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Defines concat function with given parameters of lists."""
    list2_counter: int = 0
    list1_counter: int = 0
    combined_list: list[int] = []
    while list1_counter < len(list1):
        combined_list.append(list1[list1_counter])
        list1_counter += 1
        # begins with list1 and adds them to the combined_list
    while list2_counter < len(list2):
        combined_list.append(list2[list2_counter])
        list2_counter += 1
        # then it goes onto list2 and adds those to combined_list
    return combined_list
    # returns the combined_list


def sub(list: list[int], start_index: int, end_index: int) -> list[int]:
    """Defines sub function with parameters of a list, and two integers."""
    end_list: list[int] = []
    if len(list) == 0 or start_index >= len(list) or end_index <= 0:
        return end_list
        # under certain circumstances which will return a list as empty
    else:
        current_index: int = start_index
        max_end: int = end_index 
        if start_index < 0:
            current_index = 0
            # if the start index is negative it becomes 0
        if end_index > len(list):
            max_end = len(list)
            # if the max is greater than the list length it becomes the list legnth
        while current_index < max_end:
            end_list.append(list[current_index])
            current_index += 1
            # starts to append the new subset under the given rules
    return end_list
    # returns the end list