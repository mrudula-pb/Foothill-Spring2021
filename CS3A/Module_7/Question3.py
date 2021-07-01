
# Starting with the list of the previous exercise, write Python statements to do the following:
# Append “apple” and 76 to the list.
# Insert the value “cat” at position 3.
# Insert the value 99 at the start of the list.
# Find the index of “hello”.
# Count the number of 76s in the list.
# Remove the first occurrence of 76 from the list.
# Remove True from the list using pop and index.

myList = []
myList.append(76)
myList.append(92.3)
myList.append("hello")
myList = myList + [True]
myList = myList + [4]
myList = myList + [76]
print(myList)

myList.append(['apple', 76])
myList[3:3] = ["cat"]
myList[0:0] = [99]
print(myList)
print(len(myList))
print(myList.index('hello'))
print(myList.count(76))
myList.remove(76)
print(len(myList))
myList.pop(myList.index(True))
print(myList)


