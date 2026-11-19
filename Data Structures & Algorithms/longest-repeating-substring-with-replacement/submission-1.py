class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        store = {}
        for r in range(len(s)):
            store[s[r]] = store.get(s[r], 0) + 1
            while (r-l+1) - max(store.values()) > k:
                store[s[l]] -= 1
                l += 1
            res = max( (r-l+1), res)
        
        return res