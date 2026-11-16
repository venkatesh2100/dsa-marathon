# Graphs

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Number of Islands](number-of-islands/) | BFS/DFS flood-fill, sink land in place | O(m · n) | O(min(m, n)) | Every unsunk `"1"` starts a flood-fill that sinks the whole island to `"0"`, so each island is counted exactly once; BFS queue avoids Python's recursion limit on huge islands |
