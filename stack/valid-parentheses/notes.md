# Valid Parentheses

**Problem:** Given a string `s` containing only the characters `(`, `)`, `{`, `}`, `[`, `]`, return `true` if every bracket is closed by the same type in the correct order. Each closer must match the most recent still-open bracket (LIFO nesting).

**Links:** [NeetCode 20](https://neetcode.io/problems/valid-parentheses) · [LeetCode 20](https://leetcode.com/problems/valid-parentheses/)

---

## My Solution — Opener Dictionary + Stack

Map each opener to its closer and push openers onto a stack. Every other character is a closer: it must equal the closer expected by the opener on top of the stack. Pop on a match; otherwise the string is invalid. At the end, the string is valid only if the stack is empty (no unclosed openers).

| | |
|---|---|
| **Time** | O(n) — one pass, O(1) work per character |
| **Space** | O(n) — the stack can hold every opener of a nested string |

**Caveat:** Runs as pasted only after removing a stray `+` line before the final `return` — a paste typo and a guaranteed SyntaxError otherwise. That was the only edit. Other cleanups: the closer dictionary could be indexed through `pairs[stack[-1]] == s[i]`; `for i in range(len(s))` can become `for ch in s`. A general-purpose hazard, not triggered by this problem: any character that is not a bracket receives no explicit handler and fails as a closer (`"x"` → `False`); LeetCode guarantees brackets only.

## Optimal Solution — Stack + Pairs Map (Same Idea, Polished)

The attempt is already the standard optimal approach. Iterating characters directly reads better, and the empty-stack check doubles as the reject case for early closers.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

```python
for ch in s:
    if ch in pairs:                       # opener: remember it
        stack.append(ch)
    elif stack and pairs[stack[-1]] == ch:  # matches the most recent opener
        stack.pop()
    else:                                 # closer with nothing to match
        return False

return not stack
```

Every character triggers O(1) stack work, so O(n) time is optimal — each character must be read at least once, and any valid nested string forces storage proportional to its nesting depth in the worst case.

## Alternative Approaches

- **Stack + pairs map (my solution / optimal):** O(n) time, O(n) space. Standard.
- **Closer-to-opener map:** Map `"}"` → `"{"` and check `pairs[ch] == stack[-1]`. Same complexity, equivalent logic.
- **Repeated pairwise replacement:** Erase `()`, `[]`, `{}` from the string until nothing changes, then check emptiness. O(n²) worst case; simple oracle, slow answer.
- **Counter naïve:** Count brackets per type independently. Wrong — it ignores nesting order (`"([)]"` looks balanced by counts).

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Stack + pairs map | **O(n)** | **O(n)** | **Default interview answer** |
| Closer-to-opener map | O(n) | O(n) | Equivalent variant; personal taste |
| Repeated replacement | O(n²) | O(n) | Useful as an independent testing oracle |
| Counting only | O(n) | O(1) | ❌ Incorrect — misses order (`"([)]"`) |

**Interview answer:** Push openers onto a stack. Each closer must match the closer of the stack top, so pop it; anything else is invalid. Accept when the stack is empty at the end. O(n) time and O(n) space.

## Edge Cases

- **Empty string** → `true` (vacuously balanced); LeetCode guarantees length ≥ 1.
- **Single bracket** (`"("`, `")"`) → `false`.
- **Simple pair** (`"()"`) → `true`.
- **Wrong type** (`"(]"`) → `false`; the closer does not match the top.
- **Wrong order** (`"([)]"`) → `false`; counts look fine but nesting breaks.
- **Unopened closer** (`"]"`) → `false`; the stack is empty when the closer arrives.
- **Unclosed opener** (`"((("`) → `false`; rejected by the final emptiness check.
- **Only closers** (`"]]]"`) → `false`; every closer hits an empty stack.
- **Nested correctly** (`"{[()()]}"`, `"((()))"`) → `true`.
- **Sequential pairs** (`"()[]{}"`, `"()()"`) → `true`.
- **Deep nesting** → stack grows to the depth; iterative stack avoids recursion limits.
- **Non-bracket characters** (`"a"`) → outside the constraints; the code rejects them since nothing matches.
