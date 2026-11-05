# Is Anagram

**Problem:** Given two strings `s` and `t`, return `true` if `t` is an anagram of `s` (same characters, same counts, any order), otherwise `false`.

**Links:** [NeetCode 242](https://neetcode.io/problems/is-anagram) · [LeetCode 242](https://leetcode.com/problems/valid-anagram/)

---

## My Solution — Fixed Frequency Array

First reject different lengths. Then use a 26-slot array: increment for each character in `s`, decrement for each character in `t`. If every slot ends at zero, the strings are anagrams.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

**Caveat:** The array assumes lowercase English letters `a`–`z`, which matches the problem constraints. Uppercase, digits, or Unicode characters would index out of range.

## Optimal Solution — Same Idea, Cleaned Up

The frequency-array approach is already optimal. `zip` pairs the characters, and `all(...)` replaces the manual verification loop.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

```python
for ch_s, ch_t in zip(s, t):
    counts[ord(ch_s) - ord("a")] += 1
    counts[ord(ch_t) - ord("a")] -= 1

return all(count == 0 for count in counts)
```

## Alternative Approaches

- **Hash map / `Counter`:** O(n) time, O(n) space. Handles arbitrary characters (Unicode, uppercase). Use when the alphabet is not fixed.
- **Sorting:** O(n log n) time, O(1)–O(n) space. Shortest to write (`sorted(s) == sorted(t)`), but slower than counting.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Frequency array | **O(n)** | **O(1)** | **Default** when input is lowercase `a`–`z` |
| Hash map / Counter | O(n) | O(n) | Arbitrary characters, general solution |
| Sorting | O(n log n) | O(1)–O(n) | Quick one-liner, not the fastest |

**Interview answer:** Check lengths first, then count characters in a fixed 26-slot array — O(n) time and O(1) extra space because the alphabet size is constant. Mention `Counter` if the character set is not restricted.

## Edge Cases

- Empty strings `("", "")` → `True` (lengths equal, no characters to count).
- One empty string `("a", "")` → `False` (length check catches it).
- Same multiset, different order `("listen", "silent")` → `True`.
- Same length but different counts `("aacc", "ccac")` → `False`.
- Repeated letters `("aab", "abb")` → `False` (one slot ends non-zero).
- Uppercase / Unicode → the fixed array fails; switch to `Counter`.
