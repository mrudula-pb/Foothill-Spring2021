
# Here we are creating our own error instead of ValueError
class TooHighNumberError(Exception): # We are inheriting/adopting all the methods of Exception class without typing them
    def __init__(self, message): # We are overriding init method from Exception class
        self.message = message # self.message is instance attribute

def factorial(base: int):
    if base < 0:
        raise TooHighNumberError("Please use a non-negative integer for base")
    result = 1
    for i in range(base + 1, 0, -1):
        result *= i
    return result


if __name__ == '__main__':
    print(factorial(5))
    try:
        print(factorial(-1))
    except TooHighNumberError as problem: # problem is alias for TooHighNumberError
        print(problem.message)