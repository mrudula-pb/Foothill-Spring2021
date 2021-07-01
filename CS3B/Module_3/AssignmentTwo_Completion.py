import numpy as np
from enum import Enum
import collections


class DataMismatchError(Exception):
    """ Label and Feature example lists have different lengths"""


class NNData:
    class Order(Enum):
        RANDOM = 0
        SEQUENTIAL = 1

    class Set(Enum):
        TRAIN = 0
        TEST = 1

    @staticmethod
    def percentage_limiter(percentage: float):
        if percentage < 0:
            return 0
        elif percentage > 1:
            return 1
        elif 0 <= percentage <= 1:
            return percentage

    def __init__(self, features=None, labels=None, train_factor=.9):
        # self._train_indices = list()
        # self._test_indices = list()
        # self._test_indices = collections.deque()
        # self._test_pool = collections.deque()

        if features is None:
            features = []
        if labels is None:
            labels = []

        self._features = None
        self._labels = None

        self._train_factor = NNData.percentage_limiter(train_factor)

        self.load_data(features, labels)

    #     try:
    #         self.load_data(features, labels)
    #         self.split_set(self, new_train_factor=None)
    #     except (ValueError, DataMismatchError):
    #         pass
    #
    # def split_set(self, new_train_factor=None):
    #     if new_train_factor != None:
    #         self._train_factor = new_train_factor

    def load_data(self, features=None, labels=None):
        if features is None or labels is None:
            self._features = None
            self._labels = None
            return

        if len(features) != len(labels):
            raise DataMismatchError("Label and example lists have "
                                    "different lengths")

        try:
            self._features = np.array(features, dtype=float)
            self._labels = np.array(labels, dtype=float)
        except ValueError:
            self._features = None
            self._labels = None
            raise ValueError("Label and example lists must be homogeneous "
                             "and numeric lists of lists")


def load_XOR():
    XOR_X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    XOR_Y = [[0], [1], [1], [0]]
    data = NNData(XOR_X, XOR_Y, 1)