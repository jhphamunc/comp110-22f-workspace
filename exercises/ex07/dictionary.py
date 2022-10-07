"""This is ex07 dictionary."""

__author__ = "730560264"


def invert(list: dict[str, str]) -> dict[str, str]:
    """This is the invert function which switches the key and value of a dictionary."""
    inverted_list: dict[str, str] = {}
    for key in list:
        if list[key] not in inverted_list:
            inverted_list[list[key]] = key
            # Adds the values from the original list as a key and vice versa
        else:
            raise KeyError
            # Unless there are multiple values so it becomes a KeyError
    return inverted_list


def favorite_color(list: dict[str, str]) -> str:
    """This is the favorite_color function which calculates the favorite color."""
    color_dict: dict[str, int] = {}
    colors_list: list(str) = []
    numbers: list(int) = []
    max: int = 0
    max_color: str = ""
    i: int = 0
    x: int = 1
    # Sets up all the dictionaries, list, and variables
    if len(list) == 0:
        return max_color
        # If the list is empty it returns an open string
    for key in list:
        color_dict[list[key]] = 0
    for key in list:
        color_dict[list[key]] += 1
    for key in color_dict:
        colors_list.append(key)
        numbers.append(color_dict[key])
        # Functions for the adding of the numbers and adding it to the lists
    while i < len(numbers) and x < len(numbers):
        if numbers[i] >= numbers[x]:
            x += 1
            max = i
        else:
            i += 1
            max = x
        # Comparison between the values to find the favorite color
    return colors_list[max]


def count(list: list[str]) -> dict[str, int]:
    """This is the count function which adds up how many time a word is used."""
    output_dict: dict[str, int] = {}
    for item in list:
        if item in output_dict:
            output_dict[item] += 1
            # Checks the dictionary for the term and if there adds 1
        else:
            output_dict[item] = 1
            # If term is not there adds the term and sets valye to 1
    return output_dict