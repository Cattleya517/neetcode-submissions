class Solution:
    def rob(self, nums: List[int]) -> int:
    # [rob1, rob2, n, n+1]
        rob1, rob2 = 0, 0

        for n in nums:
            # 計算本輪最大值
            cur = max(n+ rob1,rob2) 
            
            #準備下一輪
            rob1 = rob2
            rob2 = cur

        return rob2
