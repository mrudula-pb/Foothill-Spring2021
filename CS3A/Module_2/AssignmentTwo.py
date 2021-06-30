"""This program asks the user their name, gives nine options to select and
prints friendly message for selected option
"""


def main():
    """ Obtain and print the name of the user along with greetings """
    name = input("Please enter your name: ")
    print("Hi " + name + ", " + "welcome to Foothill's database project.")
    print("Main Menu")
    menu()


def print_menu():
    """ Prints out the nine choices """
    print("1 - Print Average Rent by Location and Property Type")
    print("2 - Print Minimum Rent by Location and Property Type")
    print("3 - Print Maximum Rent by Location and Property Type")
    print("4 - Print Min/Avg/Max by Location")
    print("5 - Print Min/Avg/Max by Property Type")
    print("6 - Adjust Location Filters")
    print("7 - Adjust Property Type Filters")
    print("8 - Load Data")
    print("9 - Quit")


def menu():
    """ Gives unique polite message for option entered """
    print_menu()
    option = input("What is your choice? ")
    try:
        int_option = int(option)
    except ValueError:
        print("Please enter a number only")
    except ZeroDivisionError:
        print('Please do not enter zero')
    else:
        if int_option == 1:
            print("Average Rent by Location and Property Type")
        elif int_option == 2:
            print("Minimum Rent by Location and Property Type")
        elif int_option == 3:
            print("Maximum Rent by Location and Property Type")
        elif int_option == 4:
            print("Min/Avg/Max by Location")
        elif int_option == 5:
            print("Min/Avg/Max by Property Type")
        elif int_option == 6:
            print("Adjust Location Filters")
        elif int_option == 7:
            print("Adjust Property Type Filters")
        elif int_option == 8:
            print("Load Data")
        elif int_option == 9:
            print("Quit")
        else:
            print("Please enter a number between 1 and 9")


if __name__ == '__main__':
    main()

"""
--- Sample run# 1 ---
Please enter your name: Mrudula
Hi Mrudula, welcome to Foothill's database project.
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 1
Average Rent by Location and Property Type

--- Sample run# 2 ---
Please enter your name: Mrudula
Hi Mrudula, welcome to Foothill's database project.
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 4
Min/Avg/Max by Location

--- Sample run# 3 ---
Please enter your name: Mrudula
Hi Mrudula, welcome to Foothill's database project.
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 12
Please enter a number between 1 and 9

--- Sample run# 4 ---
Please enter your name: Mrudula
Hi Mrudula, welcome to Foothill's database project.
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? e
Please enter a number only
"""
