
# See sample run below

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

    while True:
        animal = input("Please name an animal: ")

        if animal == "quit":
            break

        if animal not in animal_classes:  # This also works: if not animal in animal_classes:
            print("The animal not in animal classes")
            continue

        # if animal_classes[animal] == 'amphibian' or \
        #         animal_classes[animal] == 'bird' or \
        #         animal_classes[animal] == 'reptile':
        #     print("The animal lays eggs")

        # (OR)

        if not animal_classes[animal] == "mammal":  # This also works: if animal_classes[animal] != "mammal"
            print("The animal lays eggs")
        else:
            print('The animal does not lays eggs')

        # classification = input("Can you guess the classification for your animal? ")
        #
        # if animal in animal_classes \
        #         and classification in animal_classes[animal]:
        #     print("Correct")
        # else:
        #     print("Incorrect")


if __name__ == "__main__":
    main()


"""
----- Sample run# 1 ---

Please name an animal: mouse
Can you guess the classification for your animal? mammal
Correct  # Since both the cases are TRUE
Please name an animal: cat
Can you guess the classification for your animal? mammal
Correct  # Since both the cases are TRUE
Please name an animal: dog
Can you guess the classification for your animal? mammal
Incorrect  # Since both the cases are FALSE
Please name an animal: quit

---Sample run# 2 ----

Please name an animal: dog
The animal not in animal classes
Please name an animal: crow
The animal lays eggs
Please name an animal: cat
The animal does not lays eggs
Please name an animal: 

"""