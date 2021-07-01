data = (('Staten Island', 'Private room', 70), ('Brooklyn', 'Private room', 50), ('Bronx', 'Private room'
                                                                                                , 40),
                      ('Brooklyn', 'Entire home / apt', 150), ('Manhattan', 'Private room', 125),
                      ('Manhattan', 'Entire '
                                    'home / apt', 196), ('Brooklyn', 'Private room', 110),
                      ('Manhattan', 'Entire home / apt', 170), ('Manhattan'
                                                                '', 'Entire home / apt', 165),
                      ('Manhattan', 'Entire home / apt', 150), ('Manhattan', 'Entire home / apt',
                                                                100), ('Brooklyn', 'Private room', 65),
                      ('Queens', 'Entire home / apt', 350), ('Manhattan', 'Private room',
                                                             98), ('Brooklyn', 'Entire home / apt', 200),
                      ('Brooklyn', 'Entire home / apt', 150), ('Brooklyn', 'Private '
                                                                           'room', 99),
                      ('Brooklyn', 'Private room', 120))

list_of_data = [((row[0], row[1]), row[2]) for row in data]
print(list_of_data)

list_of_rents = []
for row in list_of_data:
    list_of_rents.append(row[1])

print()
print(list_of_rents)

length = len(list_of_rents)
minimum_rent = min(list_of_rents)
print("Minimum rent: ", minimum_rent)

average_rent = sum(list_of_rents)/length
print("Average rent: ", average_rent)

maximum_rent = max(list_of_rents)
print("Minimum rent: ", minimum_rent)
