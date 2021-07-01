
def main():
    fruits = ['Banana', 'Orange', 'Cherry']

    # Using iterators we are looping, behind the scene, an iterator is created and loops through fruits
    for fruit in fruits:
        print(fruit)

    print("------------------------")

    # loop using range
    for item in range(len(fruits)):
        print(fruits[item])

    print("------------------------")

    # Sets are not containers, No iterators since we have no sequence, No duplicates
    fruits_set = {'Banana', 'Orange', 'Cherry'}
    # Order changes for every run
    for fruit in fruits_set:
        print(fruit)

if __name__ == '__main__':
    main()