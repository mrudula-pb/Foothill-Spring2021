import copy
from enum import Enum

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


class Categories(Enum):
    """to distinguish the two categorical variables we have in our dataset"""
    LOCATION = 1
    PROPERTY_TYPE = 2


class Stats(Enum):
    """to select which statistic to display in the display_cross_table() method"""
    MIN = 1
    AVG = 2
    MAX = 3


class DataSet:
    """ the DataSet class will present summary tables based on
    information imported from a .csv file
    """

    class EmptyDatasetError(Exception):
        pass

    class NoMatchingItems(Exception):
        pass

    copyright = "No copyright has been set"
    category_values = []

    def __init__(self, header=""):
        self._data = None
        self._labels = {Categories.LOCATION.name: set(), Categories.PROPERTY_TYPE.name: set()}

        # This dictionary will start out identical to self._labels, but we will give the user the opportunity
        # to make some labels "inactive" by removing them from the _active_labels set.

        # initialize self._active_labels, using the same scheme we used for self._labels.
        self._active_labels = {Categories.LOCATION.name: set(), Categories.PROPERTY_TYPE.name: set()}

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

    def _initialize_sets(self):
        """initialize the sets"""
        location_set_data = set()
        propertyType_set_data = set()

        if not self._data:
            raise DataSet.EmptyDatasetError("No data loaded")

        set_data = set(self._data)

        for location in set_data:
            location_set_data.add(location[0])

        for property_type in set_data:
            propertyType_set_data.add(property_type[1])

        self._labels[Categories.LOCATION.name] = location_set_data
        self._labels[Categories.PROPERTY_TYPE.name] = propertyType_set_data

        new_location_set_data = copy.deepcopy(location_set_data)
        new_propertyType_set_data = copy.deepcopy(propertyType_set_data)

        self._active_labels[Categories.LOCATION.name] = new_location_set_data
        self._active_labels[Categories.PROPERTY_TYPE.name] = new_propertyType_set_data

        print('ID of _labels; ', id(self._labels))
        print('ID of _active_labels; ', id(self._active_labels))

        print(self._active_labels)
        print(self._labels)

        return self._labels, self._active_labels

    def load_default_data(self):
        """ Load sample data into self.__data"""
        self._data = [("Staten Island", "Private room", 70),
                      ("Brooklyn", "Private room", 50),
                      ("Bronx", "Private room", 40),
                      ("Brooklyn", "Entire home / apt", 150),
                      ("Manhattan", "Private room", 125),
                      ("Manhattan", "Entire home / apt", 196),
                      ("Brooklyn", "Private room", 110),
                      ("Manhattan", "Entire home / apt", 170),
                      ("Manhattan", "Entire home / apt", 165),
                      ("Manhattan", "Entire home / apt", 150),
                      ("Manhattan", "Entire home / apt", 100),
                      ("Brooklyn", "Private room", 65),
                      ("Queens", "Entire home / apt", 350),
                      ("Manhattan", "Private room", 98),
                      ("Brooklyn", "Entire home / apt", 200),
                      ("Brooklyn", "Entire home / apt", 150),
                      ("Brooklyn", "Private room", 99),
                      ("Brooklyn", "Private room", 120)]
        # As soon as the default data is loaded, we want to initialize _labels.  So, call self._initialize_sets()
        # at an appropriate spot in this method.
        self._initialize_sets()

    def get_labels(self, category: Categories):
        """Returns a list of the items in _labels[category]"""
        return list(self._labels[category.name])

    def get_active_labels(self, category: Categories):
        """Returns a list of the items in _active_labels[category]"""
        return list(self._active_labels[category.name])

    def toggle_active_label(self, category: Categories, descriptor: str):
        # If the passed descriptor is not a label in _labels[category], raise KeyError.
        if descriptor not in self._labels[category.name]:
            raise KeyError

        cat_act_labels = self._active_labels[category.name]
        print(cat_act_labels)

        # add descriptor to _active_labels[category] if descriptor is not in the set or...
        if descriptor not in cat_act_labels:
            cat_act_labels.add(descriptor)
        else:
            # remove descriptor from _active_labels[category] if descriptor is in the set.
            cat_act_labels.remove(descriptor)

    def display_cross_table(self, stat: Stats):
        """Display list data, min, max, average in rows and columns in an order"""

        if not self._data:
            raise DataSet.EmptyDatasetError("No data loaded")

        # copying both self._labels sets into lists, which guarantees that the order of the objects will remain fixed.
        location_list = list(self._labels['LOCATION'])
        property_type_list = list(self._labels['PROPERTY_TYPE'])

        # print('M---', location_list)
        # print('M---', property_type_list)
        #                Private room     Entire home / apt
        prop_types = [''] + property_type_list

        # for prop_type in property_type_list:
        #     print(prop_type, end='\t')
        # print('\n')

        # use the lists instead of the sets throughout the rest of the function.  Use f-strings to format the
        # table nicely.
        all_prop_stats = []
        for propertyT in property_type_list:
            # collecting data for propertyT for all locations
            prop_type_single = []
            for location in location_list:
                try:
                    stat_for_loc_prop = self._cross_table_statistics(location, propertyT)

                    loc_min, loc_avg, loc_max = stat_for_loc_prop
                    stat_val = None
                    if stat == Stats.AVG:
                        stat_val = loc_avg
                    elif stat == Stats.MIN:
                        stat_val = loc_min
                    else:
                        stat_val = loc_max
                    # print(location, propertyT, stat_val)

                except DataSet.NoMatchingItems:
                    # print(location, propertyT, 'N/A')
                    stat_val = 'N/A'
                prop_type_single.append(f'$ {stat_val}')

            all_prop_stats.append(prop_type_single)

        data = [prop_types] + list(zip(location_list, *all_prop_stats))
        # print(data)

        for i, d in enumerate(data):
            line = ''.join(str(x).ljust(22) for x in d)
            print(line)
            if i == 0:
                print('-' * len(line))

    def _cross_table_statistics(self, descriptor_one: str,
                                descriptor_two: str):
        """ Given a label from each category, calculate summary
        statistics for the items matching both labels.

        Keyword arguments:
            descriptor_one -- the label for the first category
            descriptor_two -- the label for the second category

        Returns a tuple of min, average, max from the matching rows.
        """
        if not self._data:
            raise DataSet.EmptyDatasetError("No data loaded")

        value_list = [item[2] for item in self._data if
                      item[0] == descriptor_one and item[1] == descriptor_two]

        if len(value_list) == 0:
            raise DataSet.NoMatchingItems

        return min(value_list), sum(value_list) / len(value_list), \
            max(value_list)


