import os


class Solution:
    def __init__(self, file_name):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_dir, file_name)
        self.TARGET_WORD = "MAS"

        with open(self.file_path) as f:
            lines = [line.strip() for line in f]
            self.graph = [[char for char in line] for line in lines]
            self.m = len(self.graph)
            self.n = len(self.graph[0])

    def wordSearch(self):
        def findMas(r, c, direction):
            if direction == -1:
                r += 2

            for word in ["MAS", "SAM"]:
                found = True
                cur_r = r
                cur_c = c

                for i in range(len(word)):
                    if self.graph[cur_r][cur_c] != word[i]:
                        found = False

                    cur_r += direction
                    cur_c += 1

                if found:
                    return True

            return False

        # DFS
        def findXmas(r, c):
            return 1 if findMas(r, c, 1) and findMas(r, c, -1) else 0

        res = 0

        for r in range(len(self.graph) - 2):
            for c in range(len(self.graph[r]) - 2):
                res += findXmas(r, c)

        return res
