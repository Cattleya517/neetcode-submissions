class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        isum, nnums = 0, 0
        
        for i, n in enumerate(nums):
            isum += i
            nnums += n

        return len(nums) + isum - nnums