from enum import Enum


class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


c = Colour.RED
print(c.name)
print(c.value)