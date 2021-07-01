
# int, float, string are immutable

my_int = 6
print("ID: ", id(my_int))  # ID: 10914656, printing the id of object that my_int refers to
my_int = 7  # created a brand new object and reassigned the name my_int to brand new object
print("ID: ", id(my_int))  # ID: 10914688, printing the id of object that my_int refers to

# dictionary is mutable
my_dictionary = {1: "one", 2: "two"}  # WE ARE CREATING A NEW DICTIONARY OBJECT AND BINDING my_dictionary TO THE OBJECT
print("ID: ", id(my_dictionary))
my_dictionary[1] = "won"  # modified the value of existing key
print("ID: ", id(my_dictionary))
my_dictionary = {1: "WON", 2: "two"}  # WE ARE CREATING A NEW DICTIONARY OBJECT AND BINDING my_dictionary TO THE OBJECT
print("ID: ", id(my_dictionary))

your_dictionary = my_dictionary
print("ID: ", id(your_dictionary))

your_dictionary[1] = "one"
print(your_dictionary[1])
print("ID: ", id(my_dictionary))

