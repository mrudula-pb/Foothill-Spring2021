
def main():
    animal_classes ={
    "frog" : "amphibian",
    'parrot' : "bird",
    "mouse" :"mammal",
    "crow" : "bird",
    "cat" : "mammal",
    "finch" : "bird",
    "turtle" : "reptile"
    }

    # display key value pairs of animal_classes
    print(animal_classes)

    # display value of frog
    print(animal_classes["frog"])

    # add key value pair to dictionary
    animal_classes["dog"] = "amphibian"
    print(animal_classes)

    # key not in dictionary
    try:
        print(animal_classes['myself'])
    except KeyError:
        print("Sorry, key not found")

    # re-assign dog value
    animal_classes["dog"] = "mammal"
    print(animal_classes)

    # delete dog key value pair
    del animal_classes['dog']
    print(animal_classes)
    try:
        print(animal_classes['dog'])
    except KeyError:
        print("Sorry, key not found")

    print(len(animal_classes))

    while True:
        animal = input("Enter the name of animal: ")
        if animal == 'quit':
            break
        if animal in animal_classes:
            print("A", animal, "is a", animal_classes[animal])
        else:
            print("Sorry, key not found")




if __name__ == '__main__':
    main()