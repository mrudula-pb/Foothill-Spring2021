import numpy as np
from enum import Enum
import collections
import random


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
        return percentage

    def __init__(self, features=None, labels=None, train_factor=.9):
        self._train_indices = list()
        self._test_indices = list()
        self._train_pool = collections.deque()
        self._test_pool = collections.deque()
        self.length_of_dataset = 0
        self.examples_of_trainset = 0
        self.dataset = 0

        if features is None:
            features = []
        if labels is None:
            labels = []

        self._features = None
        self._labels = None

        self._train_factor = NNData.percentage_limiter(train_factor)

        try:
            self.load_data(features, labels)
            self.split_set(self._train_factor)
        except (ValueError, DataMismatchError):
            pass

    def split_set(self, new_train_factor=None):
        if new_train_factor is not None:
            self._train_factor = NNData.percentage_limiter(new_train_factor)

        self.length_of_dataset = len(self._features)
        print('No of examples of features: ', self.length_of_dataset)

        self.examples_of_trainset = int(self.length_of_dataset * self._train_factor)
        print(self.examples_of_trainset)

        self._train_indices = random.sample(list(range(self.length_of_dataset)), k = self.examples_of_trainset)

        self._train_indices, self._test_indices = random.sample(list(range(self.length_of_dataset)), k =
        self.examples_of_trainset)

        self.dataset = list(range(self.length_of_dataset))

        random.shuffle(self.dataset)

        self._train_indices = self.dataset[:self.examples_of_trainset]
        self._test_indices = self.dataset[self.examples_of_trainset:]

        self._train_indices.sort()
        self._test_indices.sort()

    def prime_data(self, target_set=None, order=None):
        if target_set is NNData.Set.TRAIN:
            NNData.load_data(self._train_pool)
        elif target_set is NNData.Set.TEST:
            NNData.load_data(self._test_pool)
        elif target_set is None:
            NNData.load_data(self._train_pool, self._test_pool)

        self._train_pool = collections.deque(self._train_indices)
        self._test_pool = collections.deque(self._test_indices)

        if order == NNData.Order.RANDOM:
            random.shuffle(self._train_pool)
            random.shuffle(self._test_pool)
        if (order is None) or (order is NNData.Order.SEQUENTIAL):
            pass

    def get_one_item(self, target_set=None):
        if target_set is NNData.Set.TEST:
            if len(self._train_pool > 0):
                index_test = self._test_pool.popleft()
                feature_label_pair_TEST = (self._features[index_test], self._labels[index_test])
                return feature_label_pair_TEST
            else:
                return None
        elif target_set is NNData.Set.TRAIN or target_set is None:
            if len(self._train_pool > 0):
                index_train = self._train_pool.popleft()
                feature_label_pair_TRAIN = (self._features[index_train], self._labels[index_train])
                return feature_label_pair_TRAIN
            else:
                return None

    def number_of_samples(self, target_set=None):
        if target_set is NNData.Set.TEST:
            return len(self._test_pool)

        if target_set is NNData.Set.TRAIN:
            return len(self._train_pool)

        if target_set is None:
            return self._test_pool + self._train_pool

    def pool_is_empty(self, target_set=None):
        len_train_deque = len(self._train_pool)
        len_test_deque = len(self._test_pool)

        if target_set is NNData.Set.TEST:
            if len_test_deque == 0:
                return True
            else:
                return False

        if target_set is None or target_set is NNData.Set.TRAIN:
            if len_train_deque == 0:
                return True
            else:
                return False

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
    NNData(XOR_X, XOR_Y, 1)


def unit_test():
    errors = False
    try:
        # Create a valid small and large dataset to be used later
        x = [[i] for i in range(10)]
        y = x
        our_data_0 = NNData(x, y)
        x = [[i] for i in range(100)]
        y = x
        our_big_data = NNData(x, y, .5)

        # Try loading lists of different sizes
        y = [[1]]
        try:
            our_bad_data = NNData()
            our_bad_data.load_data(x, y)
            raise Exception
        except DataMismatchError:
            pass
        except:
            raise Exception

        # Create a dataset that can be used to make sure the
        # features and labels are not confused
        x = [[1.0], [2.0], [3.0], [4.0]]
        y = [[.1], [.2], [.3], [.4]]
        our_data_1 = NNData(x, y, .5)

    except Exception as e:
        print("There are errors that likely come from __init__ or a "
              "method called by __init__")
        import logging
        logging.getLogger().error(e, exc_info=True)
        print(e)
        errors = True

    # Test split_set to make sure the correct number of examples are in
    # each set, and that the indices do not overlap.
    try:
        our_data_0.split_set(.3)
        print(f"Train Indices:{our_data_0._train_indices}")
        print(f"Test Indices:{our_data_0._test_indices}")

        assert len(our_data_0._train_indices) == 3
        assert len(our_data_0._test_indices) == 7
        assert (list(set(our_data_0._train_indices +
                         our_data_0._test_indices))) == list(range(10))
    except:
        print("There are errors that likely come from split_set")
        errors = True

    # Make sure prime_data sets up the deques correctly, whether
    # sequential or random.
    try:
        our_data_0.prime_data(order=NNData.Order.SEQUENTIAL)
        assert len(our_data_0._train_pool) == 3
        assert len(our_data_0._test_pool) == 7
        assert our_data_0._train_indices == list(our_data_0._train_pool)
        assert our_data_0._test_indices == list(our_data_0._test_pool)
        our_big_data.prime_data(order=NNData.Order.RANDOM)
        assert our_big_data._train_indices != list(our_big_data._train_pool)
        assert our_big_data._test_indices != list(our_big_data._test_pool)
    except:
        print("There are errors that likely come from prime_data")
        errors = True

    # Make sure get_one_item is returning the correct values, and
    # that pool_is_empty functions correctly.
    try:
        our_data_1.prime_data(order=NNData.Order.SEQUENTIAL)
        my_x_list = []
        my_y_list = []
        while not our_data_1.pool_is_empty():
            example = our_data_1.get_one_item()
            my_x_list.append(list(example[0]))
            my_y_list.append(list(example[1]))
        assert len(my_x_list) == 2
        assert my_x_list != my_y_list
        my_matched_x_list = [i[0] * 10 for i in my_y_list]
        assert my_matched_x_list == my_x_list
        while not our_data_1.pool_is_empty(our_data_1.Set.TEST):
            example = our_data_1.get_one_item(our_data_1.Set.TEST)
            my_x_list.append(list(example[0]))
            my_y_list.append(list(example[1]))
        assert my_x_list != my_y_list
        my_matched_x_list = [i[0] * 10 for i in my_y_list]
        assert my_matched_x_list == my_x_list
        assert set(i[0] for i in my_x_list) == set(i[0] for i in x)
        assert set(i[0] for i in my_y_list) == set(i[0] for i in y)
    except:
        print("There are errors that may come from prime_data, but could "
              "be from another method")
        errors = True

    # Summary
    if errors:
        print("You have one or more errors.  Please fix them before "
              "submitting")
    else:
        print("No errors were identified by the unit test.")
        print("You should still double check that your code meets spec.")
        print("You should also check that PyCharm does not identify any "
              "PEP-8 issues.")

if __name__ == '__main__':
    unit_test()
