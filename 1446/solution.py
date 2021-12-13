class Solution:
    def maxPower(self, s: str) -> int:
        ans = cur = 0
        prev = ''
        for c in s:
            if c == prev:
                cur += 1
            else:
                cur = 1
                prev = c
            if cur > ans:
                ans = cur
        return ans