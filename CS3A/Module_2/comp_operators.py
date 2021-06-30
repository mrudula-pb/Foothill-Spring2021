
#  == equality operator
def main():
    print(1 == 1)
    print(1 == 2)
    print(type(1 == 1))
    print('me' == 'me')
    a = 3
    b = 5
    print(a == b)
    # Remember float values are stored as fractional approximations, hence below is false. Be careful with floats
    a = .1 + .1 + .1
    b = .3
    print(a == b)


if __name__ == "__main__":
    main()