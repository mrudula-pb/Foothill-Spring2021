
my_list = [1, 2, 'string']
my_tuple = (1, 2, 'string')

print(my_list[0])
print(my_tuple[0])

my_list[2] = "Gadzooks"
print(my_list)

# my_tuple[2] = 'Gadzooks'
# print(my_tuple)

# have different IDs
my_other_list = list(my_list)
print(id(my_other_list))
print(id(my_list))

# have same IDs
print()
my_other_tuple = tuple(my_tuple)
print(id(my_other_tuple))
print(id(my_tuple))

print()
# have same IDs
my_other_list = my_list
print(id(my_other_list))
print(id(my_list))

runners = ['Spike', 'Sammy', 'Sally']
race_time = [56.2, 49.7, 45.3]


def winner(entrants: list, times: list):
    best_time = min(times)
    list_index = times.index(best_time)
    return entrants[list_index], times[list_index]


results = winner(runners, race_time)
print(results) # When we return multiple values, we get a tuple
print(type(results)) # When we return multiple values, we get a tuple

runner, time = winner(runners, race_time)
print(runner)
print(time)