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
    - bfs 是队列先进先出， dfs 是队列后进先出，direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]学习这种方式
    如果面试管问如何用dfs 则改动q.pop 就可以

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                row, col = q.popleft() # bfs
                # row, col = q.pop() # dfs
                for dr, dc in direction:
                    r = row + dr
                    c = col + dc
                    if (c in range(cols) and
                            r in range(rows) and
                            grid[r][c] == "1" and
                            (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands


