"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730560264"


class Simpy:
    """Establishes the class Simpy."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        """Initializes Simpy."""
        self.values = values

    def __repr__(self) -> str:
        """Prints the return string."""
        return f"Simpy({self.values})"

    def fill(self, float: float, integer: int) -> None:
        """Fill a set number of indexes with a float."""
        i: int = 0
        self.values = []
        while i < integer:
            self.values.append(float)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills a certain amount of indexes with ascending or descending numbers."""
        assert step != 0.0
        i: float = start
        current_value: float = start
        while i != stop:
            self.values.append(current_value)
            current_value = current_value + step
            i += step
    
    def sum(self) -> float:
        """Adds for the total."""
        total = sum(self.values)
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Creates a magic method for addition."""
        new_simpy: Simpy = []
        i: int = 0
        if type(rhs) == float:
            while i < len(self.values):
                new_simpy.append(self.values[i] + rhs)
                i += 1
        elif type(rhs) == Simpy:
            assert len(rhs.values) == len(self.values)
            while i < len(self.values):
                new_simpy.append(self.values[i] + rhs.values[i])
                i += 1  
        return Simpy(new_simpy)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Creates a magic method for power."""
        new_simpy: Simpy = []
        i: int = 0
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                new_simpy.append(self.values[i] ** rhs.values[i])
                i += 1
        elif type(rhs) == float:
            while i < len(self.values):
                new_simpy.append(self.values[i] ** rhs)
                i += 1
        return Simpy(new_simpy)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Creates a magic method for equal."""
        result: list[bool] = []
        i: int = 0
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        elif type(rhs) == float:
            while i < len(self.values):
                if self.values[i] == rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Creates a magic method for greater than."""
        result: list[bool] = []
        i: int = 0
        if type(rhs) == Simpy:
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        if type(rhs) == float:
            while i < len(self.values):
                if self.values[i] > rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Creates a magic method to get item."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result1: list[float] = []
            for i in range(0, len(self.values)):
                if rhs[i]:
                    result1.append(self.values[i]) 
            # dunno how to get from the list to the masked list
            return Simpy(result1)