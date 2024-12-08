import unittest
import os
from day4_1 import Solution


class TestDFS(unittest.TestCase):
    def test_4_test_txt(self):
        s = Solution("4-test.txt")
        res = s.wordSearch()

        self.assertEqual(res, 4)

    def test_4_test_two_txt(self):
        s = Solution("4-test2.txt")
        res = s.wordSearch()

        self.assertEqual(res, 18)

    def test_4_main_txt(self):
        s = Solution("4.txt")
        res = s.wordSearch()

        self.assertEqual(res, 2414)


# Don't forget this, else no program entry point
if __name__ == "__main__":
    unittest.main()
