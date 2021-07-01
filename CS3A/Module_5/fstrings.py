
def prefix():
    """Create a simple string introduction"""
    return "|-> "


def main():
    animal_classes = {
        "frog": "amphibian",
        "parrot": "bird",
        "mouse": "mammal",
        "crow": "bird",
        "cat": "mammal",
        "finch": "bird",
        "turtle": "reptile"
    }

    for item in animal_classes: # 'in' will print keys, item has key in it
        print('A', item, 'is from the class',animal_classes[item])  # (OR)
        print(f'A {item} is from the class {animal_classes[item]}')  # They are the way to combine literal strings
        # with the values from objects and possibly formatting along the way

    print('Animal                   Class')
    # no proper formatting
    for items in animal_classes:
        print(items, "            ", animal_classes[items])

    print("-------------------------")
    # proper formatting
    print('Animal                  Class')
    for items in animal_classes:
        # print(f'{items:25}{animal_classes[items]}') #25 is leaving 25 spaces and for lineup. IT's the width specifier

        # for right-justified, and we can embed functions in f-string i.e {prefix()} and use the return value
        print(f'{prefix()}{items:20}{animal_classes[items]:<10}') # :>10 means right-justified, :<10 is left-justified


if __name__ == '__main__':
    main()