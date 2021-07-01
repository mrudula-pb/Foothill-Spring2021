
"""This program asks the user their name, gives nine options to select and
prints friendly message for selected option
"""


home_currency = ""


def main():
    """Obtain and print the name of the user along with greetings"""
    name = input("Please enter your name: ")
    print("Hi " + name + ", " + "welcome to Foothill's database project.")
    print_menu()


def currency_options(base_curr: str):
    """ Prints out a table of options for converting base_curr to all other currencies

    Args:
        base_curr (str): base currency to convert from to converted_currency
    """

    print(f"Options for converting from {base_curr}:")
    currency_list = list(conversions.keys())

    base_first_curr_list = [base_curr]
    print("base_first_curr_list: ", base_first_curr_list)
    for item in currency_list:
        if item != base_curr:
            base_first_curr_list.append(item)
    # print("base_first_curr_list: ", base_first_curr_list)

    for curr in base_first_curr_list:
        print(f'{curr:>3}', end='      ')
    print()
    for convert_curr in range(10, 91, 10):
        # print("convert_curr: ", convert_curr)
        for currency in base_first_curr_list:
            # print('currency: ', currency)
            if currency == base_curr:
                converted_curr = convert_curr
                # print('converted_curr: ', converted_curr)
            else:
                converted_curr = currency_converter(convert_curr, base_curr, currency)
                # print('converted_curr: ', converted_curr)
            print(f'{converted_curr:>5.2F}', end='    ')
            # print()
        print()


def currency_converter(quantity: float, source_curr: str, target_curr: str) -> float:
    """ Calculates the value after converting money from source_curr currency to target_curr

    Args:
        quantity (int): the amount of money in the original currency
        source_curr (str): the original currency
        target_curr (str): the currency after exchange
    Returns:
        float: the value after converting money from source_curr currency to target_curr
    """
    conversion_value = quantity * conversions[target_curr]
    # print(quantity, source_curr, "currency converting", "to", target_curr, "is :", conversion_value)
    return conversion_value


def print_menu():
    """ Prints out nine choices and unique polite message for option entered """

    while True:
        home_currency = input("What is your home currency: ")
        if home_currency not in conversions:
            continue
        else:
            currency_options(home_currency)
            break

    choice = 0
    while choice < 10:
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
        option = input("What is your choice? ")

        try:
            int_option = int(option)
        except ValueError:
            print("Please enter a number only")
            continue
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
            print('Goodbye!  Thank you for using the database')
            break
        else:
            print("Please enter a number between 1 and 9")


def unit_test():
    """ Unit Testing for Currency Converter """
    if currency_converter(10, "USD", "GBP") == 8.0:
        print("PASS: Conversion from USD to GBP")
    else:
        print("FAIL: Incorrect Conversion from USD to GBP")
    print('_______________')

    if currency_converter(6.3, "CHF", "USD") == 6.3:
        print("PASS: Conversion from CHF to USD")
    else:
        print("FAIL: Incorrect Conversion from CHF to USD")
    print('_______________')

    if currency_converter(2.8, "CAD", "GBP") == 2.2399999999999998:
        print("PASS: Conversion from CAD to GBP")
    else:
        print("FAIL: Incorrect Conversion from CAD to GBP")
    print('_______________')

    source = input("Enter Source Currency: ")
    try:
        print(f'{source} is {conversions[source]}')
    except KeyError:
        print(f"PASS: Invalid {source} Currency Raises KeyError")
    print('_______________')

    target = input("Enter Target Currency: ")
    try:
        print(f'{target} is {conversions[target]}')
    except KeyError:
        print("PASS: Invalid Target Currency Raises KeyError")
    print('_______________')

    print("All Tests Completed")


if __name__ == '__main__':
    conversions = {"USD": 1, "EUR": 0.9, "CAD": 1.4, "GBP": 0.8, "CHF": 0.95, "NZD": 1.66, "AUD": 1.62, "JPY": 107.92}
    main()

    print("Testing currency_converter: ")
    # unit_test()


"""
--- Sample run# 1 ---
Please enter your name: ZXC
Hi ZXC, welcome to Foothill's database project.
What is your home currency: GBP
Options for converting from GBP:
GBP      USD      EUR      CAD      CHF      NZD      AUD      JPY      
10.00    10.00     9.00    14.00     9.50    16.60    16.20    1079.20    
20.00    20.00    18.00    28.00    19.00    33.20    32.40    2158.40    
30.00    30.00    27.00    42.00    28.50    49.80    48.60    3237.60    
40.00    40.00    36.00    56.00    38.00    66.40    64.80    4316.80    
50.00    50.00    45.00    70.00    47.50    83.00    81.00    5396.00    
60.00    60.00    54.00    84.00    57.00    99.60    97.20    6475.20    
70.00    70.00    63.00    98.00    66.50    116.20    113.40    7554.40    
80.00    80.00    72.00    112.00    76.00    132.80    129.60    8633.60    
90.00    90.00    81.00    126.00    85.50    149.40    145.80    9712.80    
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
Min/Avg/Max by Property Type
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
Testing currency_converter: 
"""