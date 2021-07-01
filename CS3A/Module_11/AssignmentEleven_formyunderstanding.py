import copy
from csv import reader
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


filename = 'AB_NYC_2019.csv'


class DataSet:
    """ the DataSet class will present summary tables based on
    information imported from a .csv file
    """

    class EmptyDatasetError(Exception):
        """ handle EmptyDatasetError Exception """
        pass

    class NoMatchingItems(Exception):
        """ handle NoMatchingItems Exception """
        pass

    copyright = 'Copyright 2021 Mrudula PB'
    category_values = []

    def __init__(self, header=""):
        self._data = None
        self._labels = {Categories.LOCATION.name: set(), Categories.PROPERTY_TYPE.name: set()}
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
        """ initialize the sets """
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

        # print('ID of _labels; ', id(self._labels))
        # print('ID of _active_labels; ', id(self._active_labels))

        # print(self._active_labels)
        # print(self._labels)

        return self._labels, self._active_labels

    def load_file(self):
        """ Loading all the data from the Airbnb data file into self._data """
        # count = 0
        with open(filename, 'r', newline='') as read_obj:
            csv_reader = reader(read_obj, skipinitialspace=True)
            next(csv_reader)
            row_data = [[row[1], row[2], int(row[3])] for row in csv_reader]
            # print("row_data: ", row_data)

            self._data = list(map(tuple, row_data))
            # print("self._data: ", self._data)

            count_records = len(self._data)

            # for _ in self._data:
            #     count += 1

            self._initialize_sets()
            print(count_records, "lines loaded")

    def load_default_data(self):
        """ Load sample data into self._data """
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

        self._initialize_sets()

    def get_labels(self, category: Categories):
        """ returns a list of the items in _labels[category] """
        if not self._data:
            raise DataSet.EmptyDatasetError("No data loaded")

        return list(self._labels[category.name])

    def get_active_labels(self, category: Categories):
        """ returns a list of the items in _active_labels[category] """
        if not self._data:
            raise DataSet.EmptyDatasetError("No data loaded")

        return list(self._active_labels[category.name])

    def toggle_active_label(self, category: Categories, descriptor: str):
        """ add or remove labels from _active_labels, allowing the user to filter out certain property
        types or locations """
        if not self._data:
            raise DataSet.EmptyDatasetError("No data loaded")

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
        """ display list data, min, max, average in rows and columns in an order """

        if not self._data:
            raise DataSet.EmptyDatasetError("No data loaded")

        # copying both self._labels sets into lists, which guarantees that the order of the objects will remain fixed.
        location_list = sorted(list(self._labels['LOCATION']))
        property_type_list = sorted(list(self._labels['PROPERTY_TYPE']))

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
                    # stat_val = None
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
                prop_type_single.append(f'$ {"{:.2f}".format(stat_val)}')

            all_prop_stats.append(prop_type_single)

        data = [prop_types] + list(zip(location_list, *all_prop_stats))  # read documentation
        # print(data)

        for i, d in enumerate(data):
            line = ''.join(str(x).ljust(22) for x in d)
            print(line)
            if i == 0:
                print('-' * len(line))

    def display_field_table(self, category: Categories):
        """ Display a table of the minimum, maximum and average rent
        for each item in that category """
        if not self._data:
            raise DataSet.EmptyDatasetError("No data loaded")

        # print("Rows:", category.name)
        # print("Active Labels: ", self._active_labels)
        active_labels_for_category = sorted(self._active_labels[category.name])
        # print(active_labels_for_category)

        header = ('', 'Minimum', 'Average', 'Maximum')
        line = ''.join(str(x).ljust(22) for x in header)
        print(line)

        for label in active_labels_for_category:
            # print("To find Statistics: ", label)
            field_table_stats = self.table_statistics(label)

            formatted_field_stats = (f'$ {"{:.2f}".format(item)}' for item in field_table_stats)

            d = (label, *formatted_field_stats)
            line = ''.join(str(x).ljust(22) for x in d)
            print(line)

    def table_statistics(self, label: str): # row_category: Categories,
        """ Calculate and return the filtered minimum, maximum and average rent for the
        properties in that category

        Keyword arguments:
            descriptor_one -- the label for the first category
            descriptor_two -- the label for the second category

        Returns:
            min, max and average values

        """

        # print("row_category: ", row_category)
        # print("Label: ", label)
        # print("Active Labels for Property_Type: ", self._active_labels[Categories.PROPERTY_TYPE.name])
        # print(self._data)
        filtered_list_for_category = [item for item in self._data if label in item]
        # print("filtered_list_for_category", filtered_list_for_category)
        prop_type_active_labels = self._active_labels[Categories.PROPERTY_TYPE.name]
        filtered_list_for_prop_type_active_labels = [item for item in filtered_list_for_category if item[1] in
                                                     prop_type_active_labels]
        # print("filtered_list_for_prop_type_active_labels", filtered_list_for_prop_type_active_labels)

        location_active_labels = self._active_labels[Categories.LOCATION.name]
        filtered_list_for_location_active_labels = [item for item in filtered_list_for_prop_type_active_labels if
                                                    item[0] in location_active_labels]
        # If there are no matching properties after applying the filter, raise our NoMatchingItems custom exception.

        if not filtered_list_for_location_active_labels:
            raise DataSet.NoMatchingItems

        value_list = [item[2] for item in filtered_list_for_location_active_labels]
        # print(value_list)

        return min(value_list), sum(value_list) / len(value_list), max(value_list)

    def _cross_table_statistics(self, descriptor_one: str,
                                descriptor_two: str):
        """ given a label from each category, calculate summary
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

        return min(value_list), sum(value_list) / len(value_list), max(value_list)


def manage_filters(dataset: DataSet, category: Categories):
    """ Print a menu-like list of all labels, Indicate which ones are currently active,
    Allow the user to change a label from active to inactive and vice-versa
    and Loop until the user has finished making their choices """

    # Print a menu-like list of all the labels for the given category
    category_labels = dataset.get_labels(category)
    # index = 1
    for index, label in enumerate(category_labels, start=1):
        is_label_active = label in dataset.get_active_labels(category)
        print(index, ":", label, "ACTIVE" if is_label_active else "INACTIVE")

    # Indicate which ones are currently active (i.e. the string
    # exists in dataset._active_labels[category]

    while True:
        try:
            selection = int(input("Please select an item to toggle or enter a blank line when you are finished. "))
            print("MY SELECTION:", selection)
            if selection >= 1:
                selected_descriptor = category_labels[selection - 1]
                dataset.toggle_active_label(category, selected_descriptor)
                for index, label in enumerate(category_labels, start=1):
                    is_label_active = label in dataset.get_active_labels(category)
                    print(index, ":", label, "ACTIVE" if is_label_active else "INACTIVE")
            else:
                exit(0)
        except IndexError:
            print("SELECTED NUMBER OUT OF RANGE")
        except Exception:
            break


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
    """ Present user with options to access the Airbnb dataset """

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
                dataset.display_cross_table(Stats.MIN)
            elif selection == 3:
                dataset.display_cross_table(Stats.MAX)
            elif selection == 4:
                dataset.display_field_table(Categories.LOCATION)
            elif selection == 5:
                dataset.display_field_table(Categories.PROPERTY_TYPE)
            elif selection == 6:
                manage_filters(dataset, category=Categories.LOCATION)
            elif selection == 7:
                manage_filters(dataset, category=Categories.PROPERTY_TYPE)
            elif selection == 8:
                # dataset.load_default_data()
                dataset.load_file()
            elif selection == 9:
                print("Goodbye!  Thank you for using the database")
                break
            else:
                print("Please enter a number between 1 and 9")

        except ValueError:
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
    # air_bnb.load_default_data()
    air_bnb.load_file()
    # air_bnb.display_cross_table(Stats.AVG)
    # air_bnb._initialize_sets()
    # air_bnb.get_labels(Categories.LOCATION)
    # air_bnb.get_active_labels(Categories.LOCATION)

    # print("Labels before Toggle", air_bnb.get_labels(Categories.LOCATION))
    # print("Active labels before Toggle", air_bnb.get_active_labels(Categories.LOCATION))
    # air_bnb.toggle_active_label(category=Categories.LOCATION, descriptor="Bronx")
    # print("Active labels after TOGGLE", air_bnb.get_active_labels(Categories.LOCATION))
    # print("Labels after Toggle", air_bnb.get_labels(Categories.LOCATION))
    manage_filters(air_bnb, category=Categories.LOCATION)
    stats_for_filer = air_bnb.table_statistics(Categories.LOCATION, "Manhattan")
    # print(stats_for_filer)
    # air_bnb.display_field_table(Categories.LOCATION)
    air_bnb.display_field_table(Categories.LOCATION)


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

    # my_set.load_default_data()
    my_set.load_file()

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
    main()
    # main_2()
    # unit_test()


"""
------Sample run# 1-------

