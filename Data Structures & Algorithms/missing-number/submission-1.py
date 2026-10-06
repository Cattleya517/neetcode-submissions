class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        idSum, nSum = 0, 0
        for i, n in enumerate(nums):    
            idSum += i
            nSum += n
        
        return idSum + len(nums) - nSum 