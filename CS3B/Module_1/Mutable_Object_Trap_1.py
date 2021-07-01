def append_first_letter(string: str, list_to_append=None):
    if list_to_append is None:
        list_to_append = []

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
['d']
"""