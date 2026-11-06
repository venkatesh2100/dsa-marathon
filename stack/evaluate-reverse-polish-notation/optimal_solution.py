from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            # LeetCode truncates toward zero; Python's // floors (-7 // 2 == -4)
            "/": lambda x, y: int(x / y),
        }

        stack = []
        for token in tokens:
            if token in ops:
                y = stack.pop()  # right operand, pushed last
                x = stack.pop()  # left operand
                stack.append(ops[token](x, y))
            else:
                stack.append(int(token))

        return stack[0]  # a valid expression leaves exactly one value
