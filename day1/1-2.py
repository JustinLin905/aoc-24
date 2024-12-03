import os
from collections import defaultdict

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the file
file_path = os.path.join(script_dir, "1-1.txt")

nums1 = []
# nums2 = []
right_count = defaultdict(int)

with open(file_path) as f:
    for line in f:
        nums = line.split()
        nums1.append(int(nums[0]))
        right_count[int(nums[1])] += 1


res = 0
for num in nums1:
    similarity_score = num * right_count[num]
    res += similarity_score

print(res)
