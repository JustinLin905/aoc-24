import os
from collections import defaultdict


class Solution:
    def __init__(self, file_name):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.script_dir, file_name)

        reading_rules = True
        self.rules = defaultdict(set)
        self.updates = []
        with open(self.file_path) as f:
            for line in f:
                if line.strip() == "":
                    reading_rules = False
                    continue

                if reading_rules:
                    rule = line.split("|")
                    self.rules[int(rule[0])].add(int(rule[1]))
                else:
                    update = [int(num) for num in line.split(",")]
                    self.updates.append(update)

        # print(self.rules)
        # print(self.updates)

    def validate_update(self, update):
        """
        Accepts update as a list of ints, returns True if correctly ordered
        """
        for i in range(len(update)):
            cur = update[i]

            for j in range(i):
                prev = update[j]
                if prev in self.rules[cur]:
                    return False

        return True

    def sort_update(self, update):
        """
        Accepts an invalid update as a list of ints, and rearranges it so that it obeys all applicable rules and becomes valid

        Returns: void
        """
        for i in range(len(update)):
            for j in range(i):
                if update[j] in self.rules[update[i]]:
                    # Swap
                    update[i], update[j] = update[j], update[i]

    def sum_valid_updates(self):
        res = 0
        for update in self.updates:
            if self.validate_update(update):
                # Add the middle value
                m = len(update) // 2
                res += update[m]

        return res

    def sum_invalid_updates(self):
        res = 0
        for update in self.updates:
            if not self.validate_update(update):
                # Sort and add middle value
                self.sort_update(update)
                m = len(update) // 2
                res += update[m]

        return res
