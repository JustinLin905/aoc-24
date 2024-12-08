import unittest
from day6 import Solution


class TestDaySix(unittest.TestCase):
    def test_5_main(self):
        s = Solution("6.txt")
        res, _ = s.patrol()

        self.assertEqual(res, 4752)

    def test_5_patrol(self):
        s = Solution("6.txt")
        res = s.find_obstacles()

        self.assertEqual(res, 1719)


if __name__ == "__main__":
    unittest.main()
