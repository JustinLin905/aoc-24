import os
from math import floor, log10


class Solution:
    def __init__(self, file_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)

        with open(file_path) as f:
            self.initial_stones = [int(stone) for stone in f.readline().strip().split()]

        # print(self.initial_stones)

    def p1(self, blinks):
        # Top-down recursive with caching
        cache = {}

        def recur(num, blinks):
            if (num, blinks) in cache:
                return cache[(num, blinks)]
            if blinks == 0:
                return 1

            digits = floor(log10(num)) + 1 if num else 0
            if num == 0:
                res = recur(1, blinks - 1)
            elif digits % 2 == 0:
                divisor = 10 ** (digits // 2)
                left = num // divisor
                right = num % divisor
                res = recur(left, blinks - 1) + recur(right, blinks - 1)
            else:
                res = recur(num * 2024, blinks - 1)

            cache[(num, blinks)] = res
            return res

        # Map and calculate result
        return sum(map(lambda stone: recur(stone, blinks), self.initial_stones))
