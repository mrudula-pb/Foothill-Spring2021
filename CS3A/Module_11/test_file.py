from csv import reader


class DataClass:
    filename = 'AB_NYC_2019.csv'

    def __init__(self):
        self._data = None

    def load_file(self):
        count = 0
        # open file in read mode
        with open(self.filename, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Get all rows of csv from csv_reader object as list of tuples
            list_of_tuples = list(map(tuple, csv_reader))
            # display all rows of csv
            print(list_of_tuples)
            for row in list_of_tuples:
                count += 1
            return count


data = DataClass()
# data.load_file()
count_lines = data.load_file()
print("count_lines: ", count_lines)
