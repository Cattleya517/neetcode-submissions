class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n ==2:
            return n
        result = [0] * n
        result[0], result[1] = 1, 2
        for i in range(2, n):
            result[i] =  result[i-1] + result[i-2] 

        return result[n-1]