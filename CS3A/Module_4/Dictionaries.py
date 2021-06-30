
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
   print("Got key", k)

for akey in inventory.keys():
    print('Got key', akey, "which maps to value", inventory[akey])

ks_list = list(inventory.keys())
print(ks_list)

