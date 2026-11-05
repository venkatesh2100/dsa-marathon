class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = [v.lower() for v in s if v.isalnum()]

        return s == s[::-1]