Please enter your name: Mrudula
Hi Mrudula, welcome to Foothill's database project.
What is your home currency?AUD
Enter a header for the menu: 
Final Airbnb Database
Options for converting from AUD:
AUD       USD       EUR       CAD       GBP       CHF       NZD       JPY       
10.00     6.17      5.56      8.64      4.94      5.86      10.25     666.17    
20.00     12.35     11.11     17.28     9.88      11.73     20.49     1332.35   
30.00     18.52     16.67     25.93     14.81     17.59     30.74     1998.52   
40.00     24.69     22.22     34.57     19.75     23.46     40.99     2664.69   
50.00     30.86     27.78     43.21     24.69     29.32     51.23     3330.86   
60.00     37.04     33.33     51.85     29.63     35.19     61.48     3997.04   
70.00     43.21     38.89     60.49     34.57     41.05     71.73     4663.21   
80.00     49.38     44.44     69.14     39.51     46.91     81.98     5329.38   
90.00     55.56     50.00     77.78     44.44     52.78     92.22     5995.56   

Copyright 2021 Mrudula PB
Final Airbnb Database
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
Final Airbnb Database
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
48895 lines loaded
Final Airbnb Database
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
                      Entire home/apt       Private room          Shared room           
----------------------------------------------------------------------------------------
Bronx                 $ 127.51              $ 66.79               $ 59.80               
Brooklyn              $ 178.33              $ 76.50               $ 50.53               
Manhattan             $ 249.24              $ 116.78              $ 88.98               
Queens                $ 147.05              $ 71.76               $ 69.02               
Staten Island         $ 173.85              $ 62.29               $ 57.44               
Final Airbnb Database
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
                      Entire home/apt       Private room          Shared room           
