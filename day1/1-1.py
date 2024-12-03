import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "1-1.txt")

nums1 = []
nums2 = []

with open(file_path) as f:
    for line in f:
        nums = line.split()
        nums1.append(int(nums[0]))
        nums2.append(int(nums[1]))

nums1.sort()
nums2.sort()

total_diff = 0

for i in range(len(nums1)):
    cur_diff = abs(nums1[i] - nums2[i])
    total_diff += cur_diff

print(total_diff)
