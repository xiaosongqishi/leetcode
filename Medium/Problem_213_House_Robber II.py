"""
Problem Link:
    [Paste the LeetCode problem URL here, e.g., https://leetcode.com/problems/problem-name/]

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
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]):
        rob1 = 0
        rob2 = 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
