class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, len(s) - 1
        best = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            best = max(best, len(seen))

        return best

#'abba'  a,   ab,  b , , ba
# ''