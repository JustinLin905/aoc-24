import unittest
import os
from day4_2 import Solution


class TestDFS(unittest.TestCase):
    def test_4_main_txt(self):
        s = Solution("4.txt")
        res = s.wordSearch()

        self.assertEqual(res, 1871)


if __name__ == "__main__":
    unittest.main()
