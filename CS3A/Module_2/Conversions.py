def main():
    age = input("How old is your cat? ")
    print(age)
    print(type(age))
    # new_age = age + 1 # cannot add int to string
    # print("In a year your cat will be: " , new_age)

    # Type conversion
    int_age = int(age)
    print(type(int_age))
    new_age = int_age + 1
    print("In a year your cat will be: ", new_age)

    age = int(input("How old is your cat? "))
    print(age)
    print(type(age))
    new_age = int_age + 1
    print("In a year your cat will be: ", new_age)

    # convert str to int
    my_int = 4
    my_str = str(my_int)
    print("Type of my_str is: ", type(my_str))
    print("Value of my_str is: ", my_str)


if __name__ != "__main__":
    main()
