"""
Problem Link:
    [https://leetcode.com/problems/number-of-1-bits/]

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
    - The trick here is to avoid check multiple zero in n
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res = n % 2
            n = n >> 1 # check bit by bit
        return res