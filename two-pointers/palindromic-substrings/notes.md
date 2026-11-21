# Palindromic Substrings

**Problem:** Given a string `s`, return the number of palindromic substrings in `s`.

**Links:** [NeetCode](https://neetcode.io/problems/palindromic-substrings) · [LeetCode 647](https://leetcode.com/problems/palindromic-substrings/)

---

## My Solution — Expand Around Center (Odd and Even)

For every index as a center, expand outward while characters match. Every successful expansion step corresponds to one new palindromic substring, so increment the count each time. Check both odd-length centers `(i, i)` and even-length centers `(i, i + 1)`.

| | |
|---|---|
| **Time** | O(n²) |
| **Space** | O(1) |

**Caveat:** The odd and even expansion loops are duplicated. Substrings with different start/end indices count separately, even if they contain the same characters (e.g. `"aaa"` counts `"a"` three times).

## Optimal Solution — Expand Around Center with Helper

Same center-expansion idea with the odd/even logic deduplicated into a helper. Still O(n²) time and O(1) space; cleaner code. A DP table (`dp[i][j]`) is an alternative with the same complexity but O(n²) space.

| | |
|---|---|
| **Time** | O(n²) |
| **Space** | O(1) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Expand around center | **O(n²)** | **O(1)** | **Default interview answer** |
| DP table | O(n²) | O(n²) | When you already need palindrome lookups |
| Manacher's algorithm | O(n) | O(n) | When linear time is required |

**Interview answer:** Expand around every center (odd `(i, i)` and even `(i, i + 1)`), counting each valid expansion. O(n²) time, O(1) extra space.

## Edge Cases

- **Empty string** → `0`
- **Single character** → `1`
- **All distinct** (`"abc"`) → `n` (each single character)
- **All same** (`"aaa"`) → 6 (`"a"×3`, `"aa"×2`, `"aaa"×1`)
- **Even-length palindromes** (`"aa"`) → 3 (`"a"×2`, `"aa"×1`)
