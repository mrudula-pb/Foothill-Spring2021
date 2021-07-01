"""This program asks the user their name, gives nine options to select and
prints friendly message for selected option
"""


def main():
    """ Obtain and print the name of the user along with greetings """
    name = input("Please enter your name: ")
    print("Hi " + name + ", " + "welcome to Foothill's database project.")
    print_menu()


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
    print(quantity, source_curr, "currency converting", "to", target_curr, "is :", conversion_value)
    return conversion_value


def print_menu():
    """ Prints out nine choices and unique polite message for option entered """
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

    # Correct conversion from USD to another currency with quantity > 1
    if currency_converter(10, "USD", "GBP") == 8.0:
        print("PASS: Conversion from USD to GBP")
    else:
        print("FAIL: Incorrect Conversion from USD to GBP")
    print('_______________')

    # Correct conversion from another currency to USD with quantity > 1
    if currency_converter(6.3, "CHF", "USD") == 6.3:
        print("PASS: Conversion from CHF to USD")
    else:
        print("FAIL: Incorrect Conversion from CHF to USD")
    print('_______________')

    # Correct conversion between two currencies other than USD with quantity > 1
    # (Hint: most conversions will come out messy, try starting with 2.8 CAD)
    if currency_converter(2.8, "CAD", "GBP") == 2.2399999999999998:
        print("PASS: Conversion from CAD to GBP")
    else:
        print("FAIL: Incorrect Conversion from CAD to GBP")
    print('_______________')

    # User enters invalid source currency should raise KeyError
    source = input("Enter Source Currency: ")
    try:
        print(f'{source} is {conversions[source]}')
    except KeyError:
        print(f"PASS: Invalid {source} Currency Raises KeyError")
    print('_______________')

    # User enters invalid target currency should raise KeyError
    target = input("Enter Target Currency: ")
    try:
        print(f'{target} is {conversions[target]}')
    except KeyError:
        print("PASS: Invalid Target Currency Raises KeyError")
    print('_______________')

    print("All Tests Completed")


if __name__ == '__main__':
    # main()
    conversions = {"USD": 1, "EUR": 0.9, "CAD": 1.4, "GBP": 0.8, "CHF": 0.95, "NZD": 1.66, "AUD": 1.62, "JPY": 107.92}

    print("Testing currency_converter: ")
    unit_test()


"""
--- Sample run# 1 ---
Testing currency_converter: 
10 USD currency converting to GBP is : 8.0
PASS: Conversion from USD to GBP
_______________
6.3 CHF currency converting to USD is : 6.3
PASS: Conversion from CHF to USD
_______________
2.8 CAD currency converting to GBP is : 2.2399999999999998
PASS: Conversion from CAD to GBP
_______________
Enter Source Currency: GBP
GBP is 0.8
_______________
Enter Target Currency: CHF
CHF is 0.95
_______________
All Tests Completed

--- Sample run# 2 ---
Testing currency_converter: 
10 USD currency converting to GBP is : 8.0
PASS: Conversion from USD to GBP
_______________
6.3 CHF currency converting to USD is : 6.3
PASS: Conversion from CHF to USD
_______________
2.8 CAD currency converting to GBP is : 2.2399999999999998
PASS: Conversion from CAD to GBP
_______________
Enter Source Currency: INCORRECT
PASS: Invalid INCORRECT Currency Raises KeyError
_______________
Enter Target Currency: INCORRECT
PASS: Invalid Target Currency Raises KeyError
_______________
All Tests Completed

--- Sample run# 3 ---
Testing currency_converter: 
10 USD currency converting to GBP is : 8.0
PASS: Conversion from USD to GBP
_______________
6.3 CHF currency converting to USD is : 6.3
PASS: Conversion from CHF to USD
_______________
2.8 CAD currency converting to GBP is : 2.2399999999999998
PASS: Conversion from CAD to GBP
_______________
Enter Source Currency: @#$@#$2342aesfwerw
PASS: Invalid @#$@#$2342aesfwerw Currency Raises KeyError
_______________
Enter Target Currency: !@$!$!$!$sdfsa
PASS: Invalid Target Currency Raises KeyError
_______________
All Tests Completed

--- Sample run# 4 ---
Testing currency_converter: 
10 USD currency converting to GBP is : 10
FAIL: Incorrect Conversion from USD to GBP
_______________
6.3 CHF currency converting to USD is : 6.3
PASS: Conversion from CHF to USD
_______________
2.8 CAD currency converting to GBP is : 2.8
FAIL: Incorrect Conversion from CAD to GBP
_______________
Enter Source Currency: AEFQWQWEW
PASS: Invalid AEFQWQWEW Currency Raises KeyError
_______________
Enter Target Currency: wqeqwEQWE
PASS: Invalid Target Currency Raises KeyError
_______________
All Tests Completed

"""
