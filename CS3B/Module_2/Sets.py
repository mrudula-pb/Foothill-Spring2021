fruit_bowl_one = ["orange", "banana", "orange", "apple", 'apple', "avacado", "apple", "orange", "pear", "peach", "banana"]

fruit_bowl_two = ["peach", "grapefruit", "orange", "apple", 'apple', "kiwi", "apple", "orange", "grapefruit", "peach", "banana"]

fruit_bowl_one_unique = set(fruit_bowl_one) # here fruit_bowl_one is the iterable
print("Fruits in bowl One:", fruit_bowl_one_unique)
print('--------------------------------')

fruit_bowl_two_unique = set(fruit_bowl_two) # here fruit_bowl_two is the iterable
print("Fruits in bowl two:", fruit_bowl_two_unique)
print('--------------------------------')

fruit_bowl_combined = set.union(fruit_bowl_two_unique,fruit_bowl_one_unique)

# Another way for unique Union
# value = fruit_bowl_one_unique | fruit_bowl_two_unique
# print(value)
print("All fruits we have:", fruit_bowl_combined)
print('--------------------------------')

fruit_bowl_common = set.intersection(fruit_bowl_one_unique, fruit_bowl_two_unique) # or fruit_bowl_one_unique & fruit_bowl_two_unique
print("Common fruits in each bowl:", fruit_bowl_common)
print('--------------------------------')

for item in fruit_bowl_combined:
    print(item)
print('--------------------------------')

print(f"There are {len(fruit_bowl_combined)}  different kinds of fruit in the house")
print('--------------------------------')

if "banana" in fruit_bowl_combined:
    print('We have banana')
else:
    print('We have no banana')
print('--------------------------------')

#
new_bowl_dict = {"orange", "papaya", "lemon", 'lemon'} # this will ensure that lemon is listed only once
print(new_bowl_dict)
print('--------------------------------')

# We got error because we cannot put mutable datatype list in Set, we can put only immutable datatypes like strings, tuples or floats
# new_bowl_dict = {["orange", "papaya", "lemon", 'lemon']}
# print(new_bowl_dict)
# print('--------------------------------')

fruit_bowl_one_unique.add("banana")
print(fruit_bowl_one_unique)

# fruit_bowl_one_unique.remove("test")
# print(fruit_bowl_one_unique) # test doesn't exist, error occurs

fruit_bowl_one_unique.discard("papaya") # discard doesn't complain if the element exist or not
print(fruit_bowl_one_unique)

#create empty set
empty_set = set()
print(empty_set)






