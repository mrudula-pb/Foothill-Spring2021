location_list = ['Bronx', 'Manhatton', 'Brooklin']
prop_types = ['', '1bd', 'singlefam']

one_bed = [0.05, 0.1, 0.25]
single_fam = [2.0, 5.0, 3.0]


# [['', 'Entire home / apt', 'Private room'], ('Staten Island', 'N/A', 70.0), ('Bronx', 'N/A', 40.0), ('Manhattan', 156.2, 111.5), ('Brooklyn', 166.66666666666666, 88.8), ('Queens', 350.0, 'N/A')]

data = [prop_types] + list(zip(location_list, *[one_bed, single_fam]))
print(data)

for i, d in enumerate(data):
    line = '|'.join(str(x).ljust(22) for x in d)
    print(line)
    if i == 0:
        print('-' * len(line))