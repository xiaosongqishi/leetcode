"""
Problem Link:
    [https://leetcode.com/problems/missing-number/description/]

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
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N + 1):
            if i not in nums:
                return i

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(res):
            res += (i - nums[i])
        return res
