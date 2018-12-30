import unittest
from .task import find_symmetry_point

_symmetry_ = 0

class SymmetryPointTestCase(unittest.TestCase):
    def test_has_symmetry_point(self):
        actual = find_symmetry_point([1, 2, 2, _symmetry_, 5])
        self.assertEqual(actual, 3)

    def test_has_symmetry_point_middle(self):
        actual = find_symmetry_point([1, 2, _symmetry_, 0, 3])
        self.assertEqual(actual, 2)

    def test_has_symmetry_point_start(self):
        actual = find_symmetry_point([_symmetry_, 1, -1, 3, -3])
        self.assertEqual(actual, 0)

    def test_has_symmetry_point_end(self):
        actual = find_symmetry_point([1, -1, 3, -3, _symmetry_])
        self.assertEqual(actual, 4)

    def test_no_symmetry_point(self):
        actual = find_symmetry_point([1, 2, 3])
        self.assertIsNone(actual)

    def test_all_points_symmetry(self):
        actual = find_symmetry_point([0, 0, 0])
        self.assertEqual(actual, 0)
