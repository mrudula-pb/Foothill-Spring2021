# functions within functions such as using print() within main().
# We can make our own functions such as animal() and call from main() function

def animal_noises():
    # call functions within function
    def cow_says():
        print("Moo")

    def cat_says():
        print('Meow')

    print("A cow says")
    cow_says()

    print("A cat says")
    cat_says()


def main():
    print('Hi THere!')
    cow_says() # it cannot find since it's defined in context of animal_noises()
    animal_noises().cow_says() # Question


if __name__ == "__main__":
    main()
