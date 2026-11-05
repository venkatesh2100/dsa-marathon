class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for ch_s, ch_t in zip(s, t):
            counts[ord(ch_s) - ord("a")] += 1
            counts[ord(ch_t) - ord("a")] -= 1

        return all(count == 0 for count in counts)
