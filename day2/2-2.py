import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "2.txt")


def safe(nums):
    if len(nums) < 2:
        return True

    diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

    return (all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)) and all(
        1 <= abs(diff) <= 3 for diff in diffs
    )


def exclude(nums, i):
    return nums[:i] + nums[i + 1 :]


res = 0
with open(file_path) as f:
    for line in f:
        nums = [int(num) for num in line.split()]

        if any(safe(exclude(nums, i)) for i in range(len(nums))):
            res += 1

print(res)
