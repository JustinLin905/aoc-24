import os


class Solution:
    def __init__(self, file_name):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_dir, file_name)
        self.graph = []
        self.start = (-1, -1)
        self.visited = set()

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
        r, c = self.start
        dr, dc = -1, 0

        while 0 <= r < len(self.graph) and 0 <= c < len(self.graph[r]):
            nr, nc = r + dr, c + dc
            # print(f"Checking {nr}, {nc}")

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
                # print(f"Change dir to {dr}, {dc}. Checking {nr}, {nc}")

            # Mark cur as visited and Move space
            self.visited.add((r, c))
            r, c = nr, nc
            # print(f"MARKED as visited {r}, {c}")

        # Count visited tiles
        return len(self.visited)
