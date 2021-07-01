
import copy
import sys

string1 = "meow"
string2 = "woof"
string3 = "chirp"

deeplist = [string1, string2, string3]
toplist = [deeplist, 'moo']

# references
toplist1 = toplist
print(sys.getsizeof(toplist1))

# shallow copy/copy
toplist2 = toplist[:]
print(sys.getsizeof(toplist2))

# deep copy
toplist3 = copy.deepcopy(toplist)
print(sys.getsizeof(toplist3))

# change string2
toplist[1] = 'baa'

# change string1
toplist[0][0] = 'baa'

print(f"Toplist One: {toplist1[1]}")
print(f"Toplist Two: {toplist2[1]}")
print(f"Toplist Three: {toplist3[1]}")

print("-------------------------------")

print(f"Toplist One: {toplist1[0][0]}")
print(f"Toplist Two: {toplist2[0][0]}") # here we copied only the shallow level(1st level) and it still refers to deep
# list object. subsequent levels it refers to those levels

print(f"Toplist Three: {toplist3[0][0]}")