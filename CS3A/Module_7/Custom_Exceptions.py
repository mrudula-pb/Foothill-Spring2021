
class TooHighNumberError(Exception):
    def __init__(self, message):
        self.message = message


class NoMatchingItems(Exception):
    def __init__(self, message):
        self.message = message


def factorial(base: int):
    if base < 0:
        raise TooHighNumberError('PLease use a non-negative integer for base')
    result = 1
    for i in range(base+1, 0, -1):
        result *= i
    return result


print(factorial(5))
try:
    print(factorial(-1))
except TooHighNumberError as problem:
    print(problem.message)