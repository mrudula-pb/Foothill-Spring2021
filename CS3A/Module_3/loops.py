
def main():
    sun_shines = True
    while sun_shines:
        print("Make Hay!")
        response = input("Is the sun shining? Yes or No: ")
        if response == 'No':
            sun_shines = False
        print("THank you for the answer")
    print("No more HAY! goodBye!")


def main_new():
    """ This is main_new function """
    bales = 0
    while bales < 10:
        print("Make Hay! we need 10 bales")
        response = input("How many bales of hay do you have: ")
        bales = int(response)
        print("THank you for the answer")
    print("No more HAY! goodBye!")


def main_new1():
    bales = 0
    while bales < 10:
        print("Make Hay! we need 10 bales")
        response = input("How many bales of hay do you have: ")
        if response == "quit":
            print('Sorry to see you go..')
            break
        try:
            bales = int(response)
        except ValueError:
            print("Please enter number")
            continue
        print("THank you for the answer")
    print("No more HAY! goodBye!")

if __name__ == '__main__':
    # main()
    main_new1()
    print(main_new.__doc__)
