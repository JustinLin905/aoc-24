import os
from collections import deque


class Solution:
    def __init__(self, file_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)

        self.graph = []

        with open(file_path) as f:
            for line in f:
                self.graph.append([int(char) for char in line.strip()])

        print(self.graph)

    def p1(self):
        def bfs(r, c):
            queue = deque([(r, c, 0)])
            nine_set = set()  # Don't double count ending spots

            while queue:
                r, c, val = queue.popleft()

                if val == 9:
                    nine_set.add((r, c))
                    continue

                # Search in 4 directions for next value
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < len(self.graph)
                        and 0 <= nc < len(self.graph[r])
                        and self.graph[nr][nc] == val + 1
                    ):
                        queue.append((nr, nc, val + 1))

            return len(nine_set)

        # Apply BFS
        res = 0

        for r in range(len(self.graph)):
            for c in range(len(self.graph[r])):
                if self.graph[r][c] == 0:
                    res += bfs(r, c)

        return res

    def p2(self):
        def bfs(r, c):
            queue = deque([(r, c, 0)])
            paths = 0

            while queue:
                r, c, val = queue.popleft()

                if val == 9:
                    paths += 1
                    continue

                # Search in 4 directions for next value
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < len(self.graph)
                        and 0 <= nc < len(self.graph[r])
                        and self.graph[nr][nc] == val + 1
                    ):
                        queue.append((nr, nc, val + 1))

            return paths

        # Apply BFS
        res = 0

        for r in range(len(self.graph)):
            for c in range(len(self.graph[r])):
                if self.graph[r][c] == 0:
                    res += bfs(r, c)

        return res
