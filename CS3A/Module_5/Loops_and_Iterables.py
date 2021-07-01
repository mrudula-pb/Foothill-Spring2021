
def main():
    my_string = "The cat jumped over the lazy dog"
    print(my_string)

    print(my_string[0])  # print first character of string
    print(my_string[-1])  # print last character of string
    print("____________________")

    for character in my_string:  # my_string is an iterable just as dictionary
        if character == 'e':
            continue
        if character == 'Z':  # or 'z'
            break
        print(character, end='')  # end='' will print in same line
    else:
        print()  # this will help print in next line, you can also use \n within "" as below
        print("Printed whole string")

    print()
    print("____________________")

    for item in range(len(my_string)):
        print(my_string[item], end='')
    print("\n____________________")  # \n will print in new line


if __name__ == '__main__':
    main()