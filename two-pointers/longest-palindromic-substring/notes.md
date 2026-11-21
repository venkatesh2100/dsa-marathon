# Longest Palindromic Substring

**Problem:** Given a string `s`, return the longest palindromic substring in `s`.

**Links:** [NeetCode](https://neetcode.io/problems/longest-palindromic-substring) · [LeetCode 5](https://leetcode.com/problems/longest-palindromic-substring/)

---

## My Solution — Expand Around Center (Odd and Even)

Treat every index as a center and expand outward while the characters match. Check both odd-length centers `(i, i)` and even-length centers `(i, i + 1)`, keeping the longest match found.

| | |
|---|---|
| **Time** | O(n²) |
| **Space** | O(1) |

**Caveat:** The odd and even expansion loops are duplicated. Each center can expand up to O(n), giving O(n²) time. Returns the first (leftmost) longest palindrome on ties.

## Optimal Solution — Expand Around Center with Helper

Same expand-around-center idea, but the odd/even expansion is deduplicated into a helper that returns the bounds of the palindrome it finds. Still O(n²) time and O(1) space, but cleaner and less error-prone. (Manacher's algorithm gives O(n) time but is more complex and rarely required in interviews.)

| | |
|---|---|
| **Time** | O(n²) |
| **Space** | O(1) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Expand around center | **O(n²)** | **O(1)** | **Default interview answer** |
| Manacher's algorithm | O(n) | O(n) | When linear time is required |

**Interview answer:** Expand around every center, checking both odd `(i, i)` and even `(i, i + 1)` lengths, and track the longest palindrome. O(n²) time, O(1) extra space.

## Edge Cases

- **Empty string** → `""`
- **Single character** → the character itself
- **All same characters** (`"aaaa"`) → the whole string
- **No palindrome longer than 1** (`"abc"`) → any single character (leftmost)
- **Even-length palindrome** (`"cbbd"`) → `"bb"`
- **Multiple equal-length palindromes** → returns the leftmost one
