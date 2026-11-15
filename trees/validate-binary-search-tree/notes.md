# Validate Binary Search Tree

**Problem:** Return `True` if the binary tree is a valid BST — every node's left subtree contains only values strictly less than it, and every right subtree only values strictly greater (checked *across levels*, not just parent-child).

**Links:** [NeetCode](https://neetcode.io/problems/validate-binary-search-tree) · [LeetCode 98](https://leetcode.com/problems/validate-binary-search-tree/)

---

## My Solution — BFS with (node, low, high) bounds

Traverse level-order carrying each node's legal value interval: a node passes iff `low < node.val < high`. The left child inherits `(low, node.val)`, the right child `(node.val, high)` — so a grandchild is checked against *all* its ancestors' bounds, not just its parent's.

| | |
|---|---|
| **Time** | O(n) — each node checked once |
| **Space** | O(w) — queue holds one level of `(node, low, high)` triples (up to ~n/2 in a full tree) |

**Caveat:** No asymptotic issue, but each queue entry is a 3-tuple — constant-factor heavier than a node-only queue. And the local check `low < val < high` is *necessary but not sufficient* without the inherited bounds: only checking `left.val < node.val < right.val` misses cases like a left-grandchild greater than an ancestor (e.g., `10 → 15 → 6`, where 6 is legally < 15 but must also be < 10).

## Optimal Solution — Recursive DFS with bounds

Same bound-inheritance idea on the call stack instead of the queue — cleaner and O(h) space:

```python
def valid(node, low, high):
    if not node: return True
    if not (low < node.val < high): return False
    return valid(node.left, low, node.val) and valid(node.right, node.val, high)
```

The `and` short-circuits after the first violation. Strict inequalities are load-bearing: duplicates make a BST invalid.

| | |
|---|---|
| **Time** | O(n) — each node visited once |
| **Space** | O(h) — recursion stack; O(log n) balanced, O(n) chain |

### Alternative — In-order traversal

An in-order walk of a valid BST is *strictly increasing*; track the previous value and fail on any non-increase. Same O(n)/O(h). Elegant, and it's the natural follow-up if asked for another method.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| DFS with bounds (optimal) | **O(n)** | **O(h)** | **Default answer** — minimal, short-circuits |
| BFS with bounds (my solution) | O(n) | O(w) | Fine; useful if you're already doing level-order work |
| In-order increasing check | O(n) | O(h) | Great alternative; iterate with an explicit stack if recursion is a concern |
| Parent-only local check | O(n) | O(1) | Never — misses cross-level violations |

**Interview answer:** “Pass bounds down: a node is valid iff `low < val < high`, left child gets `(low, node.val)`, right child `(node.val, high)` — O(n) time, O(h) space. Strict inequality, so no duplicates.”

## Edge Cases

- **Empty tree** → `True` (vacuously valid).
- **Single node** → `True`.
- **Duplicate values anywhere** (`[2,2,2]`) → `False` — strict `<` forbids equality.
- **Violation two levels down** (`[5,4,6,None,None,3,7]`, where 3 < 5) → `False` — the case the parent-only check misses.
- **Left-grandchild greater than an ancestor** (`[10,5,15,None,None,6,20]`, 6 < 15 but 6 must be > 10) → `False`.
- **All negative / mixed values** → bounds start at ±inf, so no value-range assumption.
- **Skewed chain** → recursion/queue both O(n) deep on a chain.