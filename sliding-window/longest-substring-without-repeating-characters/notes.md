# Longest Substring Without Repeating Characters

**Problem:** Return the length of the longest **substring** (contiguous, not subsequence) of `s` containing only distinct characters.

**Links:** [NeetCode](https://neetcode.io/problems/longest-substring-without-repeating-characters) · [LeetCode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## My Solution — Shrink-on-duplicate window

The window `[l..r]` carries one invariant: **it never contains a duplicate**. Advance `r`; if `s[r]` is already in the set, pop characters off the left until the previous occurrence of `s[r]` itself has been evicted, then add `s[r]` and record the window length `r - l + 1`. Because the window only ever grows rightward, `res` is monotone — recorded values never need re-watching.

| | |
|---|---|
| **Time** | O(n) — despite the nested loops |
| **Space** | O(min(n, Σ)), Σ = alphabet size (effectively O(1) for ASCII inputs) |

**Caveat:** No asymptotic one — but the *amortized argument is the interview moment here*. Each character is added to the set at most once and removed at most once, so the two loops together touch the set ≤ 2n times. Say that out loud; "nested loop = O(n²)" is the reflex this problem is designed to test. Style nits: the `if s[r] in uq:` wrapper duplicates its inner `while`'s first check — the `while` alone is equivalent (it simply never spins when there's no duplicate).

## Optimal Solution — Same, Polished

Identical algorithm: the polish collapses `if + while` into a single `while`, renames `uq` → `seen`, and swaps the manual outer `while` for `for r in range(len(s))`. Same **O(n) / O(min(n, Σ))**. No faster exact algorithm exists — every character must be read.

## Alternative — Jump-pointer window (different maintenance, same O(n))

Keep `last[ch]` = most recent index of each char. On a duplicate, instead of looping pops, jump `l = last[ch] + 1` directly. Same complexity with fewer container operations, but **there's a trap the pop-loop cannot have**: the jump must fire only when `last[ch] >= l` — otherwise an old, already-evicted duplicate drags `l` *backward*, splitting the window invariant. `"abba"` is the canonical regression case: without the guard, `l` snaps back to `last['a'] + 1 = 1` and wrongly reports `"bba"` inside a window that was already clean. The pop-loop version is self-correcting — eviction physically removes bookkeeping — at the cost of the (still-linear) inner loop.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Pop-on-duplicate window | **O(n)** | **O(min(n, Σ))** | **Default — my solution already is it**; self-correcting, no guard needed |
| Jump-pointer window | O(n) | O(min(n, Σ)) | Marginally leaner ops; must carry the `last[ch] >= l` guard |
| Brute force (extend from every start) | O(n²) | O(min(n, Σ)) | Never |

**Interview answer:** sliding window + set, pop from the left until the window is legal again; defend O(n) with "each index touches the set at most twice." If asked for O(1) space nuances, name the jump variant and its regression guard.

## Edge Cases

- **Empty string** → `0` (loop never runs; `res` initialized to 0).
- **Single char** (`"a"`) → `1`.
- **All identical** (`"bbbbb"` → `1`) → every step shrinks the window fully; exercises the not-quadratic claim hardest.
- **`"pwwkew"` → 3** → the longest window is `"wke"`; `"pwke"` is a *subsequence* — the exact misread the statement warns about.
- **`"dvdf"` / `"dvdfv"` → 3** → window must evict through the previous occurrence; a later duplicate (`v` in `dvdfv`) pushes the left edge over an already-shrunk region.
- **`"abba"` → 2** (`"ba"`) → the regression trap for the jump-pointer variant; the pop-loop handles it for free.
- **`"tmmzuxt"` → 5** (`"mzuxt"`) → the final `t` repeats the *evicted* index-0 `t`: bookkeeping about chars that already left the window must not leak back in — poisons naive bookkeeping-based variants, they need the `>= l` guard; pop-loop correct by construction.
- **Everything is fair game as a character** → spaces, digits, symbols count (`"a b a"` → 3); charset bound Σ covers all of them, and O(min(n, Σ)) stays ≍ O(1) for ASCII test data.
