"""
Problem Link:
    [https://leetcode.com/problems/contains-duplicate/description/]

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
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for n in nums:
            if n in table:
                return True
            else:
                table[n] = True
        return False