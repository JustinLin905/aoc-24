import unittest
from day9 import Solution


class TestDayNine(unittest.TestCase):
    def test_nine_mini(self):
        s = Solution("9mini.txt")
        res = s.p1()
        self.assertEqual(res, 54)

    def test_nine_p1(self):
        s = Solution("9.txt")
        res = s.p1()
        self.assertEqual(res, 6241633730082)

    def test_nine_2mini(self):
        s = Solution("9mini.txt")
        res = s.p2()
        self.assertEqual(res, 54)

    def test_nine_p2(self):
        s = Solution("9.txt")
        res = s.p2()
        self.assertEqual(res, 6265268809555)

    def test_nine_p2_example(self):
        s = Solution("9example.txt")
        res = s.p2()
        self.assertEqual(res, 2858)


if __name__ == "__main__":
    unittest.main()
