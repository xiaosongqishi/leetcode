"""
Problem Link:
    [https://leetcode.com/problems/counting-bits/description/]

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
    def countBits(self, n: int) -> List[int]:
        def dectobin(n):
            res = []
            if n == 0:
                res = [0]
            while n > 0:
                res.append(n % 2)
                n = n // 2
            res.reverse()
            return res

        res = []
        for i in range(n + 1):
            num = dectobin(i)
            res.append(num.count(1))

        return res


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp