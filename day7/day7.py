import os


class Solution:
    def __init__(self, file_name):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_dir, file_name)

        self.target_nums = []
        self.equations = []

        with open(self.file_path) as f:
            for line in f:
                colon_index = line.index(":")
                self.target_nums.append(int(line[:colon_index]))
                self.equations.append(line[colon_index + 1 :].strip().split())

        # print(self.target_nums)
        # print(self.equations)

    def p1(self):
        def backtrack(idx, cur):
            if idx == len(equation):
                if cur == target:
                    return True
                return False

            return backtrack(idx + 1, cur + int(equation[idx])) or backtrack(
                idx + 1, cur * int(equation[idx])
            )

        p1_sum = 0

        for i, target in enumerate(self.target_nums):
            equation = self.equations[i]

            p1_sum += target if backtrack(1, int(equation[0])) else 0

        return p1_sum

    def p2(self):
        def backtrack(idx, cur):
            if idx == len(equation):
                if cur == target:
                    return True
                return False

            return (
                backtrack(idx + 1, cur + int(equation[idx]))
                or backtrack(idx + 1, cur * int(equation[idx]))
                or backtrack(idx + 1, int(str(cur) + equation[idx]))
            )

        p1_sum = 0

        for i, target in enumerate(self.target_nums):
            equation = self.equations[i]

            p1_sum += target if backtrack(1, int(equation[0])) else 0

        return p1_sum
