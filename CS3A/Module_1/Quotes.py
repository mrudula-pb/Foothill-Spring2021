"""HIIIIIIIIIIIIIIIIIIIIIIIII"""


def k():
    """HIIIIIIIIIIIIIIIIIIIIIIIII"""
    print(__doc__)
    print(k.__doc__)
    print('This is string literal named "Sam"')
    print("This is string literal named 'Sam'")
    print('This is string literal named "Sam" with an escape character \"')

    my_name = "My name is Mrudula"
    print(my_name)

    # Variable my_name is pointing to a different Object in memory
    # "My name is Mrudula" string onject is still in memory but nothing is pointing to it.
    # Python garbage collector will collect it
    my_name = "My name is Fred"
    print(my_name)

    one_number = 4
    another_number = 4 # both of these variables point to same value location 4
    # Checking if one_number and another_number is pointing to same value, they point to same Object
    print(id(one_number))
    print(id(another_number))
    print("-----------------------")

    one_number = 4
    another_number = 5
    # Here they point to different objects
    print(id(one_number))
    print(id(another_number))

    # print entire string
    first_string = 'The quick brown fox'
    print(first_string)

    # print individual characters by [0], [1],....
    print(first_string[0])

    # Cannot change the individual characters in string i.e string is immutable
    #first_string[4] = "y"
    #print(first_string)

    # Combine string together
    first_string = 'THe quick brown fox'
    # YOU CAN CHANGE THE STRING VARIABLE VALUE BUT NOT INDIVIDUAL CHARACTERS I.E STRING OBJECT IS IMMUTABLE
    # first_string = "TEST"

    second_string = 'jumped over the wall'
    complete_string = first_string + second_string
    print(complete_string) # INTERNALLY WE HAVE CREATED 3 OBJECTS I.E complete_string, First_string, second_string

    # Take input from user
    no = input('Enter Number: ') # input() method gives type string even though we entered number
    print(no)
    # here the type is string even though the value given is number
    print(type(no))


if __name__ == '__main__':
    k()