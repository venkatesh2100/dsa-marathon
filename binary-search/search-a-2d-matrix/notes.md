# Search a 2D Matrix

**Problem:** Given an `m × n` matrix where every row is sorted ascending and the first integer of each row is greater than the last integer of the previous row, return `True` if `target` exists in the matrix, else `False`. Must run in O(log(m·n)) time.

**Links:** [NeetCode](https://neetcode.io/problems/search-2d-matrix) · [LeetCode 74](https://leetcode.com/problems/search-a-2d-matrix/)

---

## My Solution — Flattened Single-Pass Binary Search

Treat the matrix as one virtual sorted array of length `m · n` and binary search it. Convert the flat midpoint back to 2D coordinates with the row-major map `row = mid // n`, `col = mid % n`, then compare normally.

This is the cleanest possible formulation of the problem, and the pointer updates are the correct ones this time: `r = mid - 1` / `l = mid + 1` discard the entire half including `mid`, so the window truly halves each iteration.

| | |
|---|---|
| **Time** | O(log(m·n)) |
| **Space** | O(1) |

**Why flattening is legal:** the problem's row-chain property (first of row `i` > last of row `i-1`) means reading the matrix row-by-row yields one globally sorted sequence. It is *not* legal if rows are merely individually sorted without the chain (that is LeetCode 240, a different problem).

**On the commented-out bounds check:** `mid` always satisfies `l <= mid <= r` with both ends inside `[0, m·n - 1]`, so `row < m` and `col < n` are guaranteed — the guard is dead code, safe to delete.

**Caveat:** `len(matrix[0])` raises on an empty matrix. Constraints guarantee `m, n ≥ 1`, so it passes as-is; a `if not matrix or not matrix[0]: return False` guard makes it defensive.

## Optimal Solution — Same Approach, Polished

Identical algorithm with two ergonomic touches: `divmod`-style row/col mapping through a single `val` local, and `(l + r) // 2` (the overflow-safe `l + (r - l) // 2` habit does no harm but is unnecessary in Python).

| | |
|---|---|
| **Time** | O(log(m·n)) |
| **Space** | O(1) |

## Alternative Approaches

- **Two binary searches:** binary search the right row first (`O(log m)`), then binary search within it (`O(log n)`). Same overall bound, more code, easy to fumble the row-selection comparison.
- **Staircase walk:** start at the top-right corner; move left if the value is too big, down if too small. `O(m + n)` — the go-to for LeetCode 240, but too slow here.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Flattened single-pass BS | **O(log(m·n))** | **O(1)** | **Default — my solution already is it** |
| Two binary searches | O(log m + log n) | O(1) | Equivalent bound; fine alternative, more code |
| Staircase walk | O(m + n) | O(1) | Only for the LC 240 variant (no row-chain property) |
| Brute force scan | O(m·n) | O(1) | Never |

**Interview answer:** Because the rows chain into one globally sorted sequence, binary search the virtual flat array of length `m·n`; map `mid` to `(row, col) = (mid // n, mid % n)` on the fly. Half the candidates die every step, so O(log(m·n)) time, O(1) space.

## Edge Cases

- **Single element hit** (`[[5]]`, target `5`) → `True`; miss (`[[5]]`, target `1`) → `False`.
- **Single row** (`[[1, 3, 5, 7]]`, target `5`) → degenerates to plain 1D binary search.
- **Single column** (`[[1], [3], [5]]`, target `3`) → `True`; flat map gives `row = mid`, `col = 0`.
- **Target strictly between rows** (`[[1, 3], [5, 7]]`, target `4`) → `False`. The classic trap for "search row by row" logic; the flat approach handles it for free.
- **Target smaller / larger than everything** → loop runs `log` steps and returns `False`.
- **Target at first or last cell** → both boundary indices reachable.
- **Empty matrix** (`[]`) → forbidden by constraints; the current code would raise `IndexError` on `matrix[0]` — add a guard if you want it bulletproof.
