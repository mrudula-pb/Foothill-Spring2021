# Write a function called average that takes a list of numbers as a
# parameter and returns the average of the numbers.

def average(numList):
    sum = 0
    for item in numList:
        sum += item
    return sum/len(numList)


numList = [1,2,3,4,5,6]
value = average(numList)
print(value)