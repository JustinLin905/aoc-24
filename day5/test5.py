import unittest
from day5 import Solution


class TestDayFive(unittest.TestCase):
    def test_5_main(self):
        s = Solution("5.txt")
        res = s.sum_valid_updates()

        self.assertEqual(res, 5248)

    def test_5_main_invalid_updates(self):
        s = Solution("5.txt")
        res = s.sum_invalid_updates()

        self.assertEqual(res, 4507)


if __name__ == "__main__":
    unittest.main()
