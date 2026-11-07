# Median of Two Sorted Arrays

**Problem:** Two separately sorted arrays (sizes `m`, `n`, total ≥ 1). Return the median of their merged values in O(log(m+n)); with `m + n` even the median is the mean of the two middle elements.

**Links:** [NeetCode](https://neetcode.io/problems/median-of-two-sorted-arrays) · [LeetCode 4](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---

## My Solution — Merge everything, sort, pick

Concatenate, sort the combined array, then read off `arr[n//2]` for odd totals and the mean of `arr[n//2 - 1]` and `arr[n//2]` for even totals. The `n == 0` guard returns `0` defensively.

| | |
|---|---|
| **Time** | O((m+n) log(m+n)) — dominated by `arr.sort()` |
| **Space** | O(m+n) — the merged copy |

**Why it's wasteful:** two straight answers were left on the table. The inputs are *already sorted*, so the sort re-solves a solved problem: a two-pointer merge should have cost O(m+n) with no log factor, and the problem statement demands better than even that — O(log(m+n)) via binary search.

## Optimal Solution — Binary search on the partition cut

The insight is that the median only needs the two **seam values around the cut**, not the merge. Fix the left partition's size at `half = (m + n + 1) // 2` and choose how many of those elements come from the smaller array — call it `i`; the larger array then contributes `j = half - i`. A cut is valid when the two boundary comparisons hold:

- `aL <= bR and bL <= aR` — nothing in the left partition exceeds anything in the right
- then the median is `max(aL, bL)` (odd total) or `(max(aL, bL) + min(aR, bR)) / 2` (even)

Whether the cut is valid is **monotone in `i`** (as `i` grows, `aL` and `bR` slide apart), so binary search `i` in `[0, min(m, n)]` — that's where the log comes from, and why the arrays are swapped so we always search the shorter one.

| | |
|---|---|
| **Time** | O(log min(m, n)) — the search space is partition sizes |
| **Space** | O(1) |

Mechanics that carry it:

- **`±inf` for out-of-range boundaries** (`i == 0` → `aL = -inf`; `i == m` → `aR = +inf`, same for `j` over `nums2`): real arrays always satisfy compares against infinities, so the logic needs no branches for empty partitions. Numbers *at the tip* of the index range, not inside the search.
- **`(total + 1) // 2`** instead of `total // 2`: for odd totals this puts the median element *on the left partition*, so `max(aL, bL)` alone is the answer and the odd/even branches stay tidy.
- **The `while True` is honest here:** a valid cut provably exists for sorted inputs, so unlike Template A/B loops this one returns from inside and needs no exit invariant.

This is neither of the first two templates — a third shape: the search space is a *derived quantity* (partition size), making it a cousin of Koko's "binary search on the answer."

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Merge + sort | O((m+n) log(m+n)) | O(m+n) | Quick prototype; never the final answer here |
| Two-pointer merge | O(m+n) | O(m+n) | Mentionable stepping stone — but still misses the O(log) bar |
| Partition binary search | **O(log(min(m, n)))** | **O(1)** | **The expected answer — LC 4 is *the* Hard of this topic** |

**Interview answer:** say "binary search, but on partition sizes, not values" up front — that framing is the difference between drowning and solving. One cut into each array, check the two seam inequalities, shift the cut, return seam values at parity.

## Edge Cases

- **Both parity branches** → `[1, 3] + [2]` → `2.0`; `[1, 2] + [3, 4]` → `2.5`.
- **One array empty** (`m + n ≥ 1` guarantees at most one) → reduces to the median of the other; `±inf` boundaries make the cut validate immediately.
- **Both empty** → excluded by constraints; defensively your merge-sort returns `0`, while the partition version returns `nan` (`-inf + inf`) — do not call it here.
- **All-equal arrays** (`[0, 0] + [0, 0]` → `0.0`) → every cut validates; binary search lands somewhere valid immediately.
- **Interleaved / negative / earlier-array-larger values** (`[7, 8, 9, 10] + [1..4]`) → order inside each array is what matters, cross-array order is irrelevant.
- **Unequal sizes** (e.g. 5 vs 3) → swapping ensures the binary search runs on the shorter array; `j = half - i` stays in range automatically.
- **Integer vs float returns** → odd totals may return an int (`arr[3] == 2` from `[1,2,2,3]`), even always produces a float; LeetCode accepts both, and the tests treat them as equal Python numbers.
- **Duplicate-heavy arrays** (`[1, 2, 2, 3] + [2, 2, 2]` → `2.0`) → ties validate under `<=`, never `<`; loose comparisons are what keep equal crossings valid.
- **Avoid floats when precision matters** → seam inputs are ints; the only float op is the final `/2`, no precision loss for sums that fit in a machine int.
