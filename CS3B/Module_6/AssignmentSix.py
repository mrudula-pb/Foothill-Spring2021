
from enum import Enum, auto
from abc import ABC, abstractmethod
import math


class LayerType(Enum):
    INPUT = auto()
    HIDDEN = auto()
    OUTPUT = auto()


class MultiLinkNode:

    class Side(Enum):
        UPSTREAM = auto()
        DOWNSTREAM = auto()

    """self._reporting_nodes is a dictionary with two entries.  The keys will be the two elements of the Side enum.  The values will initially be set to zero.  We will use this as a binary encoding to keep track of which neighboring nodes have indicated that they have information available
    self._reference_value is also a dictionary with two entries.  The keys will again be the two elements of the Side enum.  The values will initially be set to zero, but will represent what the reporting nodes value should be as a binary encoding when all of the nodes have reported.
    self._neighbors is also a dictionary with two entries.  The keys will again be the two elements of the Side enum.  The values will initially be set to empty lists, but eventually will contain references to the neighboring nodes upstream and downstream."""
    def __init__(self):
        self._reporting_nodes = {self.Side.UPSTREAM: 0, self.Side.DOWNSTREAM: 0}
        self._reference_value = {self.Side.UPSTREAM: 0, self.Side.DOWNSTREAM: 0}
        self._neighbors = {self.Side.UPSTREAM: list(), self.Side.DOWNSTREAM: list()}

    def __str__(self):
        pass

    @abstractmethod
    def _process_new_neighbor(self, node, side):
        pass

    def reset_neighbors(self, nodes, side):
        self._neighbors = nodes[:]

    def reset_neighbors(self, nodes, side):
        pass


class Neurode(MultiLinkNode):

    def __init__(self, node_type, learning_rate=.05):
        pass

    @property
    def value(self):
        return self._value

    @property
    def node_type(self):
        return self._node_type

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, learning_rate: float):
        self._learning_rate = learning_rate

    def _process_new_neighbor(self, node, side):
        pass

    def _check_in(self, node, side):
        pass

    def get_weight(self, node):
        pass


class FFNeurode(Neurode):

    def __init__(self, my_type):
        super().__init__()

    @classmethod # changed from staticmethod to classmethod
    def _sigmoid(value):
        sigmoid_value = 1 / (1 + math.exp(-value))
        return sigmoid_value

    def _calculate_value(self):
        input_sum = 0
        for node, weight in self._weights.items():
            input_sum += node.value * weight
        self._value = self._sigmoid(input_sum)

    def _fire_downstream(self):
        for node in self._neighbors[MultiLinkNode.Side.DOWNSTREAM]:
            node.data_ready_upstream(self)

    def data_ready_upstream(self, from_node):
        if self._check_in(from_node, MultiLinkNode.Side.UPSTREAM):
            self._calculate_value()
            self._fire_downstream()

    def set_input(self, input_value: float):
        self._value = input_value
        for node in self._neighbors[MultiLinkNode.Side.DOWNSTREAM]:
            node.data_ready_upstream(self)


class BPNeurode(Neurode):
    def __init__(self, my_type):
        super().__init__()
        self._delta = 0

    @staticmethod
    def _sigmoid_derivative(value):
        sig = FFNeurode._sigmoid(value)
        return sig * (1 - sig)

    def _calculate_delta(self, expected_value=None):
        pass

    def data_ready_downstream(self, node):
        pass

    def set_expected(self, expected_value):
        pass

    def adjust_weights(self, node, adjustment):
        pass

    def _update_weights(self):
        pass

    def _fire_upstream(self):
        pass


class FFBPNeurode(FFNeurode, BPNeurode):
    pass






