import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "2.txt")

res = 0

with open(file_path) as f:
    for line in f:
        nums = line.split()

        increasing = all(
            1 <= int(nums[i + 1]) - int(nums[i]) <= 3 for i in range(len(nums) - 1)
        )
        decreasing = all(
            1 <= int(nums[i]) - int(nums[i + 1]) <= 3 for i in range(len(nums) - 1)
        )

        if increasing or decreasing:
            res += 1

print(res)
