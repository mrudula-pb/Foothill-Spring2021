
a = ['dog', 'apple', 'cat']
a_indirect = [1, 2, 0]

for index in a_indirect:
    print(a[index])

# both these lists are synchronized. Fred is 15 yrs old, Betty is 30 yrs old, Sam is 25 yrs old.
people = ['fred', 'betty', 'sam']
ages = [15, 30, 25]


# function to print people and their ages
def print_ages(order = None):
    if order == None:
        order = [0, 1, 2]
    for item in order:
        print(f"{people[item]} is {ages[item]}")


people_sort_position = [1, 0, 2]
ages_numerical_sort = [0, 2, 1]
only_males = [0, 2]

if __name__ == "__main__":
    print("print people and their ages")
    print_ages()

    print("print people in alphabetical order")
    print_ages(people_sort_position) # for displaying in alphabetical order

    print("print ages in numerical order")
    print_ages(ages_numerical_sort) # for displaying in numerical sort

    print('print only males')
    print_ages(only_males)

