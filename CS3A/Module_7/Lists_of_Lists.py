

my_pets =[['Dog', 'Spot', 7], ['Cat', 'Fifi', 12]]
for pet in my_pets:
    print(f"{pet[1]} is a {pet[0]} of age {pet[2]}")

my_list = [[4, 2, 5], [-3, 0, 7]]

for row in my_list:
    for item in row:
        print(f"Item is: {item}")

print(my_list)

print(my_list[0][1])

my_list[0][1] = 'cat'
print(my_list)
my_list[-1] = [2, 3]
print(my_list)

my_list[1] = "penguin"
print(my_list)