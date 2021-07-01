
def append_first_letter(string: str, list_to_append=[]): # Default argument value is mutable, Python binding
    # ojects only in arguments. It doesn't have any binding in body of function. See Mutable_Object_Trap_1.py for
    # Solution
    list_to_append.append(string[0])
    return list_to_append


# provided list in arguments
my_list = ['a', 'b']
append_first_letter("cat", my_list)
print(my_list)


# not providing list in arguments
my_new_list = append_first_letter('dog')
print(my_new_list)

# Here 'd' already exits from list 'my_new_list'
my_newer_list = append_first_letter("elephant")
print(my_newer_list)

"""
['a', 'b', 'c']
['d']
['d', 'e']
"""
