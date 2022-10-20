"""Dictionary related utility functions."""

__author__ = "730560264"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(dict1: dict[str, list[str]], int1: int) -> dict[str, list[str]]:
    """This is head function which shows the first 5 rows of data."""
    result: dict[str, list[str]] = {}
    max: int = int1
    for column in dict1:
        if len(dict1) <= int1:
            result = dict1
        else:
            list1: list[str] = []
            i: int = 0
            while i < max:
                list1.append(dict1[column][i])
                i += 1
            result[column] = list1
    return result


def select(dict1: dict[str, list[str]], list1: list[str]) -> dict[str, list[str]]:
    """This is select function which selects the columns."""
    result: dict[str, list[str]] = {}
    for column in list1:
        for key in dict1:
            result[column] = dict1[column]
    return result


def concat(dict1: dict[str, list[str]], dict2: dict[str, list[str]]) -> dict[str, list[str]]:
    """This is concat function which adds more data."""
    result: dict[str, list[str]] = {}
    for column in dict1:
        result[column] = dict1[column]
    for column in dict2:
        if column in result:
            result[column] += dict2[column]
        else:
            result[column] = dict2[column]
    return result


def count(list1: list[str]) -> dict[str, int]:
    """This is count function which adds up the columns."""
    result: dict[str, int] = {}
    for item in list1:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
