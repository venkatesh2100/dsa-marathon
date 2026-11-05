class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False
        nums = [0] * 26

        # print(ord('a'))

        for i in range(len(s)):
            # print(ord(s[i]) - ord('a'))
            nums[ord(s[i]) - ord('a')]+=1
            nums[ord(t[i]) - ord('a')]-=1

        for v in nums:
            if v !=0: return False

        return True
