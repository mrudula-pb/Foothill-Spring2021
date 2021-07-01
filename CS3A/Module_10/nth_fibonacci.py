# fibonacci numbers = 1,1,2,3,5,8,13,21,....
# first number is at 0th place

def fibonacci(n: int):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# recursive functions are resource intensive, check with n = 50
n = 20
print(fibonacci(n))
