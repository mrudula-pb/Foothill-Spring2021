import timeit

my_list = [3, 4, 5]

my_square = []
for i in range(1, 101):
    my_square.append(i * i)
# print(my_square)

# Using list comprehension
my_squares_lc = [i * i for i in range(1, 101)]
# print(my_squares_lc)

# list only 'c' words
my_words = ['cat', 'car', 'apple', 'boat', 'cavern', 'elephant']

my_c_words = [word for word in my_words if word[0] == "c"]
print(my_c_words)

# get only items/inventory
my_prices = [["book", 1.53], ["dish", .12], ["picture frame", 2.43], ["lemonade", .25]]

my_inventory = [row[0] for row in my_prices]
print(my_inventory)

# get only cheap items/inventory
my_cheap_inventory = [row[0] for row in my_prices if row[1] < 1]
print(my_cheap_inventory)

# best/min times of the race in each list
race_times = [[43, 35, 36], [32, 50, 63], [43, 30, 30], [80, 36, 40]]
best_times = [(max(item), min(item)) for item in race_times]
print(best_times)


# List comprehensions are faster than loops
def list_with_loops():
    my_list = []
    for a in range(1, 1001):
        my_list.append(a * a)


def list_with_comprehension():
    my_list = [a * a for a in range(1, 1001)]


print(timeit.timeit(list_with_loops, number=1000)) # run 1000 times, not calling the function but passing as
# object parameter
print(timeit.timeit(list_with_comprehension, number=1000)) # run 1000 times, not calling the function but passing as
# object parameter
