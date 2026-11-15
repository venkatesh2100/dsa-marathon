# Binary Tree Level Order Traversal

**Problem:** Given the root of a binary tree, return the values of its nodes level by level, left to right, as a list of lists.

**Links:** [NeetCode](https://neetcode.io/problems/level-order-traversal-of-a-binary-tree) · [LeetCode 102](https://leetcode.com/problems/binary-tree-level-order-traversal/)

---

## My Solution — BFS with a per-level inner loop

Standard level-order BFS: the outer loop drains the queue level by level, and the inner `for i in range(len(que))` snapshot processes exactly the nodes currently in the queue (one level), collecting them into `sub` and enqueuing their children for the next round.

| | |
|---|---|
| **Time** | O(n) — each node enqueued and dequeued once |
| **Space** | O(w) — queue holds the widest level `w` (up to ~n/2 in a full tree); output adds O(n) |

**Caveat:** The `if node:` guard inside the loop is dead code — the queue never contains `None` because children are appended only when truthy. Harmless, but it suggests the queue might hold `None`s, which is exactly the *other* level-order idiom (enqueue `None` placeholders); mixing the two mental models is where bugs come from.

## Optimal Solution — Same BFS, polished

Identical algorithm — it's already optimal, as each node must be visited once and grouped by level. Polish: snapshot `len(q)` with a throwaway `_` loop, no dead guards, direct `level.append(node.val)`.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(w) queue + O(n) output |

### Alternative — DFS with depth-indexed buckets

Recurse with a running depth: `if len(res) == depth: res.append([])`, then `res[depth].append(node.val)`. Same O(n) time; stack is O(h), but each level's list is appended left-to-right *and* the recursion visits in DFS order — output rows still come out in level order because `depth` indexes the right row. Useful when asked for level-order *without* a queue.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| BFS level loop (optimal) | **O(n)** | O(w) | **Default answer** — the canonical level-order idiom |
| DFS + depth index | O(n) | O(h) stack | No-queue follow-up; also trivially adapts to right-side view / zigzag |
| BFS with `None` markers | O(n) | O(n) | Never here — placeholders only pay off when you need level separators inline |

**Interview answer:** “BFS with a per-level snapshot of the queue length: inner loop processes exactly one level, appending its values and enqueuing children — O(n) time, O(w) space for the queue.”

## Edge Cases

- **Empty tree** → `[]` (early return).
- **Single node** → `[[1]]`.
- **Perfect tree** → each level a full row; queue peaks at ~n/2.
- **Left-only / right-only chain** → `n` rows of one element each.
- **Skewed levels (few nodes deep down)** → snapshot keeps partial rows correct.
- **Large values / duplicates** → grouping is positional, values irrelevant.