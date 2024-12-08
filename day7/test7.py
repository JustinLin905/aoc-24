import unittest
from day7 import Solution


class TestDaySeven(unittest.TestCase):
    def test_7_main(self):
        s = Solution("7.txt")
        res = s.p1()

        self.assertEqual(res, 20665830408335)

    def test_7_main(self):
        s = Solution("7.txt")
        res = s.p2()

        self.assertEqual(res, 0)


if __name__ == "__main__":
    unittest.main()
