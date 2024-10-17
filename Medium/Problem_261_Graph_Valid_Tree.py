"""
Problem Link:
    https://www.youtube.com/watch?v=bXsUuownnoQ&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=32
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
def vaildTree(self, n, edges):
    if not n:
        return True

    adj = { i:[] for i in range(n) }
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    visit = set()

    def dfs(Node, prevNode):
        if Node in visit:
            return False
        visit.add(Node)
        for nei in adj[Node]:
            if nei == prevNode:
                continue
            if not dfs(nei, Node):
                return False

        return True

    return dfs(0, -1) and len(visit) == n

# My way:
def vaildTree(self, n, edges):
    if n <= 1:
        return True
    
    adj = {}
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    
    visit = set()
    
    def dfs(Node, prevNode):
        if Node in visit or prevNode in visit:
            return False
        visit.add(Node)
        for nei in adj[Node]:
            dfs(nei, Node)
        
        return True
    
    if dfs(0, -1) and len(visit) == n:
        return True
    else:
        return False

