class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window: [l..r] always holds only distinct characters.
        # When s[r] is a duplicate, pop from the left until the previous
        # occurrence of s[r] is evicted. Each index enters the set once and
        # leaves at most once, so the nested loops together are still O(n)
        # — NOT O(n²), despite appearances.
        seen = set()
        l = res = 0
        for r in range(len(s)):
            while s[r] in seen:  # no-op when s[r] is not a duplicate
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res