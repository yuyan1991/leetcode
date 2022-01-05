# 斜率优化
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = self.cal(heights)
        reversedHeights = heights[::-1]
        ans = max(ans, self.cal(reversedHeights))
        return ans
    
    def cal(self, heights):
        ans = 0
        m = len(heights)
        q = [[0, 0, -1] for i in range(m + 1)]
        leftPosition = [[0, -1] for i in range(m + 1)]
        leftPositionSize = 1
        head = tail = 0
        for i, height in enumerate(heights):
            while leftPositionSize > 0 and leftPosition[leftPositionSize - 1][0] >= height:
                leftPositionSize -= 1
            while head < tail and q[tail - 1][0] >= height:
                tail -= 1
            q[tail][0] = height
            q[tail][1] = i
            q[tail][2] = leftPosition[leftPositionSize - 1][1]
            tail += 1
            while head + 1 < tail and q[head][0] * (i - q[head][2]) <= q[head + 1][0] * (i - q[head + 1][2]):
                head += 1
            leftPosition[leftPositionSize] = [height, i]
            leftPositionSize += 1
            ans = max(ans, q[head][0] * (i - q[head][2]))
        return ans