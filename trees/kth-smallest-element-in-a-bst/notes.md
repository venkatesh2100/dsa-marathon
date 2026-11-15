# Kth Smallest Element in a BST

**Problem:** Given the root of a BST and an integer `k`, return the `k`-th smallest value in the tree (1-indexed).

**Links:** [NeetCode](https://neetcode.io/problems/kth-smallest-integer-in-bst) · [LeetCode 230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

---

## My Solution — Collect all values, sort, index

BFS to gather every node's value into a list, sort it, and return index `k-1`.

| | |
|---|---|
| **Time** | O(n log n) — the sort dominates; the BFS itself is O(n) |
| **Space** | O(n) — the list holds every value |

**Caveat:** It ignores the BST property entirely — the same code would work on any binary tree, which is both its strength (robust) and its weakness (does avoidable work). Also `if node.val or node.val == 0:` is a two-clause workaround for `0` being falsy; a bare `arr.append(node.val)` needs no guard at all.

## Optimal Solution — Iterative in-order with early stop

In-order traversal of a BST visits values in ascending order *for free*. Walk left-spines with an explicit stack; each pop is the next-smallest value; return the `k`-th pop and stop — never touching the remaining n − k nodes.

| | |
|---|---|
| **Time** | O(h + k) — descend to the leftmost node (h), then pop k times; ≤ O(n) |
| **Space** | O(h) — stack holds one left-spine; O(log n) balanced, O(n) chain |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Iterative in-order, stop at k (optimal) | **O(h + k)** | **O(h)** | **Default answer** — uses the BST property, early exit |
| Recursive in-order with counter | O(h + k) | O(h) | Same idea recursively; needs a shared counter or generator |
| Collect + sort (my solution) | O(n log n) | O(n) | Fine as a first pass; say out loud that in-order beats it |
| Full in-order list then index | O(n) | O(n) | When k is unknown upfront or you need several k queries |

**Interview answer:** “In-order traversal is sorted for a BST; do it iteratively and return after popping k nodes — O(h + k) time, O(h) space. My first pass collected and sorted, which is O(n log n); the in-order version exploits the tree.”

## Edge Cases

- **Single node** → that value (k = 1).
- **k = 1** → leftmost node's value (minimum).
- **k = n** → rightmost node's value (maximum); the stack drains the whole tree.
- **Left-skewed chain** → stack grows to O(n) while descending; early stop if k is small.
- **Values including 0** → fine; the falsy-`0` guard in my version exists precisely for this.
- **Follow-up "frequent modification"** → augment nodes with subtree-size counts for O(h) queries; mention as the classic follow-up.