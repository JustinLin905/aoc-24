import unittest
from day10 import Solution


class TestDayTen(unittest.TestCase):
    def test_ten_p1(self):
        s = Solution("10.txt")
        res = s.p1()

        self.assertEqual(res, 557)

    def test_ten_p2(self):
        s = Solution("10.txt")
        res = s.p2()

        self.assertEqual(res, 1062)


if __name__ == "__main__":
    unittest.main()
