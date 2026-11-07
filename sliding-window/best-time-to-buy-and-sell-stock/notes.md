# Best Time to Buy and Sell Stock

**Problem:** Given daily prices and one buy-before-sell opportunity, return the maximum profit achievable (0 if no profitable trade exists).

**Links:** [NeetCode](https://neetcode.io/problems/buy-and-sell-stock) · [LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

---

## My Solution — One pass with a running min

Track the cheapest price seen so far (`buy`) and the best profit so far (`res`). Each day: update `buy = min(buy, p)` (today as buy candidate), then `res = max(res, abs(p - buy))` (today as sell day).

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

**Ordering detail doing real work:** the min-update happens *before* the profit check, so a buy and a "sell" can land on the same day — profit 0, harmless, and the invariant `p >= buy` is guaranteed the moment it's used. Two loose ends: `abs()` is a tautology (never fires, since the update ran first — it quietly signals intent but hides why the value can't be negative), and the comment `# print(p,mini)` references a variable that got renamed to `buy`. Also — third time in a row the first attempt is already optimal (after [Koko](../binary-search/koko-eating-bananas/notes.md) and [Search-in-Rotated](../binary-search/search-in-rotated-sorted-array/notes.md)); O(n) is the floor here, every price must be read.

## Optimal Solution — Same, Polished

Identical one-pass. Polish: `float("inf")` seed (no reliance on `prices[0]` — survives an empty list, though constraints forbid it), `profit` instead of `res`, the `abs()` tautology dropped since the min-update already guarantees `price - cheapest >= 0`. Same **O(n) / O(1)**.

## Why This Counts as Sliding Window — and the Competing Mental Model

The window framing: the answer is the max of `prices[r] - prices[l]` subject to `l <= r`; equivalently, max over all pairs. A window over `[l..r]` where `l` only ever moves right — but never needs to move back — because when `prices[l] > prices[r]`, any window starting later on the left pointer is dominated: reset `l = r` is safe. Same complexity; the running-min formulation is just the window's stationary fixed point.

The backwards variant is worth naming too: scan right-to-left tracking `max_price_so_far`, profit = `max_so_far - price`. Symmetric, same O(n)/O(1).

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| One-pass running min (my solution) | **O(n)** | **O(1)** | **Default — already optimal; polish off the abs/comment** |
| Sliding-window reset (`l = r` when it beats best) | O(n) | O(1) | Same honestly — if the window framing clicks better |
| Suffix pass (max seen, scan right-to-left) | O(n) | O(1) | Symmetry exercise; no practical edge |
| Brute force all pairs | O(n²) | O(1) | Never — only as the springboard explanation |

**Interview answer:** "Cheapest so far is the best buy; every day ask 'sell today?'" — `profit = max(profit, p - min_so_far)`. O(n), O(1); watch out that you don't also need to *report which days* — that's why `res` is the only state needed over `(buy_day, sell_day)` indices.

## Edge Cases

- **Single price** (`[1]`) → no trade possible → `0` (loop runs once, profit vs itself is 0).
- **Strictly decreasing** (`[7, 6, 4, 3, 1]`) → no profitable day → `0`; `min` keeps chasing the floor.
- **Strictly increasing** (`[1, 2, 3, 4, 5]`) → buy on day 0, sell on the last → `4`.
- **All equal** (`[10, 10, 10]`) → `0`.
- **Dip after a peak** (`[2, 4, 1, 7]`) → `6` (buy 1, sell 7), *not* `2` — the trap for anyone tracking "max seen so far" without resetting profit when a new min appears.
- **Empty input** → constraints require `n ≥ 1`; your version would `IndexError` on `prices[0]` — the `inf` seed version returns `0` gracefully.
- **No integer subtlety back home** → `prices` ints, `res` int; in C/Java a large-min blend can't overflow here since `abs` guards nothing and values stay within `prices` range.
