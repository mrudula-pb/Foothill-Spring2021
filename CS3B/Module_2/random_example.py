
import random

# generate random number
print(random.random())
print('--------------------------------')

for item in range(10): # item is 0 to 9
    print(random.random())
print('--------------------------------')

# We can tell random from which number to start
random.seed(1) # when no argument, it uses current system time to tell where to start
for item in range(10):
    print(random.random())
print('--------------------------------')

random.seed(1)
for item in range(10):
    print(random.randint(0, 10)) # 0 not included and 10 included
print('--------------------------------')

# list comprehension
base_list = [random.randint(0, 10) for item in range(50)]
print(base_list)
print('--------------------------------')

for _ in range(3):
    print(random.choice(base_list)) # choice takes a list and here it picks 3 items from base_list
print('--------------------------------')

my_choices = random.choices(base_list, k=10) # we can get same item one or more times, replacement [0, 6, 0, 8, 0, 2, 0, 0, 6, 10]

print(my_choices)
print('--------------------------------')

my_choices = random.sample(base_list, k=10) # without replacement, use sample()
print(my_choices)
print('--------------------------------')

# my_choices = random.sample(base_list, k=60) # base-list doesn't have 60 items. error occurs
# print(my_choices)
print('--------------------------------')

#shuffle the list, base_list is modified and printed. base_list on line 24 is shuffled
random.shuffle(base_list)
print(base_list)
print('--------------------------------')
