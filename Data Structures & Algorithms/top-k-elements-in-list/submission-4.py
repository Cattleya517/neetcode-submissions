class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        freq = [[] for _ in range(len(nums) + 1)]

        for key, val in count.items():
            freq[val].append(key)

        result = []
        target = 0
        for l in freq[::-1]:
            if l:
                result += l
                target += len(l)
                if target == k:
                    return result
            else: 
                continue 

#[[], [3], [2], [1], [], [], []]

            