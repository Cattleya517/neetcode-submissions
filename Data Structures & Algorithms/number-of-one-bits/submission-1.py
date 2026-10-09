class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n >= 1:
            count += n & 1
            n = n >> 1
        return count

# 23
# count = 1 n = 11
# count = 2 n = 5
# count = 3 n = 2
# conut = 3 n = 1
# count = 4 n = 0