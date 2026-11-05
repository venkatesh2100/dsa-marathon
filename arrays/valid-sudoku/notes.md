# Valid Sudoku

**Problem:** Given a `9 × 9` Sudoku board, return `true` if every filled cell is valid — no digit `1`–`9` repeats in any row, column, or `3 × 3` sub-box. Empty cells are `"."`; the board does not need to be solvable.

**Links:** [NeetCode 36](https://neetcode.io/problems/valid-sudoku) · [LeetCode 36](https://leetcode.com/problems/valid-sudoku/)

---

## My Solution — Boolean Arrays per Row, Column, and Box

Keep nine "seen" flags per row, column, and box. For each filled cell, map the digit to index `0`–`8`, compute its box with `(r // 3) * 3 + c // 3`, and return `false` if that digit is already marked in any of the three groups. Otherwise mark it and continue.

| | |
|---|---|
| **Time** | O(81) = O(1) — one pass over the fixed `9 × 9` board |
| **Space** | O(243) = O(1) — 27 arrays of 9 booleans |

**Caveat:** This is already asymptotically optimal. The only improvement is the constant factor; the code uses 243 boolean slots where 27 integers (bitmasks) or 27 sets would also do.

## Optimal Solution — Bitmasks

Represent each row, column, and box as a 9-bit integer. Bit `d - 1` being set means digit `d` has been seen. Checking and marking become `mask & bit` and `mask |= bit`.

| | |
|---|---|
| **Time** | O(81) = O(1) |
| **Space** | O(27) = O(1) — three arrays of 9 machine-sized integers |

```python
bit = 1 << (int(board[r][c]) - 1)
box = (r // 3) * 3 + c // 3

if rows[r] & bit or cols[c] & bit or boxes[box] & bit:
    return False

rows[r] |= bit
cols[c] |= bit
boxes[box] |= bit
```

This is optimal: every cell must be inspected once, and the grid size is fixed. The bitmask version has the same complexity as the boolean version but uses about nine times less tracking memory and avoids allocating multi-dimensional lists.

## Alternative Approaches

- **Boolean arrays (my solution):** O(1) time, O(1) space. Clearest to explain and the safest default.
- **Bitmasks (optimal):** O(1) time, O(1) space. Tightest memory; a good follow-up if asked to reduce space.
- **Set of `(digit, row/col/box)` tuples:** O(1) time, O(1) space. Short and language-agnostic, but hashes tuples and is slower in practice.
- **Brute force:** For each cell, scan its entire row, column, and box. Also O(1) for a fixed board, but about 27 checks per cell — only useful for comparison.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Boolean arrays | **O(1)** | O(1) | **Default interview answer** — easiest to explain |
| Bitmasks | **O(1)** | O(1) | Asked to minimize memory, or comfortable with bit tricks |
| Seen-tuple set | O(1) | O(1) | Shortest code, slower constants |
| Brute force | O(1)* | O(1) | Never — only for comparison |

\* Technically constant because the board is fixed, but the constant is much larger.

**Interview answer:** Walk the board once. For each digit, track whether it has appeared in its row, column, and box using either 27 boolean arrays or 27 bitmasks. If it has appeared in any of the three, return `false`; otherwise mark it and continue. O(1) time and space because the board is always `9 × 9`.

## Edge Cases

- **All cells empty** → `true`; there are no duplicates.
- **Single filled cell** → `true`.
- **Duplicate in a row, column, or box** → `false`; the check stops early.
- **Same digit in different rows, columns, and boxes** → `true`; only the three groups matter.
- **Duplicate only inside a box** (different row and column) → `false`; the box index formula must catch it.
- **Cells near box boundaries** → `(r // 3) * 3 + c // 3` maps rows/columns `0–2` to box `0`, `3–5` to box `1`, and `6–8` to box `2` (and likewise across).
- **Fully solved valid board** → `true`.
- **Malformed input** (wrong size, invalid characters) → not handled; the constraints guarantee a `9 × 9` board of `"1"`–`"9"` and `"."`.
