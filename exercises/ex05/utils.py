"""This is ex05 Utils."""

__author__ = "730560264"


def only_evens(given_list: list[int]) -> list[int]:
    i: int = 0
    even_list: list[int] = []
    while i < len(given_list):
        if given_list[i] % 2 == 0:
            even_list.append(given_list[i])
            i += 1
        else:
            i += 1
    return even_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    list2_counter: int = 0
    list1_counter: int = 0
    combined_list: list[int] = []
    while list1_counter < len(list1):
        combined_list.append(list1[list1_counter])
        list1_counter += 1
    while list2_counter < len(list2):
        combined_list.append(list2[list2_counter])
        list2_counter += 1
    return combined_list


def sub(list: list[int], start_index: int, end_index: int) -> list[int]:
    end_list: list[int] = []
    if len(list) == 0 or start_index > len(list) or end_index <= 0:
        return end_list
    else:
        current_index = start_index
        while current_index < end_index:
            end_list.append(list[current_index])
            current_index += 1
    return end_list
