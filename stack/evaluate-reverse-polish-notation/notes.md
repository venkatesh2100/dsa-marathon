# Evaluate Reverse Polish Notation

**Problem:** Given `tokens` forming a valid Reverse Polish (postfix) arithmetic expression, evaluate it and return the value. Operators `+ - * /` apply to the two most recent operands; `/` divides and **truncates toward zero**.

**Links:** [NeetCode 150](https://neetcode.io/problems/evaluate-reverse-polish-notation) · [LeetCode 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

---

## My Solution — Stack Evaluation

Push parsed numbers. When a token is an operator, the stack top holds the two most recent operands: pop `a` (the right operand), then `b` (the left operand), compute the operation, and push the result back. The expression is prefix-free and fully evaluated, so the single remaining entry is the answer.

Order matters for the non-commutative operators: `val = b - a` and `int(b / a)` use the first-popped value as the *right* operand.

| | |
|---|---|
| **Time** | O(n) — each token is processed once |
| **Space** | O(n) — the stack never holds more than about half the tokens |

**Caveats:** `if tok in "+-*/"` is substring containment — safe only because operator tokens are exactly one character long (negative numbers like `"-11"` are not substrings of `"+-*/"`, so they fall through to `int`). A set `{"+", "-", "*", "/"}` states that intent explicitly. The key subtlety is division: Python's `//` **floors** (`7 // -2 == -4`), but the problem truncates toward zero (`-3`), hence `int(b / a)`. That conversion goes through a float; it is exact for LeetCode's constraints (intermediates fit in 32 bits), while a sign-aware `abs(b) // abs(a)` stays exact for any magnitude. Minor: `val = 0` is dead code, and the commented `# print(stack)` can be dropped.

## Optimal Solution — Stack with Operator Table

Same evaluation; the operator lives in a dict, iterating tokens directly, and the pops land in clearly named variables so operand order is obvious.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

```python
ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: int(x / y),  # LeetCode truncates toward zero
}

for token in tokens:
    if token in ops:
        y = stack.pop()  # right operand, pushed last
        x = stack.pop()  # left operand
        stack.append(ops[token](x, y))
    else:
        stack.append(int(token))
```

Each token triggers O(1) stack work, so O(n) time is optimal — every token must be read once — and the helper stack's depth is bounded by the token count.

## Alternative Approaches

- **Stack with operator table (optimal):** O(n) time, O(n) space. Standard.
- **If/elif chain (my solution):** O(n) time, O(n) space. Same complexity; fine either way.
- **Recursive evaluation over the array:** Process tokens from the end with a shared index. O(n) time, O(n) depth; elegant but easier to get wrong.
- **Repeated pairwise reduction:** Scan until an operator, splice in the result, repeat. O(n²) time.
- **`eval()` on a rebuilt infix string:** O(n) but arbitrary-code execution hazards and float semantics (`/`) unless patched out. Never.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Stack + operator table | **O(n)** | **O(n)** | **Default interview answer** |
| Stack + if/elif (mine) | O(n) | O(n) | Identical speed; dict scales better |
| Recursive scan | O(n) | O(n) | If the interviewer wants recursion |
| Splicing array | O(n²) | O(n) | Never — only for comparison |
| `eval()` | O(n) | O(n) | Never — unsafe and wrong division semantics |

**Interview answer:** One pass with a stack: push numbers, and on an operator pop two values (top = right operand), combine as `left op right`, and push. Return the last value. Division truncates toward zero, so in Python use `int(x / y)` — not `//`, which floors. O(n) time, O(n) space.

## Edge Cases

- **Single number** (`["18"]`) → `18`.
- **LeetCode examples** (`["2","1","+","3","*"]` → `9`, `["4","13","5","/","+"]` → `6`, and the longer one → `22`).
- **Truncation toward zero** (`["7","-2","/"]` → `-3`, `["6","-132","/"]` → `0`) — floor division would give `-4` and `-1` instead.
- **Non-commutative order** (`["4","-2","/","2","3","*","-"]` → `-8`): swapping the two pops flips `-` and `/` results.
- **Operand order in `/`** (`["-3","2","/"]` → `-1`): first token minus-divided-by second.
- **Multi-digit and negative tokens** (`"13"`, `"-11"`) → `int()` parses them; only exact single-character operator tokens match the operator check.
- **Zero denominator** → impossible per the "valid expression" guarantee.
- **Large products** → Python integers are unbounded; `int(x / y)`'s float path is exact while intermediates fit 32 bits.
- **Empty input** → outside the constraints (`len(tokens) ≥ 2`); the final peek would raise defensively.
