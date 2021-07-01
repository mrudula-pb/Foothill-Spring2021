import numpy as np

""" Program comparing Numpy array with List of Lists
"""
def main():
    a = np.array([1,2,3]) # 1-dimensional array
    print(a)
    my_numpy_array = np.array([[1,2,3], [4,5,6]]) # 2-dimensional array
    print(my_numpy_array)
    print(my_numpy_array[0,0])

    # dtype displays the data type of element within the Data Structure
    print(my_numpy_array.dtype) # int64

    # type displays the type of Data Structure
    print(type(my_numpy_array)) # <class 'numpy.ndarray'>

    # having 'string' as one of the items makes all items to strings
    my_numpy_array = np.array([[1, 2, 3], [4, 5, 'string']])
    print(my_numpy_array)
    print(my_numpy_array[0, 0])
    print(my_numpy_array.dtype)

    # having 'float' as one of the items makes all elements to float
    # my_numpy_array = np.array([[1, 2, 3], [4, 5, 1.0]])
    my_numpy_array = np.array([[1, 2, 3], [4, 5, 3]], dtype=float)

    # Shape gives what type of matrix it is, 2*3
    print("Shape: ", my_numpy_array.shape)

    # Shape for 1-dimensional array as tuple
    my_array = np.array([1,2,3])
    print('Shape: ', my_array.shape)

    print(my_numpy_array)
    print(my_numpy_array[0, 0])
    print(my_numpy_array.dtype)

    my_list = [[1,2,3], [4,5,6]]
    print(my_list)
    print(my_list[0][0])

    my_numpy_array = np.array([1, 2, 3]) # 1-dimensional array
    print(my_numpy_array.shape) # (3,), it's a tuple, Shape is a tuple

    # To make all zeroes
    my_numpy_array = np.zeros((2,3))
    print(my_numpy_array)

    # To make all ones
    my_numpy_array = np.ones((2, 3))
    print(my_numpy_array)

    # full to make all elements same, here we are using 8
    my_numpy_array = np.full((2, 3), 8)
    print(my_numpy_array)

    # arange numbers with step 2
    my_numpy_array = np.arange(2, 20, 2)
    print("Shape: ", my_numpy_array.shape)
    # displays sequence of numbers
    print(my_numpy_array)

    # arange 20 numbers
    my_numpy_array = np.arange(20)
    print("Shape: ", my_numpy_array.shape)
    # displays sequence of numbers
    print(my_numpy_array)

    my_numpy_array = np.arange(20)
    # arange 20 numbers in 4*5 array and it returns a new array
    new_numpy_array = my_numpy_array.reshape(4,5)
    print("Shape: ", new_numpy_array.shape)
    # displays sequence of numbers
    print(new_numpy_array)

    # cannot insert a different data type to an numpy array, you get error
    #new_numpy_array[3,4] = 'string'
    #print(new_numpy_array)

    # In array, the slice of array is the view of the array
    print(new_numpy_array[0:1, :])

    # In list, the slice of list is a new list
    x_list = my_list[0][:]
    print(x_list)
    #print(new_numpy_array)

    # have random numbers
    ran = np.random.random((3,4))
    print(ran)

    # random integer
    ran_int = np.random.randint(3,50, (3,4))
    print(ran_int)

    # Multiply an array
    a = np.array([[1,2,3], [4,5,6]])
    x = a * a

    # add 1 to each element in array
    a = a + 1

    # add array to existing one
    a = a + [1,2,3]  # [[2,4,6], [5,7,9]]

    # sum of all elements
    b = a.sum() # 21

    # sum of each column
    a.sum(axis=0)

    # sum of each row
    a.sum(axis=1) #[5 7 9]



if __name__ == '__main__':
    main()