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
    - 通过使用最大堆（Max-Heap）来优化这个过程。最大堆的数据结构允许我们快速地获取和更新最大值，操作复杂度为 O(log n)。
    在Python中，heapq模块实现的是最小堆（Min-Heap），所以我们可以通过将数组中的每个元素取负值来模拟最大堆的行为。

"""
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Convert nums into a max-heap by negating all elements (Python's heapq is a min-heap by default)
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        score = 0

        for _ in range(k):
            # Extract the maximum element (by popping the smallest in the negated max-heap)
            maxnum = -heapq.heappop(max_heap)
            score += maxnum

            # Push the updated value back into the heap
            heapq.heappush(max_heap, -ceil(maxnum / 3))

        return score
