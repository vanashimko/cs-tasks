from y_list.task import find_vanishing_point
from shared.node import Node
import unittest

class YListTests(unittest.TestCase):
    def setUp(self):
        self.common_part = Node(3, Node(4))

    def test_equal_length(self):
        """
            1   -1
             2 -2
              3
              4
        """
        _2 = Node(2)
        first_start = Node(1, _2)
        _2.next = self.common_part
        _minus2 = Node(-2)
        second_start = Node(-1, _minus2)
        _minus2.next = self.common_part

        vanishing_point = find_vanishing_point(first_start, second_start)

        self.assertEqual(vanishing_point.value, 3)

    def test_first_is_longer(self):
        """
           0 
            1   -1
             2 -2
              3
              4
        """
        _2 = Node(2)
        first_start = Node(0, Node(1, _2))
        _2.next = self.common_part
        _minus2 = Node(-2)
        second_start = Node(-1, _minus2)
        _minus2.next = self.common_part

        vanishing_point = find_vanishing_point(first_start, second_start)

        self.assertEqual(vanishing_point.value, 3)

    def test_second_is_longer(self):
        """
                  0
            1   -1
             2 -2
              3
              4
        """
        _2 = Node(2)
        first_start = Node(1, _2)
        _2.next = self.common_part
        _minus2 = Node(-2)
        second_start = Node(0, Node(-1, _minus2))
        _minus2.next = self.common_part

        vanishing_point = find_vanishing_point(first_start, second_start)

        self.assertEqual(vanishing_point.value, 3)