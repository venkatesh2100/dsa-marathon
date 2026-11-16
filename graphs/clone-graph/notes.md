# Clone Graph

**Problem:** Given a reference node of a connected undirected graph (each node holds `val` and a `neighbors` list), return a **deep copy** — entirely new node objects with the same structure. The input graph may contain cycles.

**Links:** [NeetCode](https://neetcode.io/problems/clone-graph) · [LeetCode 133](https://leetcode.com/problems/clone-graph/)

---

## My Solution — BFS with an original→clone hash map

Seed the map with a clone of the start node and BFS. When dequeuing `cur`, look at each neighbor: if it hasn't been cloned yet, clone it and enqueue the *original* for later processing; either way, append the clone of `nei` to the clone of `cur`. When the queue drains, every node has been cloned once and every edge wired once, so `hmap[node]` is the deep copy.

The key insight: `hmap` is doing double duty — it's both the clone registry **and** the visited set. That's why cycles don't loop forever (a node already in the map is never re-enqueued) and why you can't drop the map for a plain visited set: the registry *is* the output being built.

| | |
|---|---|
| **Time** | O(V + E) — each node is enqueued once; each edge is scanned once from each endpoint |
| **Space** | O(V) — the map (one entry per node, unavoidable since it holds the copy) + the queue |

## Optimal Solution — Same BFS, cleaned up

This *is* the standard optimal — the map is mandatory (it stores the deep copy), and one traversal is the minimum. The optimal file is the same algorithm with an empty-graph guard, explicit comment on the double-duty map, and the note that wiring runs for fresh *and* already-cloned neighbors. The recursive DFS form is the only real alternative:

```python
clones = {}
def dfs(cur):
    if cur in clones:
        return clones[cur]
    copy = Node(cur.val)
    clones[cur] = copy                      # register BEFORE recursing — breaks cycles
    copy.neighbors = [dfs(nei) for nei in cur.neighbors]
    return copy
return dfs(node)
```

Registering the clone before the neighbor recursion is what stops infinite loops on cycles — registering after would stack-overflow on `[1↔2]`.

| | |
|---|---|
| **Time** | O(V + E) |
| **Space** | O(V) — map + recursion stack |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| BFS + map (my solution ≈ optimal) | O(V + E) | O(V) | **Default answer** — iterative, no stack-depth worries |
| Recursive DFS + map | O(V + E) | O(V) stack | Slightly less code; fine here (LeetCode caps the graph at 100 nodes) |
| Traversal without a map | — | — | Impossible — cycles require a visited check, and the clone registry is the natural one |

**Interview answer:** "BFS or DFS with a hash map from original→clone. The map doubles as the visited set — clone each node once, wire edges from the clone side. O(V+E) time, O(V) space."

## Edge Cases

- **`node = None`** → return `None` (handled up front).
- **Single node, no neighbors** (`adjList = [[]]`) → one clone, empty neighbors.
- **Two-node cycle** (`[[2],[1]]`) → the map check stops the loop; edges wire in both directions.
- **Self-loops / repeated edges** → excluded by LeetCode constraints (`val` unique, no dup edges).
- **Disconnected graph** → not a LeetCode input (graph is guaranteed connected); a map-seeded-per-component loop would be needed.
