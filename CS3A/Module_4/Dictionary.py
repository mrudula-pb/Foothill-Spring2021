
def main():
    animal_classes = {
        "frog": "amphibian",
        'parrot': "bird",
        "mouse": 'mammal',
        "crow": "bird",
        "cat": "mammal",
        "finch": "bird",
        "turtle": 'reptile'
    }
    print(animal_classes["frog"])

    print(animal_classes)
    # while True:
    #     animal = input("Please name an animal: ")
    #     if animal == "quit":
    #         break
    #     try:
    #         print("A", animal, "is a", animal_classes[animal])
    #     except KeyError:
    #         print("Key doesn't exist")
    #     print()

    while True:
        animal = input("Please name an animal: ")
        if animal == "quit":
            break
        if animal in animal_classes:
            print("A", animal, "is a", animal_classes[animal])
        else:
            print("Key doesn't exist")
        print()


    # print("Before assignment: ")
    # try:
    #     print(animal_classes["dog"])  # KeyError, doesn't exist in dict
    # except KeyError:
    #     print("Key doesn't exist")
    # print()
    # print("After assignment: ")
    # animal_classes['dog'] = "mammal"
    # try:
    #     print(animal_classes["dog"])  # KeyError, doesn't exist in dict
    # except KeyError:
    #     print("Key doesn't exist")
    # else:
    #     print("Key exist")
    # print()
    #
    # print("Delete key")
    # del animal_classes['dog']
    # print()
    #
    # print("After deleting: ")
    # try:
    #     print(animal_classes["dog"])  # KeyError, doesn't exist in dict
    # except KeyError:
    #     print("Key doesn't exist")


if __name__ == "__main__":
    main()