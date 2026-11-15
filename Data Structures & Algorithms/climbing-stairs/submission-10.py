class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            nxt = a+b
            a = b
            b = nxt
        return a