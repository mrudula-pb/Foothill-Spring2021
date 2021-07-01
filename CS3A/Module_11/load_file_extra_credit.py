from csv import reader


def load_file():
    file_name = 'AB_NYC_2019.csv'
    count = 0
    with open(file_name, 'r') as read_obj:
        csv_reader = reader(read_obj, skipinitialspace=True)
        next(csv_reader)
        row_data = [[row[1], row[2], int(row[3])] for row in csv_reader]
        # print("row_data: ", row_data)

        data = list(map(tuple, row_data))
        # print("self._data: ", data)

        for row in data:
            count += 1
        return count


def main():
    line_count = load_file()
    print(line_count)


if __name__ == '__main__':
    main()


""" 

----Sample run# 1 -----

/home/mdot/MyAssignments/venv/bin/python /snap/pycharm-community/240/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py --target unit_test.TestCC.test_lines_of_airbnb_data
Testing started at 11:17 PM ...
Launching unittests with arguments python -m unittest unit_test.TestCC.test_lines_of_airbnb_data in /home/mdot/MyAssignments/CS3A/Module_11


Process finished with exit code 0


Ran 1 test in 0.212s

OK

"""