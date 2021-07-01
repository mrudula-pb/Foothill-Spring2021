#
# prices = { 'Pen' : 10, 'Pencil' : 5, 'Notebook' : 25}
# item = input('Get price of:')
#
# try:
#     x = prices[item]
#     print(x)
#     print(f'The price of {item} is x')
# except KeyError:
#     print(f'The price of {item} is not known')
# else:
#     print(f'There is no error in the statement')

ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
person = input('Get age for: ')

try:
    print(f'{person} is {ages[person]} years old.')
except KeyError:
    print(f"{person}'s age is unknown.")
