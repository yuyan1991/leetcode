class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        sum = [[0 for i in range(m)] for i in range(n)]

        if matrix[0][0] == '1':
            sum[0][0] = 1
        else:
            sum[0][0] = 0
        for i in range(1, m):
            num = 0
            if matrix[0][i] == '1':
                num = 1
            sum[0][i] = sum[0][i - 1] + num
        for i in range(1, n):
            num = 0
            if matrix[i][0] == '1':
                num = 1
            sum[i][0] = sum[i - 1][0] + num
        for i in range(1, n):
            for j in range(1, m):
                num = 0
                if matrix[i][j] == '1':
                    num = 1
                sum[i][j] = sum[i][j - 1] + sum[i - 1][j] - sum [i - 1][j - 1] + num
        foundSize = 0
        for i in range(n):
            for j in range(m):
                maxSize = min(i + 1, j + 1)
                cur = 0
                for k in range(foundSize + 1, maxSize + 1):
                    topSum = leftSum = leftTopSum = 0
                    if i >= k:
                        topSum = sum[i - k][j]
                    if j >= k:
                        leftSum = sum[i][j - k]
                    if i >= k and j >= k:
                        leftTopSum = sum[i - k][j - k]
                    if sum[i][j] - topSum - leftSum + leftTopSum == k * k:
                        cur = k
                    else:
                        break
                foundSize = max(foundSize, cur)
        return foundSize * foundSize