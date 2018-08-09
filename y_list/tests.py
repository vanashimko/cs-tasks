from y_list.task import find_vanishing_point
from shared.node import Node
import unittest

class YListTests(unittest.TestCase):
    def test_equal_length(self):
        _4 = Node(4)
        first_start = Node(1, Node(2, Node(3, _4)))
        common = Node(5, Node(6, Node(7)))
        _4.next = common
        _minus4 = Node(-4)
        second_start = Node(-1, Node(-2, Node(-3, _minus4)))
        _minus4.next = common

        vanishing_point = find_vanishing_point(first_start, second_start)

        self.assertEqual(vanishing_point.value, 5)

    def test_first_is_longer(self):
        _4 = Node(4)
        first_start = Node(0, Node(1, Node(2, Node(3, _4))))
        common = Node(5, Node(6, Node(7)))
        _4.next = common
        _minus4 = Node(-4)
        second_start = Node(-1, Node(-2, Node(-3, _minus4)))
        _minus4.next = common

        vanishing_point = find_vanishing_point(first_start, second_start)

        self.assertEqual(vanishing_point.value, 5)

    def test_second_is_longer(self):
        _4 = Node(4)
        first_start = Node(1, Node(2, Node(3, _4)))
        common = Node(5, Node(6, Node(7)))
        _4.next = common
        _minus4 = Node(-4)
        second_start = Node(0, Node(-1, Node(-2, Node(-3, _minus4))))
        _minus4.next = common

        vanishing_point = find_vanishing_point(first_start, second_start)

        self.assertEqual(vanishing_point.value, 5)