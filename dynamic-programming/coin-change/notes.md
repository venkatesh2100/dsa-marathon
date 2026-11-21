# Coin Change

**Problem:** Given coins of different denominations and a total `amount`, return the fewest number of coins needed to make up that amount, or `-1` if it cannot be made.

**Links:** [NeetCode](https://neetcode.io/problems/coin-change) · [LeetCode 322](https://leetcode.com/problems/coin-change/)

---

## My Solution — Top-down Memoization (caching bug)

Recursively try every coin and memoize the result per remaining amount. **Bug:** `dp[a]` is written inside the coin loop, so a partially-computed value can be cached and returned on a revisit, producing wrong answers. The `return res` at the end uses the fully accumulated `res`, so the final answer for the top call can still be right, but any sub-problem pulled from the cache mid-computation is unreliable.

| | |
|---|---|
| **Time** | O(amount · C) |
| **Space** | O(amount) |

**Caveat:** `C` = number of coin denominations. The memo write belongs *after* the loop, not inside it.

## Optimal Solution — Bottom-up DP

`dp[a]` = fewest coins to make amount `a`. Seed `dp[0] = 0`, then `dp[a] = 1 + min(dp[a - c])` over every coin `c <= a`. Return `dp[amount]`, or `-1` if it stays infinite.

| | |
|---|---|
| **Time** | O(amount · C) |
| **Space** | O(amount) |

This is the standard optimal interview solution. O(amount · C) time is required because each amount considers every coin; O(amount) space is needed for the table.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Top-down memoization | O(amount · C) | O(amount) | Intuitive, but fix the cache-write placement |
| Bottom-up DP | **O(amount · C)** | **O(amount)** | **Default interview answer** |
| Greedy | — | — | Never — not always optimal (e.g. coins `[1, 3, 4]`, amount `6`) |

**Interview answer:** "Bottom-up DP: `dp[a]` is the fewest coins for amount `a`, built upward from `dp[0] = 0` using every coin `<= a`. Return `dp[amount]` or `-1` if unreachable."

## Edge Cases

- `amount = 0` → `0`
- Amount unreachable (e.g. `coins = [2]`, `amount = 3`) → `-1`
- Single coin that divides amount (e.g. `coins = [5]`, `amount = 15`) → `3`
- Coins larger than amount are simply skipped
- `coins = [1]`, any amount → `amount`
