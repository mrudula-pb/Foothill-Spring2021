
my_list = [i * i for i in range(1, 100)]
print(my_list)
print(my_list[1])

print(my_list[0:10]) # 0 to 9

print(my_list[0: 10: 2])
print(my_list[10:0:-1])
print(my_list[90:])

print(id(my_list))
print(id(my_list[:])) # shallow copy of my_list , both id's are different

new_list = my_list[:]
new_list[0] = "safe!"

print(my_list)
print(new_list)

my_tuple = ('red', 'orange', 'yellow', 'green', 'nlue', 'indigo', 'violet')
print(my_tuple[3:6])

print(my_tuple[-1:-4:-1])

new_tuple = my_tuple[:]

print(id(my_tuple))
print(id(new_tuple))
