
my_list = [12, 3, 2, -1]

my_list.append(15)

print(my_list)

print(my_list[1])
print(my_list[-1])
for item in my_list:
    print(item, end=' ')

print()
print("My list ID is: ", id(my_list), "before change")
my_list[2] = 'dog'
print("My list ID is: ", id(my_list), "after change")

my_list = [1,2,3]
print("My list ID is: ", id(my_list), "after change")


print()
for item in my_list:
    print(item, end=' ')

print()
if "dog" in my_list:
    print("There is dog")
else:
    print('No dog')

if "cat" in my_list:
    print("There is cat")
else:
    print('No cat')