# f-strings are used for numerical values as well


def prefix():
    """Create a simple string introduction"""
    return "|->"


def main():
    animal_prices = {
        "frog": 2.37,
        "parrot": 4362,
        "mouse": 3.50,
        "crow": 0,
        "cat": 50.42,
        "finch": 67.1234,
        "turtle": 80.20
    }

    for item in animal_prices:  # 'in' will print keys
        print('A', item, 'is from the class', animal_prices[item])  # (OR)
        print(f'A {item} is from the class {animal_prices[item]}')

    print('Animal                   Price')
    for items in animal_prices:
        # print(f'{items:17}{animal_classes[items]}')  # 17 is leaving 17 spaces and for lineup

        # for right-justified, and we can embed functions in f-string i.e {prefix()} and use the return value
        print(f'{prefix()}{items:17}{animal_prices[items]:>10.2f}')  # decimal number which is float, 67.1234 is
        # rounded off


if __name__ == '__main__':
    main()
