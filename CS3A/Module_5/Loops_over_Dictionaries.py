
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

    for item in animal_classes:  # 'in'
        print(item, "->", animal_classes[item])


if __name__ == '__main__':
    main()