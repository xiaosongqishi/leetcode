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
    - 使用最小（大）堆来实现，保证每次使用最多的字母，如果有限制，选用第二多的

"""
import heapq


def longestHappyString(a: int, b: int, c: int) -> str:
    # Max-Heap to store characters with counts (negative for max-heap behavior)
    heap = []
    if a > 0:
        heapq.heappush(heap, (-a, 'a'))
    if b > 0:
        heapq.heappush(heap, (-b, 'b'))
    if c > 0:
        heapq.heappush(heap, (-c, 'c'))

    result = []

    while heap:
        # Pop the character with the highest remaining count
        count1, char1 = heapq.heappop(heap)

        # Check if we can append it to the result
        if len(result) > 1 and result[-1] == result[-2] == char1:
            # If appending char1 would cause three consecutive chars, use the next most frequent character
            if not heap:
                break  # If no other character to use, we're done

            # Use the second character instead
            count2, char2 = heapq.heappop(heap)
            result.append(char2)
            count2 += 1  # Use one count of char2

            # Put char2 back if it still has remaining count
            if count2 < 0:
                heapq.heappush(heap, (count2, char2))

            # Put char1 back for the next round
            heapq.heappush(heap, (count1, char1))

        else:
            # Append char1 as it does not cause any consecutive issue
            result.append(char1)
            count1 += 1  # Use one count of char1

            # Put char1 back if it still has remaining count
            if count1 < 0:
                heapq.heappush(heap, (count1, char1))

    return ''.join(result)

