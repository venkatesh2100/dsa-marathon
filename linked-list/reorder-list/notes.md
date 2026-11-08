# Reorder List

**Problem:** Rewrite `L0 → L1 → … → Ln-1` into `L0 → Ln-1 → L1 → Ln-2 → …` in place, returning nothing (LeetCode's "modify head in-place" contract).

**Links:** [NeetCode](https://neetcode.io/problems/reorder-linked-list) · [LeetCode 143](https://leetcode.com/problems/reorder-list/)

---

## My Solution — Split → reverse tail half → weave (already optimal)

Three passes, each a known primitive costing O(n):

1. **Split.** `slow` walks 1, `fast` walks 2 — but `fast` starts at `head.next`, deliberately. That off-by-one puts `slow` on the **last node of the first half** for *both* parities (`[1,2]` split as `1 | 2`; `[1,2,3]` as `1,2 | 3`). Cutting there gives a clean first half every time.
2. **Reverse** the second half with the standard three-pointer flip ([Reverse Linked List](../reverse-linked-list/notes.md)).
3. **Weave.** Two cursors, `first` and reversed `second`; each step splices one reversed-half node between the current `first` node and its `next` (two re-links, two holds). The loop is driven by `second` — legal because the first half is always the longer (or equal) piece, so when `second` runs dry the list already ends on the first half's leftovers, which is exactly where the middle belongs in odd lengths.

| | |
|---|---|
| **Time** | O(n) — three linear passes, constant work per node |
| **Space** | O(1) — pointer variables only; the output is the same node objects relinked |

**Caveat:** No asymptotic one; the danger is the two classic off-by-ones, and this code dodges both: starting `fast` at `head` instead of `head.next` puts `slow` mid-list and splits even lengths wrong; and driving the weave by `first` instead of `second` runs the shorter list straight into `None` and crashes on odd halves. Say the `head.next` choice out loud in an interview — it reads as insight, not luck.

## Optimal Solution — Same, Polished

Identical algorithm. Polish: the middle-finding names and comments mirror [Linked List Cycle](../linked-list-cycle/notes.md), the reversal is extracted to a `_reverse` helper (one tuple-assignment flip per node), and the weave uses `nxt_first`/`nxt_second` instead of `tmp1`/`tmp2` so the two holds aren't interchangeable-looking. Same **O(n) / O(1)**. It cannot be beaten: the transformation requires visiting every node (O(n) floor) and touching only links (O(1) space is its defining demand).

## Alternative — Materialize nodes, relink by index pattern

Walk once into a plain array/deque of node references, then relink straight down the pattern `L0, Ln-1, L1, Ln-2, …`. O(n) time, but **O(n) auxiliary space** — the same nodes, so still "in place" spirit-wise, and near-zero-risk to write. Reach for it when the three-pointer choreography slips your mind mid-interview; correctness is load-bearing on one index loop instead of a split/reverse/weave state machine.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Split → reverse → weave | **O(n)** | **O(1)** | **Default — my solution already is it**; the expected answer |
| Array/deque of nodes → relink | O(n) | O(n) | Rescue mode: simpler bookkeeping, extra memory |
| Recursion (weave from both ends) | O(n) | O(n) stack | Never — same stack trap as Reverse Linked List, zero payoff |

**Interview answer:** This is three primitives composed — fast/slow middle (with the `head.next` start stated deliberately), reverse-the-tail-half, alternate weave driven by the shorter side. O(n) time, O(1) space, same nodes relinked, nothing returned.

## Edge Cases

- **Empty list / single node** → guard returns immediately (the contract allows mutating nothing).
- **Two nodes** (`[1,2]`) → reorder is *unchanged* — smallest case that still exercises cut, half-reverse, and one weave step.
- **Odd length middle** (`[1,2,3]` → `[1,3,2]`, `[1,2,3,4,5]` → `[1,5,2,4,3]`) → the middle survives as the final node because the weave is driven by `second`.
- **Even length** (`[1,2,3,4]` → `[1,4,2,3]`) → the parity that breaks the `fast = head` variant of the split.
- **Duplicate values** (`[7,7,7,7]`) → verification must be by node identity, not values; the permutation oracle below checks object ids.
- **In-place object identity** → result chain's node ids equal the expected permuted order (`0, n-1, 1, n-2, …`), head object unchanged, no cycle/fork in the walk.
- **Return contract** → the method returns `None`, not the list (LeetCode-style mutation contract).
