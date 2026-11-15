# Same Tree

**Problem:** Given the roots of two binary trees, return `True` if they are structurally identical and the nodes have the same values, else `False`.

**Links:** [NeetCode](https://neetcode.io/problems/same-binary-tree) · [LeetCode 100](https://leetcode.com/problems/same-tree/)

---

## My Solution — Parallel BFS with a level loop

Walk both trees level-by-level with two queues, pairing nodes in lockstep. `None` children are enqueued too, so *shape* is compared, not just values: two `None`s match (`continue`), a `None` paired with a real node or a value mismatch aborts with `False`.

| | |
|---|---|
| **Time** | O(n) — each node of the smaller-shaped tree is paired once; mismatch aborts early |
| **Space** | O(w) — each queue holds one level's worth of nodes (including `None` slots), up to ~n/2 in a full tree |

**Caveat:** Enqueueing `None` children bloats the queue with placeholder slots (up to ~2n entries across the whole run). The `while que1 and que2` guard plus per-level `for` is also more moving parts than needed — a single `while que1` suffices since both queues always have identical lengths. On a skewed chain, both BFS variants hold O(n) in the queues.

## Optimal Solution — Recursive DFS

Three-line recursion: two `None`s match; one `None` or a value mismatch fails; otherwise both subtrees must match.

```python
if not p and not q: return True
if not p or not q or p.val != q.val: return False
return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

The `and` short-circuits — the right subtree isn't touched once the left says "different."

| | |
|---|---|
| **Time** | O(n) — each node pair compared once |
| **Space** | O(h) — recursion stack; O(log n) balanced, O(n) worst-case chain |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Recursive DFS | **O(n)** | **O(h)** | **Default answer** — minimal code, O(h) stack |
| Iterative DFS (explicit stack of pairs) | O(n) | O(h) | Same profile as recursion, no stack-overflow risk |
| Parallel BFS (my solution) | O(n) | O(w) ≤ O(n) | Fine; heavier queue (with `None` slots) and more bookkeeping |

**Interview answer:** “Recursion: match when both `None`, fail when one is `None` or values differ, else recurse on both subtrees — O(n) time, O(h) space.”

## Edge Cases

- **Both empty** → `True`.
- **One empty, one not** → `False` (one-node mismatch caught immediately).
- **Same values, different shape** (`[1,2]` vs `[1,None,2]`) → `False` — this is what distinguishing real nodes from enqueued `None`s buys you.
- **Different values, same shape** → `False`.
- **Deep skew** → recursion O(n) stack; BFS queues also O(n) on a chain.
- **Large identical trees** → full traversal, `True`.