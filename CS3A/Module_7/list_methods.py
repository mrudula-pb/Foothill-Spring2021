
my_fruit_bowl = ['banana', 'orange', 'avacado', 'orange', 'lemon', 'lemon', 'orange']
my_grocery_bag = ['grapefruit', 'persimmon', 'apple']

my_other_bowl = my_fruit_bowl.copy()

print(my_other_bowl)

my_fruit_bowl.extend(my_grocery_bag)
print(my_fruit_bowl)

my_fruit_bowl.sort()
print(my_fruit_bowl)

my_fruit_bowl.reverse()
print(my_fruit_bowl)

location = my_fruit_bowl.index("orange")
print(location) # returns the first occurence

# append at middle of list
my_fruit_bowl.insert(1, "papaya")
print(my_fruit_bowl)

value = my_fruit_bowl.count("orange")
print(value)

my_fruit_bowl.clear()
print(my_fruit_bowl)