class Solution:
    def climbStairs(self, n: int) -> int:
        a , b = 0, 1
        for i in range(n):   #0, 1, 2  (n=3)
            cur = a+b
            a = b
            b= cur
        return b 