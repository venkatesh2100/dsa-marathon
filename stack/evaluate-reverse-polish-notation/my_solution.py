from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for tok in tokens:

            if tok in "+-*/":

                a = stack.pop()
                b = stack.pop()
                val = 0
                if tok == "+":val = a + b
                elif tok == "-": val = b - a
                elif tok == "*": val = a * b
                elif tok ==  "/": val = int(b / a)

                stack.append(val)
            else:
                stack.append(int(tok))
            # print(stack)
        return stack[-1]
