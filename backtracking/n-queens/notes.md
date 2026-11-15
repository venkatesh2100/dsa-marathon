# N-Queens

**Problem:** Place `n` queens on an `n × n` board so no two attack each other (no shared row, column, or diagonal); return **all** distinct boards as lists of strings.

**Links:** [NeetCode](https://neetcode.io/problems/n-queens) · [LeetCode 51](https://leetcode.com/problems/n-queens/)

---

## My Solution — Row-by-row backtracking with occupancy sets

Recurse one row at a time — a queen per row eliminates row conflicts *by construction*. For each column, reject the square if its column, anti-diagonal (`row + col`), or main diagonal (`row − col`) is already occupied (tracked in sets); otherwise place the queen, recurse to the next row, and undo everything on backtrack. At `row == n` the board is a valid solution, converted row-by-row to strings.

| | |
|---|---|
| **Time** | O(n!) upper bound — one queen per row and column prunes to column permutations; diagonals cut further. Each found solution adds O(n²) to copy |
| **Space** | O(n) — recursion depth n + three sets; output adds O(n² · #solutions) |

**Caveat:** `rowset` is dead code — `backtracking(row)` is entered once per row value and every candidate within a call shares that row, so a row conflict is impossible; the set always holds exactly `{row}`. The `copy = chessboard[:]` at the leaf is also unnecessary — the rows are only read and joined, so iterating `chessboard` directly is equivalent. Neither affects correctness, just noise.

## Optimal Solution — Same, polished

Same row-by-row backtracking with the dead `rowset` dropped, the leaf copy collapsed to a single comprehension, and the diagonal keys commented (`r + c` anti, `r − c` main — both are constant along their diagonal).

| | |
|---|---|
| **Time** | O(n!) upper bound |
| **Space** | O(n) auxiliary + output |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Row recursion + 3 sets (optimal) | O(n!) | O(n) | **Default answer** — the standard formulation |
| Row recursion + bitmask columns/diags | O(n!) | O(n) | Follow-up "no sets / faster constants"; same search, ints instead of sets |
| Full n² scan per placement | O(n² · n!) | O(n²) | Never — re-validates what the sets remember |

**Interview answer:** “Place one queen per row; track occupied columns and the two diagonal families (`r+c`, `r−c`) in sets; backtrack and undo. O(n!)-ish search, O(n) space.”

## Edge Cases

- **n = 1** → `[["Q"]]`.
- **n = 2, n = 3** → `[]` — no arrangement exists; the search exhausts every column.
- **n = 4** → exactly 2 solutions (mirror images).
- **Diagonal collision shapes** → `r + c` catches anti-diagonals (↗), `r − c` catches main diagonals (↘); both constant along their line.
- **Undo symmetry** → every `add` has a matching `remove`, so partial boards never leak between branches.
- **Large n** → solution count grows superfast (n=8: 92); enumeration is inherently exponential.