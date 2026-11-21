# Decode Ways

**Problem:** A string of digits can be decoded into letters (`A` = 1, ..., `Z` = 26). Return the number of ways to decode it.

**Links:** [NeetCode](https://neetcode.io/problems/decode-ways) · [LeetCode 91](https://leetcode.com/problems/decode-ways/)

---

## My Solution — Top-down Memoization (`@cache`)

Recurse from index `i`: take one digit (valid if it isn't `'0'`) or take two digits (valid if they form `10`–`26`). Cache the result per index so each suffix is computed once. Leading `'0'` yields `0` ways.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

**Caveat:** Recursion depth can reach `n`, and `@cache` holds one entry per index. Input is assumed non-empty (LeetCode guarantees `1 <= len(s)`).

## Optimal Solution — Bottom-up DP, O(1) Space

Iterate from the end of the string, keeping only the next two counts. `cur = next_one` (one-digit decode) plus `next_two` when the two-digit chunk is `10`–`26`. Shift the pair forward each step.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

This is optimal: every index is visited once, and O(n) time is a lower bound since the whole string may need to be scanned. O(1) extra space is best possible.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Top-down memoization | O(n) | O(n) | Clean, mirrors the recurrence |
| Bottom-up, two variables | **O(n)** | **O(1)** | **Default interview answer** |
| Brute-force recursion | O(2ⁿ) | O(n) | Never — exponential without memoization |

**Interview answer:** "It's DP on suffixes: at each index take one valid digit or a valid two-digit pair, memoize results, then convert to bottom-up with two rolling variables for O(1) space."

## Edge Cases

- `"0"` → `0` (no letter starts with zero)
- `"10"` → `1` (`"J"`)
- `"12"` → `2` (`"AB"`, `"L"`)
- `"226"` → `3` (`"2 2 6"`, `"22 6"`, `"2 26"`)
- `"06"` → `0` (leading zero can't be decoded)
- `"27"` → `1` (`"2 7"`; `"27"` is out of range)
