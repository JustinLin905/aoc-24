import unittest
from day6_1 import Solution


class TestDaySix(unittest.TestCase):
    def test_5_main(self):
        s = Solution("6.txt")
        res = s.patrol()

        self.assertEqual(res, 4752)


if __name__ == "__main__":
    unittest.main()
