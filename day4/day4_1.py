import os


class Solution:
    def __init__(self, file_name):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_dir, file_name)
        self.TARGET_WORD = "XMAS"

        with open(self.file_path) as f:
            lines = [line.strip() for line in f]
            self.graph = [[char for char in line] for line in lines]
            self.m = len(self.graph)
            self.n = len(self.graph[0])
            self.directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
                (1, 1),
                (-1, 1),
                (1, -1),
                (-1, -1),
            ]

    def wordSearch(self):
        def isValidTile(r, c):
            return 0 <= r < self.m and 0 <= c < self.n

        # DFS
        def dfs(r, c, idx, direction):
            if idx == 4:
                return 1

            # Check if current position is valid and matches the current letter
            if not isValidTile(r, c) or self.graph[r][c] != self.TARGET_WORD[idx]:
                return 0

            # Move to next position
            nr = r + direction[0]
            nc = c + direction[1]

            # Continue searching in the same direction
            return dfs(nr, nc, idx + 1, direction)

        res = 0

        for r in range(len(self.graph)):
            for c in range(len(self.graph[r])):
                for direction in self.directions:
                    res += dfs(r, c, 0, direction)

        return res
