import unittest
from day8 import Solution


class TestDayEight(unittest.TestCase):
    def test_8_1(self):
        s = Solution("8.txt")
        s.map_nodes()
        res = s.plot_antinodes()

        self.assertEqual(res, 222)

    def test_8_2(self):
        s = Solution("8.txt")
        s.map_nodes()
        res = s.plot_antinodes_p2()

        self.assertEqual(res, 884)


if __name__ == "__main__":
    unittest.main()
