# Dynamic Programming

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Climbing Stairs](climb-stairs/) | Two rolling variables | O(n) | O(1) | Fibonacci recurrence `ways(i) = ways(i-1) + ways(i-2)`; only the last two values are needed, so two variables replace the array |
