
# global variables
president = "Joe Biden"
national_pastime = "Baseball"


def house_one():
    dinner = 'Chicken'

    def randall():
        print('-----------------------')
        book = "Catch22"

        print(f'At the alice level, the president is {president}')
        print(f'At the alice level, the national pastime is {national_pastime}')

        # at the local function level
        print(f"At the alice level, dinner is {book}")
        print(f"At the alice level, dinner is {dinner}")  # randall lives in house_one, so she knows the dinner
        # is chicken

    def alice():
        print('-----------------------')
        book = "Dairy of a wimpy kid"

        print(f'At the alice level, the president is {president}')
        print(f'At the alice level, the national pastime is {national_pastime}')

        # at the local function level
        print(f"At the alice level, dinner is {book}")
        print(f"At the alice level, dinner is {dinner}")  # alice lives in house_one, so she knows the dinner is chicken

    # we still have access to global variables
    print(f'At the house_one level, the president is {president}')
    print(f'At the house_one level, the national pastime is {national_pastime}')

    # at the local function level
    print(f"At the house_one level, dinner is {dinner}")
    alice()
    randall()


def clubhouse():
    print('-----------------------')
    # temporarily the president is Betty
    president = "Betty"  # Here president is Betty in clubhouse, it's not an error, pycharm is informing you
    print(f'At the clubhouse level, president is {president}')


# global variables
print(f'At the global level, the president is {president}')
print(f'At the global level, the national pastime is {national_pastime}')


if __name__ == '__main__':
    house_one()
    clubhouse()
    print("______________")
    print(f'At the global level, the president is {president}')  # president is still Joe Biden

# scope of dinner variable doesn't exist at global level
print(f"At the global level, dinner is {dinner}")
