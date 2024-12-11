import unittest
from day11 import Solution


class TestDayEleven(unittest.TestCase):
    def test_eleven_example(self):
        s = Solution("11example.txt")
        res = s.p1(6)
        self.assertEqual(res, 22)

        res = s.p1(25)
        self.assertEqual(res, 55312)

    def test_eleven_p1(self):
        s = Solution("11.txt")
        res = s.p1(25)
        self.assertEqual(res, 203457)

    def test_eleven_p1(self):
        s = Solution("11.txt")
        res = s.p1(75)
        self.assertEqual(res, 241394363462435)


if __name__ == "__main__":
    unittest.main()
