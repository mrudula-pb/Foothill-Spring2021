# Create a list called myList with the following six items: 76, 92.3, “hello”, True, 4, 76. Begin with the empty list
# shown below, and add 6 statements to add each item, one per item. The first three statements should use the append
# method to append the item to the list, and the last three statements should use concatenation.

myList = []

myList.append(76)
myList.append(92.3)
myList.append("hello")
myList = myList + [True]
myList = myList + [4]
myList = myList + [76]
print(myList)