class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for ch in s:
            if ch in pairs:  # opener: remember it
                stack.append(ch)
            elif stack and pairs[stack[-1]] == ch:  # matches the most recent opener
                stack.pop()
            else:  # closer with nothing to match
                return False

        return not stack
