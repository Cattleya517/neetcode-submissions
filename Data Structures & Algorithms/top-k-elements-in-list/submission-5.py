class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        freq = [[] for _ in range(len(nums) + 1)]

        for key, val in count.items():
            freq[val].append(key)

        result = []
        for l in reversed(freq):
            result += l
            if len(result) == k:
                return result

#[[], [3], [2], [1], [], [], []]

            