class Solution:
    def numTilings(self, n: int) -> int:
        mod = 1_000_000_000 + 7
        f = [[0 for i in range(1 << 2)] for i in range(2)]
        f[0][(1 << 2) - 1] = 1
        o0 = 0
        o1 = 1
        for i in range(n):
            f[o1][0] = f[o0][(1 << 2) - 1]
            f[o1][1] = (f[o0][0] + f[o0][2]) % mod
            f[o1][2] = (f[o0][0] + f[o0][1]) % mod
            f[o1][(1 << 2) - 1] = (f[o0][0] + f[o0][1] + f[o0][2] + f[o0][(1 << 2) - 1]) % mod
            o0 = o1
            o1 ^= 1
        return f[o0][(1 << 2) - 1]