def manage_filters(dataset: DataSet, category: Categories):
    # Print a menu-like list of all the labels for the given category
    category_labels = dataset.get_labels(category)
    index = 1
    for index, label in enumerate(category_labels, start=1):
        is_label_active = label in dataset.get_active_labels(category)
        print(index, ":", label,"ACTIVE" if is_label_active else "INACTIVE")

    # Indicate which ones are currently active (i.e. the string
    # exists in dataset._active_labels[category]
    # The following labels are in the dataset:

    while True:
        try:
            selection = int(input("Please select an item to toggle or enter a blank line when you are finished. "))
            print("MY SELECTION:", selection)
            selected_descriptor = category_labels[selection - 1]
            dataset.toggle_active_label(category, selected_descriptor)
            for index, label in enumerate(category_labels, start=1):
                is_label_active = label in dataset.get_active_labels(category)
                print(index, ":", label, "ACTIVE" if is_label_active else "INACTIVE")
        except IndexError:
            print("SELECTED NUMBER OUT OF RANGE")
            

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
    print(DataSet.copyright)

    while True:
        print(dataset.header)
        print_menu()
        try:
            selection = int(input("What is your choice? "))
        # We have now implemented the first three items from our menu.  Adjust the menu() function to display the
        # cross table appropriately when the user selects 1, 2 or 3.  Catch any EmptyDatasetError that was raised
        # and provide an appropriate message to the user.
            if selection == 1:
                dataset.display_cross_table(Stats.AVG)
            elif selection == 2:
                print("Minimum rent functionality is not implemented yet")
                dataset.display_cross_table(Stats.MAX)
            elif selection == 3:
                print("Maximum rent functionality is not implemented yet")
                dataset.display_cross_table(Stats.MIN)
            elif selection == 4:
                print("Location functionality is not implemented yet")
            elif selection == 5:
                print("Property type functionality is not implemented yet")
            elif selection == 6:
                print("Location filter functionality is not implemented yet")
            elif selection == 7:
                print("Property type functionality is not implemented yet")
            # Also if the user selects option 8, call load_default_data()
            elif selection == 8:
                dataset.load_default_data()
            elif selection == 9:
                print("Goodbye!  Thank you for using the database")
                break
            else:
                print("Please enter a number between 1 and 9")

        except ValueError:   # Talk about why this needs to be here
            print("Please enter a number only")
            continue
        except DataSet.EmptyDatasetError:
            print("Please Load a Dataset First")
            continue


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


def main_2():
    air_bnb = DataSet()
    air_bnb.load_default_data()
    # air_bnb.display_cross_table(Stats.AVG)
    # air_bnb._initialize_sets()
    # air_bnb.get_labels(Categories.LOCATION)
    # air_bnb.get_active_labels(Categories.LOCATION)

    print("Labels before Toggle", air_bnb.get_labels(Categories.LOCATION))
    print("Active labels before Toggle", air_bnb.get_active_labels(Categories.LOCATION))
    air_bnb.toggle_active_label(category=Categories.LOCATION, descriptor="Bronx")
    print("Active labels after TOGGLE", air_bnb.get_active_labels(Categories.LOCATION))
    print("Labels after Toggle", air_bnb.get_labels(Categories.LOCATION))
    manage_filters(air_bnb, category=Categories.LOCATION)


