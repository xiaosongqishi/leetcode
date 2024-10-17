"""
Problem Link: 和 323 特别像
    https://leetcode.com/problems/number-of-provinces/
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edges = []
        for i, contain in enumerate(isConnected):
            for index, number in enumerate(contain):
                if number == 1:
                    edges.append([i, index])

        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                # self.parent = [ i for i in range(1, size + 1)]
                print(self.parent)
                self.rank = [1] * size

            def find(self, x):
                # 递归查找根节点，并进行路径压缩
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                # 查找 x 和 y 的根节点
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    # 按秩合并，较小秩合并到较大秩的根上
                    if self.rank[rootX] > self.rank[rootY]:
                        self.parent[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.parent[rootX] = rootY
                    else:
                        # 如果秩相等，选择一个作为新的根，并将其秩加一
                        self.parent[rootY] = rootX
                        self.rank[rootX] += 1
                    return 1

        n = len(isConnected)
        res = n
        uf = UnionFind(n)
        for e1, e2 in edges:
            if uf.union(e1, e2) == 1:
                res -= 1
        return res


# dfs方法
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited[i] = True
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)

        provinces = 0
        visited = [False] * len(isConnected)

        for i in range(len(isConnected)):
            if not visited[i]:
                provinces += 1
                dfs(i)

        return provinces
