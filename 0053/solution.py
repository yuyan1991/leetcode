class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur = 0
        for num in nums:
            cur += num
            if cur > res:
                res = cur
            if cur < 0:
                cur = 0
        return res