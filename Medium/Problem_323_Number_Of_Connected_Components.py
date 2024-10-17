"""
Problem Link: 和 547 特别像
    https://www.youtube.com/watch?v=8f1XPm4WOUc&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=33&pp=iAQB
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
    - Number of Connected Components in an Undirected Graph - Union Find
    Union-Find（又称 Disjoint Set Union 或 DSU）是一种数据结构，用于高效地处理和维护不相交集合。它支持两个主要操作：

    Union：将两个集合合并。
    Find：查找一个元素所属集合的代表（或根节点）。
    Union-Find 常用于解决连通性问题，例如在无向图中判断是否存在环、动态连通性、最小生成树等。

"""
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
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
    res = n
    uf = UnionFind(n)
    for e1, e2 in edges:
        if uf.union(e1, e2):
            res -= 1

    return res