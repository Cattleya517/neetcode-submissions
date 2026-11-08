class Solution:
    def climbStairs(self, n: int) -> int:
        a , b = 1, 1  # f(1), f(1) 
        for i in range(n):  
            nexxt = a+b   #f(2)
            a = b
            b = nexxt
        return a