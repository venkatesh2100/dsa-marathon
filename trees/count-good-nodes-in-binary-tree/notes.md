# Count Good Nodes in Binary Tree

**Problem:** Count the "good" nodes — a node is good if, on the path from the root to it, no node has a strictly greater value (i.e., `node.val >= max(values along its root path)`).

**Links:** [NeetCode](https://neetcode.io/problems/count-good-nodes-in-binary-tree) · [LeetCode 1448](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

---

## My Solution — BFS carrying the path max

Level-order traversal where the queue holds `(node, max_so_far)` pairs: the running max of the path *to that node*. Each node is good iff `node.val >= rval`; children are enqueued with the updated max.

| | |
|---|---|
| **Time** | O(n) — each node processed once |
| **Space** | O(w) — queue holds one level of `(node, max)` tuples (up to ~n/2 in a full tree) |

**Caveat:** `if not root: return []` is the wrong return type — the method must return an `int` (an empty tree has 0 good nodes, so it should be `return 0`). Unreachable under LC's constraints (`>= 1` node), but it's a latent type bug: calling with `None` returns a list. Also, `(node, rval)` tuples double the queue's memory churn versus a plain node queue.

## Optimal Solution — Recursive DFS with running max

Pass the path max down as an argument: each node contributes `1` if `node.val >= mx`, then recurses with the updated max. No tuples, no queue, no dead branches.

| | |
|---|---|
| **Time** | O(n) — each node visited once |
| **Space** | O(h) — recursion stack; O(log n) balanced, O(n) worst-case chain |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| DFS with running max (optimal) | **O(n)** | **O(h)** | **Default answer** — minimal code, max lives on the call stack |
| BFS with `(node, max)` pairs | O(n) | O(w) | Fine; needed if you're already doing level-order for another requirement |
| Recheck the whole path per node | O(n · h) | O(h) | Never — recomputes ancestors at every node |

**Interview answer:** “DFS passing the max-so-far down: each node counts itself if `val >= max`, children get the updated max — O(n) time, O(h) space.”

## Edge Cases

- **Empty tree** → `0` (my version's `return []` is the type bug; correct answer is the integer 0).
- **Single node** → `1` (the root is always good).
- **Descending chain** (e.g., `5 → 3 → 1`) → only the root is good.
- **Ascending chain** → every node is good (each `>=` the smaller max above).
- **Ties count as good** — `>=` not `>`: a node equal to the path max is good (`[3,3]` → 2).
- **Negative values** → works; the max starts at `root.val`, so e.g. `[-1, 5, -2]` counts root and 5 only.