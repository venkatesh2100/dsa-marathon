# Palindrome Partitioning

**Problem:** Given a string `s`, partition it into every possible grouping of contiguous palindromic substrings, and return all such partitions.

**Links:** [NeetCode](https://neetcode.io/problems/palindrome-partitioning) · [LeetCode 131](https://leetcode.com/problems/palindrome-partitioning/)

---

## My Solution — Backtracking over cut positions

From start index `i`, try every end `j`: if `s[i..j]` is a palindrome (checked by the two-pointer `isPali`), cut there — append the piece, recurse from `j + 1`, pop. The base case at `i == len(s)` records the completed partition. Every string has up to 2ⁿ⁻¹ such palindromic-cut partitions, all enumerated.

| | |
|---|---|
| **Time** | O(n · 2ⁿ) — 2ⁿ⁻¹ partitions copied in O(n) at the leaves, plus O(n) palindrome scans along the way |
| **Space** | O(n) auxiliary — `part` buffer + recursion depth; output adds O(n · 2ⁿ) |

**Caveat:** `isPali(s, i, j)` re-derives from scratch, and the *same* substring gets re-checked at multiple branch points — the scan repeats work the recursion already did. It's still within the O(n · 2ⁿ) output bound, but a palindrome DP table makes every check O(1).

## Optimal Solution — Same backtracking + palindrome DP table

Precompute `is_pal[i][j]` bottom-up (`s[i] == s[j]` and either the span is length ≤ 2 or the inner span is a palindrome), then the backtracking loop consults the table instead of scanning:

| | |
|---|---|
| **Time** | O(n²) for the table + O(n · 2ⁿ) enumeration (output-dominated) |
| **Space** | O(n²) for the table + O(n) recursion; output adds O(n · 2ⁿ) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Backtracking + palindrome DP (optimal) | O(n² + n · 2ⁿ) | O(n²) | **Default answer** — O(1) checks; also the springboard for Palindrome Partitioning *II/IV* (min cuts / feasibility) |
| Backtracking + live two-pointer scan | O(n · 2ⁿ) | O(n) | Perfectly fine at n ≤ 16; simpler, no table |
| Memoized DFS over start indices | O(2ⁿ) states | O(2ⁿ) | Same enumeration, different shape; rarely cleaner |

**Interview answer:** “Backtrack over every cut: cut at `j` if `s[i..j]` is a palindrome, recurse from `j+1`. I'd precompute an n×n palindrome table so each check is O(1) — O(n²) setup, output-bound enumeration.”

## Edge Cases

- **Single char** → `[[s]]` (one piece).
- **All same char** (`"aaa"`) → 2ⁿ⁻¹ = 4 partitions: every split works since every substring is a palindrome.
- **Whole string is a palindrome** (`"abccba"`) → includes the single-piece partition `[[s]]`.
- **No multi-char palindromes** (`"abc"`) → only the all-singles partition `[[a],[b],[c]]`.
- **Empty string** (not in LC constraints, len ≥ 1) → `[[]]` — base case fires immediately.
- **Longest-necessary DP** → the table build order (i descending) guarantees `is_pal[i+1][j-1]` is ready before use.