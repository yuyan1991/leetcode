class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        n = len(matrix)
        m = len(matrix[0])
        upperCount = [0] * m
        stack = [0] * m
        for i in range(n):
            stackSize = 0
            start = -1
            for j, c in enumerate(matrix[i]):
                if c == '1':
                    if start == -1:
                        start = j
                    upperCount[j] += 1
                    while stackSize > 0 and stack[stackSize - 1] >= upperCount[j]:
                        stackSize -= 1
                    stack[stackSize] = upperCount[j]
                    stackSize += 1
                    ans = max(ans, (j - start + 1) * stack[0])
                else:
                    upperCount[j] = 0
                    start = -1
        return ans