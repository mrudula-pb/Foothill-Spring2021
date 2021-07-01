
def main():
    my_list = [[1,7,4],[3,2,-1]]
    print(my_list)
    print(my_list[1][2])
    my_list[1][2] = 'cat'
    print(my_list[1][2])
    print(my_list)

    my_list[1] = ['dog', 5] # ragged list i.e not each row has same length
    print(my_list)

    my_list[1] = 'penguin' # pointing to string
    print(my_list)

    my_list = [[1, 7, 4], [3, 2, -1]]
    length = len(my_list)
    print(length)
    for row in my_list:
        for item in row:
            print(f"Item is: {item}")

    new_list = [["Dog", "Spot", 7],['Cat', "Fifi", 120004]] # data type is different
    for item in new_list:
        print(f"{item[1]} is a {item[0]} who is {item[2]} years old")

if __name__ == '__main__':
    main()