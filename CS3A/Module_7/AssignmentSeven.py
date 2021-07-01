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


class EmptyDatasetError(Exception):
    def __init__(self, message):
        self.message = message


class NoMatchingItems(Exception):
    def __init__(self, message):
        self.message = message


class DataSet:
    """ the DataSet class will present summary tables based on
    information imported from a .csv file
    """
    copyright = "No copyright has been set"

    def __init__(self, header=""):
        self._data = None
        try:
            self.header = header
        except ValueError:
            self.header = ""

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, new_header: str):
        if isinstance(new_header, str) and \
                len(new_header) <= 30:
            self._header = new_header
        else:
            raise ValueError

    def load_default_data(self):
        self._data = (('Staten Island', 'Private room', 70),
                      ('Brooklyn', 'Private room', 50),
                      ('Bronx', 'Private room', 40),
                      ('Brooklyn', 'Entire home / apt', 150),
                      ('Manhattan', 'Private room', 125),
                      ('Manhattan', 'Entire home / apt', 196),
                      ('Brooklyn', 'Private room', 110),
                      ('Manhattan', 'Entire home / apt', 170),
                      ('Manhattan', 'Entire home / apt', 165),
                      ('Manhattan', 'Entire home / apt', 150),
                      ('Manhattan', 'Entire home / apt', 100),
                      ('Brooklyn', 'Private room', 65),
                      ('Queens', 'Entire home / apt', 350),
                      ('Manhattan', 'Private room', 98),
                      ('Brooklyn', 'Entire home / apt', 200),
                      ('Brooklyn', 'Entire home / apt', 150),
                      ('Brooklyn', 'Private room', 99),
                      ('Brooklyn', 'Private room', 120))
        print(self._data)

    def _cross_table_statistics(self, descriptor_one: str, descriptor_two: str):
        if not self._data:
            raise EmptyDatasetError

        # group by borough and type
        grouped_list_of_data = [((row[0], row[1]), row[2]) for row in self._data]
        print(grouped_list_of_data)

        # find the match for (descriptor_one, descriptor_two) in list_of-data
        req_borough_type = (descriptor_one, descriptor_two)

        matching_properties = [x for x in grouped_list_of_data if x[0] == req_borough_type]

        if not matching_properties:
            raise NoMatchingItems

        list_of_rents = [x[1] for x in matching_properties]

        length = len(list_of_rents)
        average_rent = sum(list_of_rents) / length

        # take minimum, average, and maximum rent of matching properties as a tuple of floats.
        statistics_for_borough_type = (min(list_of_rents), average_rent, max(list_of_rents))

        return statistics_for_borough_type


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


def menu(dataset: DataSet):
    """ present user with options to access the Airbnb dataset """

    currency_options(home_currency)
    print()
    print(dataset.copyright)
    while True:
        print(dataset.header)
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
    if source_curr not in conversions or target_curr not in \
            conversions or quantity <= 0:
        raise ValueError
    in_usd = quantity / conversions[source_curr]
    in_target = in_usd * conversions[target_curr]
    return in_target


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
    air_bnb = DataSet()
    print(air_bnb.header)
    name = input("Please enter your name: ")
    message = "Hi " + name + ", welcome to Foothill's database project."
    print(message)
    while home_currency not in conversions:
        home_currency = input("What is your home currency?")
    while True:
        print("Enter a header for the menu: ")
        header = input()
        try:
            air_bnb.header = header
            break
        except ValueError:
            print(f"Header must be a string less or equal to than thirty "
                  f"characters long")
    menu(air_bnb)


def unit_test():
    my_set = DataSet()
    try:
        my_set._cross_table_statistics()
    except EmptyDatasetError as problem:
        print(problem.message)

    my_set.load_default_data()
    a = DataSet()
    b = DataSet("OK Header")
    c = DataSet("This header is way too long, I am quite sure")
    print("Testing constructor with default parameter: ", end="")
    if a.header == "":
        print("Pass")
    else:
        print("Fail")
    print("Testing constructor with valid header argument: ", end="")
    if b.header == "OK Header":
        print("Pass")
    else:
        print("Fail")
    print("Testing constructor with invalid header argument: ", end="")
    if c.header == "":
        print("Pass")
    else:
        print("Fail")
    print("Testing setter with valid assignment: ", end="")
    c.header = "New header"
    if c.header == "New header":
        print("Pass")
    else:
        print("Fail")
    print("Testing setter with invalid assignment: ", end="")
    try:
        c.header = "This header is way too long, I am quite sure"
    except ValueError:
        if c.header == "New header":
            print("Pass")
        else:
            print("Fail - Exception raised but value is incorrect")
    else:
        print("Fail - Exception not raised")
    print("Setting DataSet.copyright = 'copyright Eric Reed'")
    DataSet.copyright = 'copyright Eric Reed'
    print("Checking that I can access this using DataSet.copyright")
    if DataSet.copyright == 'copyright Eric Reed':
        print("Pass")
    else:
        print("Fail")
    print("Checking that I can access this after created a test object "
          "using test.copyright")
    test = DataSet()
    if test.copyright == 'copyright Eric Reed':
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    unit_test()
    main()
