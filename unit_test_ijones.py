import unittest
from ijones import main


class IjonesTest(unittest.TestCase):
    """Tests for ijones.py"""

    def test_ijones1_out(self):
        """A test that compares the result of the algorithm with a given value of 5"""
        current = main('test_ijones/ijones1.in', 'test_ijones/ijones1.out')

        self.assertEqual(current, 5)

    def test_ijones2_out(self):
        """A test that compares the result of the algorithm with a given value of 2"""
        current = main('test_ijones/ijones2.in', 'test_ijones/ijones2.out')

        self.assertEqual(current, 2)

    def test_ijones3_out(self):
        """A test that compares the result of the algorithm with a given value of 201684"""
        current = main('test_ijones/ijones3.in', 'test_ijones/ijones3.out')

        self.assertEqual(current, 201684)


if __name__ == '__name__':
    unittest.main()
