"""
Problem Link:
    [https://leetcode.com/problems/search-in-rotated-sorted-array/description/]

Key Points:
    - Input:
        [Describe the input format, data types, and constraints.]
    - Output:
        [Describe the expected output format and data types.]
    - Constraints:
        [List all the important constraints and edge cases.]

Approach:
    1. [Step 1 of your approach to solving the problem.]
    2. [Step 2 of your approach, etc.]

Complexity Analysis:
    - Time Complexity: [Explain the time complexity of your solution.]
    - Space Complexity: [Explain the space complexity of your solution.]

Notes:
    - [Any additional notes, observations, or optimizations.]

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2  # 计算中间索引
            if nums[m] == target:
                return m  # 找到目标值，返回索引

            # 判断哪一侧是有序的
            if nums[m] >= nums[l]:
                # 左半部分是有序的
                if nums[l] <= target < nums[m]:
                    r = m - 1  # 在左半部分查找
                else:
                    l = m + 1  # 否则在右半部分查找
            else:
                # 右半部分是有序的
                if nums[m] < target <= nums[r]:
                    l = m + 1  # 在右半部分查找
                else:
                    r = m - 1  # 否则在左半部分查找

        return -1  # 未找到目标值