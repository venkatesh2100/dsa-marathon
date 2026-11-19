# Min Cost Climbing Stairs

**Problem:** Given an array `cost` where `cost[i]` is the cost to step on the ith step, find the minimum cost to reach the top of the staircase (step `len(cost)`). You may start at step 0 or step 1, and from step `i` you can move to step `i+1` or `i+2`.

**Links:** [NeetCode](https://neetcode.io/problems/min-cost-climbing-stairs) · [LeetCode 746](https://leetcode.com/problems/min-cost-climbing-stairs/)

---

## My Solution — DFS with memoization

We recursively explore two choices from each position `i`: go to `i+1` or `i+2`. The recursion returns the minimum cost to reach beyond the last step. To avoid exponential recomputation, we memoize results in `dp[i]`, which stores the minimum cost starting from step `i`.

- Base case: if `i` is beyond the last step, return `0`.
- If `dp[i]` is already computed, return it.
- Otherwise, compute `cost[i] + min(dfs(i+1), dfs(i+2))`, store in `dp[i]`, and return it.

| | |
|---|---|
| **Time** | O(n) — each index is computed once |
| **Space** | O(n) — recursion stack + memo table |

**Caveat:** The recursion depth can reach `n` in the worst case (e.g., when the optimal path is to take 1-step moves), which might hit recursion limits in some environments. Python’s default recursion limit is ~1000, so for very large `n` you’d need to increase the limit or switch to an iterative approach.

## Optimal Solution — Iterative DP with O(1) space

The recurrence `dp[i] = min(dp[i-1], dp[i-2]) + cost[i-1]` for `i >= 2` (with `dp[0] = 0`, `dp[1] = cost[0]`) lets us compute the answer iteratively while keeping only the two most recent values. We iterate from `i = 2` to `len(cost)` (the top step), updating two variables that represent `dp[i-2]` and `dp[i-1]`. The final answer is `dp[len(cost)]`, which is stored in `b` after the loop.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

**Why it’s optimal:** The recurrence captures the two possible ways to reach the top (from one step back or two steps back). Keeping only the two previous costs eliminates the need for an array and reduces space to constant, which is the expected optimal solution for interview settings.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| DFS + memoization | O(n) | O(n) | Good for clarity; easy to reason about recursion, but uses extra space |
| Iterative DP (two vars) | **O(n)** | **O(1)** | **Default interview answer** — same complexity, constant space, no recursion depth concerns |

**Interview answer:** "I can solve this with a simple DP recurrence: the cost to reach the top from step `i` is the cost of step `i` plus the minimum of the costs to reach `i+1` or `i+2`. I’ll compute it iteratively with two variables to get O(1) space."

## Edge Cases

- **Empty `cost`** → Not a valid LeetCode input (`n ≥ 1`), but both implementations return `0`.
- **Single element** (`[10]`) → Start at step 0 or 1, min cost is `0` (just step over).
- **Two elements** (`[1, 100]`) → Best path is start at step 0, take 1 step to the top → cost `10`.
- **Large `n`** → Iterative solution handles it safely; recursive version may need increased recursion limit.
- **Costs with zeros** → Works fine; zero-cost steps don’t affect the recurrence.

**Interview tip:** Mention that you could also start from the top (reverse DP) or use a bottom‑up approach; the key is the same recurrence.