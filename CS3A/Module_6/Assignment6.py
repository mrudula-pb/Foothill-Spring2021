"""
Based on the user's chosen home currency, this program prints out a
table of conversions to other currencies.  A menu is presented in a loop
but the functions are not yet implemented.
"""

conversions = {
    "USD": 1,
    "EUR": .9,
    "CAD": 1.4,
    "GBP": .8,
    "CHF": .95,
    "NZD": 1.66,
    "AUD": 1.62,
    "JPY": 107.92
}

home_currency = ""


class DataSet:
    copyright = "No copyright has been set"

    def __init__(self, header=""):
        try:
            self.header = header
        except ValueError:
            self._header = ""
        self._data = None

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header: str):
        header_length = len(header)
        if (header == "Welcome to the airBNB Database") and (header_length >= 30):
            self._header = header
        else:
            raise ValueError
        # self._header = ""


def print_menu():
    """ Display the main menu text. """
    print("Main Menu")
    print("1 - Print Average Rent by Location and Property Type")
    print("2 - Print Minimum Rent by Location and Property Type")
    print("3 - Print Maximum Rent by Location and Property Type")
    print("4 - Print Min/Avg/Max by Location")
    print("5 - Print Min/Avg/Max by Property Type")
    print("6 - Adjust Location Filters")
    print("7 - Adjust Property Type Filters")
    print("8 - Load Data")
    print("9 - Quit")


def menu(dataset):
    print(dataset.copyright)
    print(dataset.header)

    currency_options(home_currency)
    while True:
        print_menu()
        try:
            selection = int(input("What is your choice? "))
        except ValueError:  # Talk about why this needs to be here
            print("Please enter a number only")
            continue
        if selection == 1:
            print("Average rent functionality is not implemented yet")
        elif selection == 2:
            print("Minimum rent functionality is not implemented yet")
        elif selection == 3:
            print("Maximum rent functionality is not implemented yet")
        elif selection == 4:
            print("Location functionality is not implemented yet")
        elif selection == 5:
            print("Property type functionality is not implemented yet")
        elif selection == 6:
            print("Location filter functionality is not implemented yet")
        elif selection == 7:
            print("Property type functionality is not implemented yet")
        elif selection == 8:
            print("Load data functionality is not implemented yet")
        elif selection == 9:
            print("Goodbye!  Thank you for using the database")
            break
        else:
            print("Please enter a number between 1 and 9")


def currency_converter(quantity: float, source_curr: str, target_curr: str):
    """ Convert from one unit of currency to another.

    Keyword arguments:
        quantity -- a float representing the amount of currency to be
                    converted.
        source_curr -- a three letter currency identifier string from
                       the conversions dictionary
        target_curr -- a three letter currency identifier string from
                       the conversions dictionary
    """

    return quantity / conversions[source_curr] * conversions[target_curr]


def currency_options(base_curr='EUR'):
    """ Present a table of common conversions from base_curr to other
    currencies.
    """
    print(f"Options for converting from {base_curr}:")
    print(f"{base_curr:10}", end="")
    for target in conversions:
        if target == base_curr:
            continue
        else:
            print(f"{target:10}", end="")
    print()
    for i in range(10, 100, 10):
        print(f"{i:<10.2f}", end="")
        for target in conversions:
            if target == base_curr:
                continue
            print(f"{currency_converter(i, base_curr, target):<10.2f}", end="")
        print()


def main():
    global home_currency

    copyright = input("Please enter your name: ")
    message = "Hi " + copyright + ", welcome to Foothill's database project."
    print(message)
    air_bnb = DataSet()
    while home_currency not in conversions:
        home_currency = input("What is your home currency? ")
        air_bnb.header = input("Enter a header for the menu: ")
    menu(air_bnb)


def unit_test():
    """ Unit Testing for header and copyright properties"""
    dataset_one = DataSet()
    dataset_two = DataSet("Welcome to the airBNB Database")
    dataset_three = DataSet()
    dataset_four = DataSet()
    dataset_five = DataSet()

    if dataset_one.header == "":
        print("Testing constructor with default parameter: Pass")
    else:
        print("Testing constructor with default parameter: Fail")
    print('_______________')

    if dataset_two.copyright == "No copyright has been set":
        print("Testing constructor with valid header argument: Pass")
    else:
        print("Testing constructor with valid header argument: Fail")
    print('_______________')


if __name__ == "__main__":
    unit_test()
    main()


"""
--- Sample run# 1 ----
Testing constructor with default parameter: Pass
_______________
Testing constructor with valid header argument: Pass
_______________
Please enter your name: Mrudula
Hi Mrudula, welcome to Foothill's database project.
What is your home currency? GBP
Enter a header for the menu: Welcome to the airBNB Database
No copyright has been set
Welcome to the airBNB Database
Options for converting from GBP:
GBP       USD       EUR       CAD       CHF       NZD       AUD       JPY       
10.00     12.50     11.25     17.50     11.88     20.75     20.25     1349.00   
20.00     25.00     22.50     35.00     23.75     41.50     40.50     2698.00   
30.00     37.50     33.75     52.50     35.62     62.25     60.75     4047.00   
40.00     50.00     45.00     70.00     47.50     83.00     81.00     5396.00   
50.00     62.50     56.25     87.50     59.38     103.75    101.25    6745.00   
60.00     75.00     67.50     105.00    71.25     124.50    121.50    8094.00   
70.00     87.50     78.75     122.50    83.12     145.25    141.75    9443.00   
80.00     100.00    90.00     140.00    95.00     166.00    162.00    10792.00  
90.00     112.50    101.25    157.50    106.88    186.75    182.25    12141.00  
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
What is your choice? 5
Property type functionality is not implemented yet
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
What is your choice? 9
Goodbye!  Thank you for using the database

--- Sample run# 2 ----
Testing constructor with default parameter: Pass
_______________
Testing constructor with valid header argument: Pass
_______________
Please enter your name: Mrudula
Hi Mrudula, welcome to Foothill's database project.
What is your home currency? USD
Enter a header for the menu: Welcome to the airBNB DatabaseWelcome to the airBNB DatabaseWelcome to the airBNB Database
Traceback (most recent call last):
  File "/home/mdot/MyAssignments/CS3A/Module_6/PROF_CODE.py", line 166, in <module>
    main()
  File "/home/mdot/MyAssignments/CS3A/Module_6/PROF_CODE.py", line 139, in main
    air_bnb.header = input("Enter a header for the menu: ")
  File "/home/mdot/MyAssignments/CS3A/Module_6/PROF_CODE.py", line 41, in header
    raise ValueError
ValueError

"""