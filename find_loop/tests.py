import unittest
from .task import Node, find_loop

class FindLoopTests(unittest.TestCase):
    def test_has_loop(self):
        """
                 5 <- 4
                 V    ^   
            1 -> 2 -> 3
        """
        start = _1 = Node(1)
        _1.next = _2 = Node(2)
        _2.next = _3 = Node(3)
        _3.next = _4 = Node(4)
        _4.next = _5 = Node(5)
        _5.next = _2

        loop = find_loop(start)

        self.assertIsNotNone(loop)
        self.assertEqual(loop.length, 4)
        self.assertEqual(loop.start_element.value, 2)

    def test_no_loop(self):
        start = Node(1, Node(2, Node(3, Node(4, Node(5)))))

        loop = find_loop(start)

        self.assertEqual(loop, None)

        