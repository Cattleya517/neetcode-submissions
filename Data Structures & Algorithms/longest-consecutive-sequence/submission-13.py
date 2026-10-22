class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet  = set(nums)
        result = 0
        for n in numSet:
            if n-1 in numSet: # 不是起點
                pass
            else:
                count = 1
                track = n
                while track + 1 in numSet:
                    count += 1
                    track+=1
                result = max(count, result)
        
        return result