----------------------------------------------------------------------------------------
Bronx                 $ 28.00               $ 0.00                $ 20.00               
Brooklyn              $ 0.00                $ 0.00                $ 0.00                
Manhattan             $ 0.00                $ 10.00               $ 10.00               
Queens                $ 10.00               $ 10.00               $ 11.00               
Staten Island         $ 48.00               $ 20.00               $ 13.00               
Final Airbnb Database
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
                      Entire home/apt       Private room          Shared room           
----------------------------------------------------------------------------------------
Bronx                 $ 1000.00             $ 2500.00             $ 800.00              
Brooklyn              $ 10000.00            $ 7500.00             $ 725.00              
Manhattan             $ 10000.00            $ 9999.00             $ 1000.00             
Queens                $ 2600.00             $ 10000.00            $ 1800.00             
Staten Island         $ 5000.00             $ 300.00              $ 150.00              
Final Airbnb Database
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
                      Minimum               Average               Maximum               
Bronx                 $ 0.00                $ 87.50               $ 2500.00             
Brooklyn              $ 0.00                $ 124.38              $ 10000.00            
Manhattan             $ 0.00                $ 196.88              $ 10000.00            
Queens                $ 10.00               $ 99.52               $ 10000.00            
Staten Island         $ 13.00               $ 114.81              $ 5000.00             
Final Airbnb Database
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
                      Minimum               Average               Maximum               
Entire home/apt       $ 0.00                $ 211.79              $ 10000.00            
Private room          $ 0.00                $ 89.78               $ 10000.00            
Shared room           $ 0.00                $ 70.13               $ 1800.00             
Final Airbnb Database
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
What is your choice? 6
1 : Queens ACTIVE
2 : Staten Island ACTIVE
3 : Bronx ACTIVE
4 : Manhattan ACTIVE
5 : Brooklyn ACTIVE
Please select an item to toggle or enter a blank line when you are finished. 3
MY SELECTION: 3
{'Queens', 'Staten Island', 'Bronx', 'Manhattan', 'Brooklyn'}
1 : Queens ACTIVE
2 : Staten Island ACTIVE
3 : Bronx INACTIVE
4 : Manhattan ACTIVE
5 : Brooklyn ACTIVE
Please select an item to toggle or enter a blank line when you are finished. 4
MY SELECTION: 4
{'Queens', 'Staten Island', 'Manhattan', 'Brooklyn'}
1 : Queens ACTIVE
2 : Staten Island ACTIVE
3 : Bronx INACTIVE
4 : Manhattan INACTIVE
5 : Brooklyn ACTIVE
Please select an item to toggle or enter a blank line when you are finished. 
Final Airbnb Database
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
                      Minimum               Average               Maximum               
Entire home/apt       $ 0.00                $ 172.72              $ 10000.00            
Private room          $ 0.00                $ 75.14               $ 10000.00            
Shared room           $ 0.00                $ 56.53               $ 1800.00             
Final Airbnb Database
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

Process finished with exit code 0

"""
