"""
Build a class called NNData with methods that will help us efficiently
manage our training and testing data.
"""
import numpy as np
from enum import Enum


class NNData:

    def __init__(self, features=None, labels=None, train_factor: float = 0.9):
        if features is None:
            features = []
        if labels is None:
            labels = []

        self._labels = None  # to avoid warnings
        self._features = None

        self._train_factor = NNData.percentage_limiter(train_factor)

        self.load_data(features, labels)

    class Order(Enum):  # Enums are constants
        """Define if training data is presented in the same order to the NN each time or random order"""
        RANDOM = 1
        SEQUENTIAL = 2

    class Set(Enum):
        """Identifies whether we are requesting training set ot testing set data"""
        TRAIN = 1
        TEST = 2

    # This is function for safeguard of how much data I am sending (only between 0 and 1)
    @staticmethod
    def percentage_limiter(percentage: float):  # train_factor is percentage of data which I want to use for training
        # data versus testing data
        # here it's 90% training data and 10% testing data
        if percentage < 0:
            print("percentage ", percentage, "should be between 0 and 1, 1 included")
            return 0
        elif percentage > 1:
            print("percentage ", percentage, "should be between 0 and 1, 1 included")
            return 1
        return percentage

    def load_data(self, features=None, labels=None):
        features_len = len(features)
        labels_len = len(labels)

        if features_len != labels_len:
            self._features = None
            self._labels = None
            print("self._features is: ", self._features)
            print("self._labels is: ", self._labels)
            raise DataMismatchError("Label and feature example lists have different lengths")

        # if features is None:
        #     self._features = None
        #     self._labels = None
        #     return

        try:
            self._features = np.array(features, dtype=float)  # To generalize the data we are making dtype float
            self._labels = np.array(labels, dtype=float)
        except ValueError:
            self._features = None
            self._labels = None
            raise ValueError("Label and Feature example lists must be homogeneous "
                             "and numeric lists of lists")


def load_XOR():
    list_of_features = [[0, 1], [0, 1], [1, 0], [1, 1]]
    list_of_labels = [[0], [1], [1], [0]]

    NNData(list_of_features, list_of_labels, train_factor=1)


class DataMismatchError(Exception):
    """Label and Feature example lists have different lengths"""


def unit_test():
    # NNData.load_data() raises a DataMismatchError if features and labels have different lengths when calling .
    # Verify that self._features and self._labels are set to None.
    list_of_features = [[0, 1], [1, 0], [1, 0]]  # passing 3 values instead of 4
    list_of_labels = [[0], [1], [1], [0]]

    # NNData(list_of_features, list_of_labels, train_factor=1)

    # NNData.load_data() raises a ValueError if features or labels contain non-float values (like strings) when
    # calling load_data(). Verify that self._features and self._labels are set to None.

    list_of_features = [["str", "str1"], [1, 0], [1, 0], [1, 1]]  # passing 3 values instead of 4
    list_of_labels = [[0], [1], [1], [0]]
    # NNData(list_of_features, list_of_labels, train_factor=1)

    # Verify that if invalid data values  are passed to the constructor (such as lists of different
    # lengths, or lists that cannot be made into a homogeneous array of floats), self._features and self._labels
    # are set to None.
    # IMPLEMENTED

    # Verify that NNData limits the training factor to zero if a negative number is passed
    NNData.percentage_limiter(-1)

    # Verify that NNData limits the training factor to one if a number greater than one is passed
    NNData.percentage_limiter(2)


if __name__ == "__main__":
    unit_test()


"""
--- Sample run# 1 ---
# NNData.load_data() raises a DataMismatchError if features and labels have different lengths when calling .
# Verify that self._features and self._labels are set to None.

File "/home/mdot/MyAssignments/CS3B/Module_1/AssignmentOne.py", line 58, in load_data
 raise DataMismatchError("Label and feature example lists have "
__main__.DataMismatchError: Label and feature example lists have different lengths

--- Sample run# 2 ---
# NNData(list_of_features, list_of_labels, train_factor=1)
# NNData.load_data() raises a ValueError if features or labels contain non-float values (like strings) when
# calling load_data(). Verify that self._features and self._labels are set to None.

Traceback (most recent call last):
  File "/home/mdot/MyAssignments/CS3B/Module_1/AssignmentOne.py", line 70, in load_data
    self._features = np.array(features, dtype=float) #To generalize the data we are making dtype float
ValueError: could not convert string to float: 'str'

During handling of the above exception, another exception occurred:

--- Sample run# 3 ---

"""
