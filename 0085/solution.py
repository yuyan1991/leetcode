# 斜率优化
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = self.cal(matrix)
        reversedMatrix = []
        for row in matrix:
            reversedMatrix.append(row[::-1])
        ans = max(ans, self.cal(reversedMatrix))
        return ans
    
    def cal(self, matrix):
        ans = 0
        m = len(matrix[0])
        u = [0 for i in range(m)]
        for row in matrix:
            q = [[0, 0, -1] for i in range(m + 1)]
            leftPosition = [[0, -1] for i in range(m + 1)]
            leftPositionSize = 1
            head = tail = 0
            for i, element in enumerate(row):
                if element == "0":
                    leftPositionSize = 1
                    leftPosition[leftPositionSize - 1] = [0, i]
                    head = tail = 0
                    u[i] = 0
                else:
                    u[i] += 1
                    while leftPositionSize > 0 and leftPosition[leftPositionSize - 1][0] >= u[i]:
                        leftPositionSize -= 1
                    while head < tail and q[tail - 1][0] >= u[i]:
                        tail -= 1
                    q[tail][0] = u[i]
                    q[tail][1] = i
                    q[tail][2] = leftPosition[leftPositionSize - 1][1]
                    tail += 1
                    while head + 1 < tail and q[head][0] * (i - q[head][2]) <= q[head + 1][0] * (i - q[head + 1][2]):
                        head += 1
                    leftPosition[leftPositionSize] = [u[i], i]
                    leftPositionSize += 1
                    ans = max(ans, q[head][0] * (i - q[head][2]))
        return ans