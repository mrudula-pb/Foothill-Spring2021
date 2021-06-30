
def main():
    value = "10000000"
    name = "Erica"
    print("My name is", name, "and I have", "$", value)  # My name is Erica I own $ 10000000

    # To remove spaces between arguments use sep = "", say between $ 10000000
    print("My name is", name, "and I have", "$", value, sep="")  # My name isEricaand I have$10000000

    # To create space between "name" and string, provide space towards end of string
    print("My name is ", name, " and I have ", "$", value, sep="")


if __name__ == '__main__':
    main()