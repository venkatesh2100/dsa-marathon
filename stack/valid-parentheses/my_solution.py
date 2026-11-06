class Solution:
    def isValid(self, s: str) -> bool:


        dic = { "{":"}" , "[":"]" , "(":")" }
        stack = []

        for i in range(len(s)):

            if s[i] in dic:
                stack.append(s[i])

            elif stack and s[i] == dic[stack[-1]]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
