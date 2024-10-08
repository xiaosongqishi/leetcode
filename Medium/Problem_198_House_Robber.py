"""
Problem Link:
    [https://leetcode.com/problems/house-robber/description/]

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
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []
        L = len(nums)
        dp = [0] * L
        if L == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1] + 0)
        for i in range(2, L):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            # print(dp[i])

        return max(dp)
