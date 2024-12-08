import os
from collections import defaultdict


class Solution:
    def __init__(self, file_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)

        self.graph = []
        self.nodes = defaultdict(list)

        with open(file_path) as f:
            self.graph = [line.strip() for line in f]

        # print(self.graph)

    def map_nodes(self):
        for r in range(len(self.graph)):
            for c in range(len(self.graph[r])):
                if self.graph[r][c] == ".":
                    continue
                self.nodes[self.graph[r][c]].append((r, c))

        # print(self.nodes)

    def plot_antinodes(self):
        antinodes = set()

        for char in self.nodes:
            for i in range(len(self.nodes[char])):
                n1 = self.nodes[char][i]
                for j in range(i + 1, len(self.nodes[char])):
                    n2 = self.nodes[char][j]

                    rise = n2[0] - n1[0]
                    run = n2[1] - n1[1]
                    a1 = (n1[0] - rise, n1[1] - run)
                    a2 = (n2[0] + rise, n2[1] + run)

                    if 0 <= a1[0] < len(self.graph) and 0 <= a1[1] < len(self.graph[0]):
                        antinodes.add(a1)
                    if 0 <= a2[0] < len(self.graph) and 0 <= a2[1] < len(self.graph[0]):
                        antinodes.add(a2)

        return len(antinodes)

    def plot_antinodes_p2(self):
        antinodes = set()

        for char in self.nodes:
            for i in range(len(self.nodes[char])):
                n1 = self.nodes[char][i]
                for j in range(i + 1, len(self.nodes[char])):
                    n2 = self.nodes[char][j]

                    rise = n2[0] - n1[0]
                    run = n2[1] - n1[1]

                    # Extend in one direction...
                    cur_r, cur_c = n1

                    while 0 <= cur_r < len(self.graph) and 0 <= cur_c < len(
                        self.graph[0]
                    ):
                        antinodes.add((cur_r, cur_c))
                        cur_r -= rise
                        cur_c -= run

                    # ... then the other
                    cur_r, cur_c = n2

                    while 0 <= cur_r < len(self.graph) and 0 <= cur_c < len(
                        self.graph[0]
                    ):
                        antinodes.add((cur_r, cur_c))
                        cur_r += rise
                        cur_c += run

        return len(antinodes)