def unit_test():
    my_set = DataSet()
    print("Testing _cross_table_statistics")

    try:
        my_set._cross_table_statistics("test", "test")
        print("Method Raises EmptyDataSet Error: Fail")
    except my_set.EmptyDatasetError:
        print("Method Raises EmptyDataSet Error: Pass")
    except:
        print("Method Raises EmptyDataSet Error: Fail")

    my_set.load_default_data()

    try:
        my_set._cross_table_statistics("Queens", "a")
        print("No Matching Rows Raises NoMatchingItems: Fail")
    except DataSet.NoMatchingItems:
        print("No Matching Rows Raises NoMatchingItems: Pass")
    except:
        print("No Matching Rows Raises NoMatchingItems: Fail")

    try:
        my_set._cross_table_statistics("a", "Private Room")
        print("No Matching Rows Raises NoMatchingItems: Fail")
    except DataSet.NoMatchingItems:
        print("No Matching Rows Raises NoMatchingItems: Pass")
    except:
        print("No Matching Rows Raises NoMatchingItems: Fail")

    try:
        my_set._cross_table_statistics("Queens", "Private Room")
        print("No Matching Rows Raises NoMatchingItems: Fail")
    except DataSet.NoMatchingItems:
        print("No Matching Rows Raises NoMatchingItems: Pass")
    except:
        print("No Matching Rows Raises NoMatchingItems: Fail")

    if my_set._cross_table_statistics("Queens", "Entire home / apt") == \
            (350, 350, 350):
        print("One Matching Row Returns Correct Tuple: Pass")
    else:
        print("One Matching Row Rows Returns Correct Tuple: Fail")

    if my_set._cross_table_statistics("Manhattan", "Private room") == \
            (98, 111.5, 125):
        print("Multiple Matching Rows Returns Correct Tuple: Pass")
    else:
        print("Multiple Matching Rows Returns Correct Tuple: Fail")
    print(f"{my_set._cross_table_statistics('Manhattan', 'Private room')}")
    if my_set._cross_table_statistics("Brooklyn", "Private room") == \
            (50, 88.8, 120):
        print("Multiple Matching Rows Returns Correct Tuple: Pass")
    else:
        print("Multiple Matching Rows Returns Correct Tuple: Fail")


if __name__ == "__main__":
    # main()
    main_2()
    # unit_test()


"""
------Sample run# 1-------

Please enter your name: Mrudula
Hi Mrudula, welcome to Foothill's database project.
What is your home currency?EUR
Enter a header for the menu: 
AirBNB
Options for converting from EUR:
EUR       USD       CAD       GBP       CHF       NZD       AUD       JPY       
10.00     11.11     15.56     8.89      10.56     18.44     18.00     1199.11   
20.00     22.22     31.11     17.78     21.11     36.89     36.00     2398.22   
30.00     33.33     46.67     26.67     31.67     55.33     54.00     3597.33   
40.00     44.44     62.22     35.56     42.22     73.78     72.00     4796.44   
50.00     55.56     77.78     44.44     52.78     92.22     90.00     5995.56   
60.00     66.67     93.33     53.33     63.33     110.67    108.00    7194.67   
70.00     77.78     108.89    62.22     73.89     129.11    126.00    8393.78   
80.00     88.89     124.44    71.11     84.44     147.56    144.00    9592.89   
90.00     100.00    140.00    80.00     95.00     166.00    162.00    10792.00  

No copyright has been set
AirBNB
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
Please Load a Dataset First
AirBNB
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
What is your choice? 8
AirBNB
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
                      Entire home / apt     Private room          
------------------------------------------------------------------
Bronx                 $ N/A                 $ 40.0                
Brooklyn              $ 166.66666666666666  $ 88.8                
Manhattan             $ 156.2               $ 111.5               
Queens                $ 350.0               $ N/A                 
Staten Island         $ N/A                 $ 70.0                
AirBNB
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
What is your choice? 2
Minimum rent functionality is not implemented yet
                      Entire home / apt     Private room          
------------------------------------------------------------------
Bronx                 $ N/A                 $ 40                  
Brooklyn              $ 200                 $ 120                 
Manhattan             $ 196                 $ 125                 
Queens                $ 350                 $ N/A                 
Staten Island         $ N/A                 $ 70                  
AirBNB
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
What is your choice? 3
Maximum rent functionality is not implemented yet
                      Entire home / apt     Private room          
------------------------------------------------------------------
Bronx                 $ N/A                 $ 40                  
Brooklyn              $ 150                 $ 50                  
Manhattan             $ 100                 $ 98                  
Queens                $ 350                 $ N/A                 
Staten Island         $ N/A                 $ 70                  
AirBNB
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

"""