import os
from collections import deque


class Solution:
    def __init__(self, file_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)

        self.disk_map = ""
        self.id_queue = deque()
        self.space_queue = deque()

        self.id_intervals = deque()
        self.space_intervals = deque()

        with open(file_path) as f:
            self.disk_map = f.readline().strip()

        # print(self.disk_map)

        # Process string to find counts of IDs and intervals of free space
        cur_id = 0
        cur_index = 0
        for i in range(len(self.disk_map)):
            val = int(self.disk_map[i])

            # Blocks of files
            if i & 1 == 0:
                # Interval
                self.id_intervals.append((cur_index, cur_index + val, cur_id))

                for _ in range(val):
                    self.id_queue.append(cur_id)
                    cur_index += 1

                cur_id += 1
            else:
                # Interval
                self.space_intervals.append((cur_index, cur_index + val))

                for _ in range(val):
                    self.space_queue.append(cur_index)
                    cur_index += 1

        # print(self.id_queue)
        # print(self.space_queue)
        # print(self.id_intervals)
        # print(self.space_intervals)

    def p1(self):
        cur_index = 0
        res = 0

        while self.id_queue:
            if self.space_queue[0] == cur_index:
                # Pop from right end of id queue and left of space queue
                self.space_queue.popleft()
                val = self.id_queue.pop()
                res += cur_index * val
            else:
                # Not at a blank space, pop from left of id queue
                val = self.id_queue.popleft()
                res += cur_index * val

            cur_index += 1

        return res

    def p2(self):
        finished_intervals = []
        res = 0

        # Attempt move in decreasing ID order
        while self.id_intervals:
            start, end, cur_id = self.id_intervals.pop()

            for i, space_interval in enumerate(self.space_intervals):
                space_start, space_end = space_interval
                space_len = space_end - space_start
                id_len = end - start

                if space_len >= id_len and space_start <= start:
                    start, end = space_start, space_start + id_len
                    self.space_intervals[i] = (space_start + id_len, space_end)
                    break

            finished_intervals.append((start, end, cur_id))

        for start, end, cur_id in finished_intervals:
            for j in range(start, end):
                res += cur_id * j

        return res
