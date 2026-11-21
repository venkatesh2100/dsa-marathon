# Word Break

**Problem:** Given a string `s` and a dictionary of words `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Links:** [NeetCode](https://neetcode.io/problems/word-break) · [LeetCode 139](https://leetcode.com/problems/word-break/)

---

## My Solution — Top-down Memoization (DFS)

Recurse from index `i`: try every dictionary word that matches a prefix starting at `i`, and recurse on the remainder. Cache results per index so each suffix is computed once. Base case: reaching the end of the string means a valid segmentation.

| | |
|---|---|
| **Time** | O(n² · w) in the worst case (each of n indices tries up to w words, each slice is O(n)) |
| **Space** | O(n) for the memo and recursion stack |

**Caveat:** Iterating over all words at every index can repeat work; converting `wordDict` to a set and slicing `s[j:i]` avoids re-checking words that can't match. Recursion depth can reach `n`.

## Optimal Solution — Bottom-up DP

`dp[i]` is True iff the prefix `s[:i]` can be segmented. Seed `dp[0] = True` (empty prefix). For each end index `i`, try every split point `j < i`; if `dp[j]` is True and `s[j:i]` is in the dictionary, then `dp[i]` is True. Return `dp[n]`.

| | |
|---|---|
| **Time** | O(n²) (with O(1) set lookups; slicing is O(n) in the worst case, so O(n³) if slicing cost is counted) |
| **Space** | O(n) |

This is the standard optimal interview answer. Converting `wordDict` to a set gives O(1) membership checks, and the DP table avoids repeated subproblem work.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Top-down memoization | O(n² · w) | O(n) | Mirrors the recursion naturally |
| Bottom-up DP | **O(n²)** | **O(n)** | **Default interview answer** |
| Brute-force recursion | O(2ⁿ) | O(n) | Never — exponential without memoization |

**Interview answer:** "Use DP: `dp[i]` means `s[:i]` can be segmented. For each `i`, check all split points `j` where `dp[j]` is true and `s[j:i]` is a dictionary word. Store words in a set for O(1) lookups. O(n²) time, O(n) space."

## Edge Cases

- **Empty string** → depends on constraints (LeetCode guarantees `1 <= len(s)`)
- **Single character in dict** (`"a"`, `["a"]`) → `true`
- **Single character not in dict** (`"a"`, `["b"]`) → `false`
- **Whole string is one word** (`"leetcode"`, `["leetcode"]`) → `true`
- **No valid segmentation** (`"catsandog"`, `["cats","dog","sand","and","cat"]`) → `false`
- **Reusing words** (`"applepenapple"`, `["apple","pen"]`) → `true`
- **Overlapping word choices** (`"aaaaaaa"`, `["aaaa","aaa"]`) → `true`
