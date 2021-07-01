""" This program will help you order lovely breakfast"""


def spam(how_many=5, other_item='eggs') -> float: # if default value of formal parameters given then, variable type should not be
    # mentioned i.e def spam(how_many=10: int, other_item='eggs') is incorrect
    """ Place a breakfast order

    Args:
        how_many (int): how many orders of spam you would like
        other_item (str): something nice to go on the side
    Returns:
        float: total cost of the breakfast
    """
    if how_many == 0:
        print("We are not serving the breakfast")
        return 0
    print("May I please have my spam? ", end='')
    # '_' -> when we want to loop but don't want to use the variable within loop, we use '_''
    for _ in range(how_many):
        print('Spam ', end='')  # end is everything prints in same line
    print('and', other_item, end='')
    print(' please?')
    return how_many * 10 + 1.53


def simple_function():
    """ Do very little """
    print("I am in a function")


def main():
    print('Hi there!')
    print("Run the simple fucntion")
    ret_val = simple_function()
    print("Type of simple function's return: ")
    print(type(ret_val))
    print("Value of simple function's return: ")
    print(ret_val)  # None IS AN OBJECT. IT'S OFTEN ASSIGNED TO A VARIABLE OR SIGNAL THAT SOMETHING IS WRONG OR DATA IS NOT AVAILABLE
    # spam(5, 'eggs')
    # spam()  # you can also call like this when spam function have default arguments set i.e def spam(how_many=5, other_item='eggs')
    cost = spam(other_item="toast")  # another way when how_many is set to default i.e def spam(how_many=5, other_item='eggs'
    print("Total cost of your breakfast $", cost, sep='')  # sep is no space between $ and cost (default, you get a space)
    print()
    cost = spam(0, other_item="toast")
    print("Total cost of your breakfast $", cost, sep='')


if __name__ == '__main__':
    main()