
def factorial(base: int):
    if base < 0:
        raise ValueError #
    result = 1
    for i in range(base + 1, 0, -1):
        result *= i
    return result


if __name__ == '__main__':
    print(factorial(5))
    print(factorial(-1))
