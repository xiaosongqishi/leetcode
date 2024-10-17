"""
Problem Link:
    [https://www.youtube.com/watch?v=6kTZYvNNyps&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=32]

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
    -先创建每个字母跟着的adj，即字母的先后顺序，
    再判断是否出现循环或者不符合要求的地方


"""
def alienOrder(self, words: List[str]) -> str:
    adj = { c:set() for w in words for c in w}

    for i in range(len(words) - 1):
        w1, w2 =  words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""

        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    visit = {}
    res = []

    def dfs(c):
        if c in visit:
            return visit[c]

        visit[c] = True

        for nei in adj[c]:
            if dfs[nei]:
                return True

        visit[c] = False
        res.append(c)

    for c in adj:
        if dfs(c):
            return ""

    res.reverse()
    return "".join(res)