class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddPosition = evenPosition = 0
        for p in position:
            if p % 2 == 1:
                oddPosition += 1
            else:
                evenPosition += 1
        return min(oddPosition, evenPosition)