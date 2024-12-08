import os


class Solution:
    def __init__(self, file_name):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_dir, file_name)
        self.graph = []
        self.start = (-1, -1)

        with open(self.file_path) as f:
            lines = [line.strip() for line in f]
            for r in range(len(lines)):
                line = lines[r]
                cur_row = []
                for c in range(len(line)):
                    cur_char = line[c]
                    cur_row.append(cur_char)

                    if cur_char == "^":
                        self.start = (r, c)

                self.graph.append(cur_row)

            # print(self.graph)
            # print(self.start)

    def patrol(self):
        """
        For efficiency in P2: preprocess and create a jump table, which will tell you where the next obstacle is in each position and direction combination
        """
        r, c = self.start
        dr, dc = -1, 0
        visited = set()
        cache = set()

        while 0 <= r < len(self.graph) and 0 <= c < len(self.graph[r]):
            # Check for loop
            if (r, c, dr, dc) in cache:
                return -1
            cache.add((r, c, dr, dc))

            nr, nc = r + dr, c + dc

            # Next space is an obstacle
            # (-1, 0), (0, 1), (1, 0), (0, -1)
            while (
                0 <= nr < len(self.graph)
                and 0 <= nc < len(self.graph[r])
                and self.graph[nr][nc] == "#"
            ):
                # Change dir
                temp = dc
                dc = dr * -1
                dr = temp

                nr, nc = r + dr, c + dc

            # Mark cur as visited and Move space
            visited.add((r, c))
            r, c = nr, nc

        # Count visited tiles
        return len(visited), visited

    def find_obstacles(self):
        res = 0

        # First pass: get all tiles that are visited normally. Placing an obstacle at a tile we don't visit normally won't have any effect
        _, visited = self.patrol()

        # Can't place an obstacle on start
        visited.remove((self.start[0], self.start[1]))

        for i, j in visited:
            print(f"Trying to place obstacle at: {i}, {j}")
            self.graph[i][j] = "#"
            if self.patrol() == -1:
                res += 1
                print(f"Infinite loop with obstacle at: {i}, {j}")
            self.graph[i][j] = "."

        return res
