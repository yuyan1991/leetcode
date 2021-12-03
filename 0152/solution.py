class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = - 1 << 30
        negativeIntegerPrefix = currentRes = 1
        totalNegativeInteger = 0
        for num in nums:
            currentIsFirstNegativeInteger = False
            if num == 0:
                ans = max(ans, 0)
                negativeIntegerPrefix = currentRes = 1
                totalNegativeInteger = 0
                continue
            currentRes *= num
            if num < 0:
                totalNegativeInteger += 1
                if totalNegativeInteger == 1:
                    negativeIntegerPrefix = currentRes
                    currentIsFirstNegativeInteger = True
            
            if totalNegativeInteger & 1:
                if currentIsFirstNegativeInteger:
                    ans = max(ans, negativeIntegerPrefix)
                else:
                    ans = max(ans, currentRes // negativeIntegerPrefix)
            else:
                ans = max(ans, currentRes)
        return ans