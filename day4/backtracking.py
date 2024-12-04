import os


class Solution:
    def init(self, file_name):
        self.script_dir = os.path.dirname(os.path.abspath(file))
        self.file_path = os.path.join(self.script_dir, file_name)
        self.TARGET_WORD = "XMAS"

        with open(self.file_path) as f:
            lines = [line.strip() for line in f]
            self.graph = [[char for char in line] for line in lines]
            self.m = len(self.graph)
            self.n = len(self.graph[0])

            print(self.graph)

    def wordSearch(self):
        def isValidTile(r, c):
            return 0 <= r < self.m and 0 <= c < self.n

        # DFS
        def dfs(r, c, idx):
            if idx == len(self.TARGET_WORD) - 1:
                return 1 if self.graph[r][c] == self.TARGET_WORD[idx] else 0

            found = 0

            # Mark visited
            prev = self.graph[r][c]
            self.graph[r][c] = "/"

            for dr, dc in [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
                (1, 1),
                (-1, 1),
                (1, -1),
                (-1, -1),
            ]:
                nr, nc = r + dr, c + dc

                if (
                    isValidTile(nr, nc)
                    and self.graph[nr][nc] == self.TARGET_WORD[idx + 1]
                ):
                    found += dfs(nr, nc, idx + 1)

            # Unmark
            self.graph[r][c] = prev
            return found

        res = 0

        for r in range(len(self.graph)):
            for c in range(len(self.graph[r])):
                # DFS
                if self.graph[r][c] == self.TARGET_WORD[0]:
                    res += dfs(r, c, 0)

        return res
