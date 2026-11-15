# Generate Parentheses

**Problem:** Given `n` pairs of parentheses, generate all combinations of well-formed (balanced) parentheses.

**Links:** [NeetCode](https://neetcode.io/problems/generate-parentheses) · [LeetCode 22](https://leetcode.com/problems/generate-parentheses/)

---

## My Solution — Backtracking with open/close counters

Build the string one character at a time, tracking `o` (opens used) and `c` (closes used). Two legal moves from any state: append `"("` while `o < n`, append `")"` while `c < o`. When `o == c == n` the buffer is a complete balanced string — joined and recorded. The `c < o` rule *is* the validity condition: a prefix can never have more closes than opens, so every emitted string is well-formed and no post-filtering is needed.

| | |
|---|---|
| **Time** | O(4ⁿ / √n) — the n-th Catalan number of results, each of length 2n copied out |
| **Space** | O(n) auxiliary — buffer + recursion depth 2n; output adds O(n · Cₙ) |

**Caveat:** None — this is the canonical optimal. The result count is the Catalan number Cₙ = (2n choose n)/(n+1): 1, 2, 5, 14, 42 for n = 1..5, which grows ~4ⁿ/√n.

## Optimal Solution — Same, polished

Identical recursion — already optimal, since the output size is the lower bound. Polish: the invariant (`0 ≤ c ≤ o ≤ n`) stated up top.

| | |
|---|---|
| **Time** | O(4ⁿ / √n) |
| **Space** | O(n) auxiliary + output |

### Alternative — Closure/DP view

Every balanced string is `"(" + A + ")" + B` where A, B are balanced with total n−1 pairs — recursion on the *first* pair's interior/exterior. Same Catalan count; handy if asked for a non-backtracking framing.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Counter backtracking (optimal) | **O(4ⁿ/√n)** | **O(n)** aux | **Default answer** — two `if`s encode validity directly |
| Generate all 2²ⁿ strings, filter | O(n · 4ⁿ) | O(n) | Never — generates invalid prefixes wholesale |
| Closure-number DP | O(4ⁿ/√n) | O(4ⁿ/√n) | Same count; more machinery, no pruning advantage |

**Interview answer:** “Backtrack with counters: add `(` while opens remain, add `)` while closes trail opens; record at `o == c == n`. Only valid prefixes are ever built — O(Cₙ · n) ≈ O(4ⁿ/√n) time, O(n) depth.”

## Edge Cases

- **n = 1** → `["()"]`.
- **n = 0** (not in LC constraints, n ≥ 1) → `[[""]]` by the base case firing immediately — defensible.
- **All-open prefix** (`"((("…`) → `c < o` drives the closing run.
- **Deep nesting vs. flat** → both appear; e.g. n = 3 gives `"((()))"` and `"()()()"`.
- **No dead ends** → every branch reaches `o == c == n`; validity is structural, not filtered.