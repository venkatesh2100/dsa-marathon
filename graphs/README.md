# Graphs

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Number of Islands](number-of-islands/) | BFS/DFS flood-fill, sink land in place | O(m · n) | O(min(m, n)) | Every unsunk `"1"` starts a flood-fill that sinks the whole island to `"0"`, so each island is counted exactly once; BFS queue avoids Python's recursion limit on huge islands |
| [Max Area of Island](max-area-of-island/) | BFS/DFS flood-fill, count cells per island | O(m · n) | O(min(m, n)) | Same sink-in-place flood-fill as Number of Islands, but track the max cell count instead of the island count; a DFS that *returns* area beats a `nonlocal` counter (no reset to forget) |
