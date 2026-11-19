# Climbing Stairs

**Problem:** Given `n` stairs, you can climb 1 or 2 steps at a time. Return the number of distinct ways to reach the top (step `n`).

**Links:** [NeetCode](https://neetcode.io/problems/climbing-stairs) · [LeetCode 70](https://leetcode.com/problems/climbing-stairs/)

---

## My Solution — DP with an array

The number of ways to reach step `i` is the sum of the ways to reach steps `i - 1` and `i - 2`, because the last move was either a 1-step or a 2-step jump. That is the Fibonacci recurrence shifted by one.

`arr` starts as `[0, 1]` (`arr[0] = 0`, `arr[1] = 1`) and is filled with `arr[i] = arr[i - 1] + arr[i - 2]` up to index `n + 1`, then `arr[n + 1]` is returned. `n == 0` and `n == 1` are short-circuited to `1`.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

**Caveat:** The whole array is stored even though only the last two values are needed — hence the O(n) space. Growing the array to `n + 2` also means the answer sits at `arr[n + 1]`, one index past the natural `arr[n]`, which is easy to misread.

## Optimal Solution — Two rolling variables

At any point only `ways(i - 1)` and `ways(i - 2)` are needed, so keep them in two variables and roll forward. Seed `prev = curr = 1` (one way to stand at step 0, one way to reach step 1) and loop `i = 2 … n` updating `prev, curr = curr, prev + curr`. Return `curr`.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Array DP | O(n) | O(n) | Fine first answer, but stores more than needed |
| Rolling two variables | **O(n)** | **O(1)** | **Default interview answer** — same recurrence, constant space |
| Naive recursion | O(2ⁿ) | O(n) | Never — exponential without memoization |
| Matrix exponentiation | O(log n) | O(1) | Only if `n` is enormous and O(n) is too slow |

**Interview answer:** "It's Fibonacci: `ways(i) = ways(i-1) + ways(i-2)`. I can compute it with two rolling variables in O(n) time and O(1) space."

## Edge Cases

- `n = 0` → `1` way (do nothing).
- `n = 1` → `1` way.
- `n = 2` → `2` ways (`1+1`, `2`).
- `n = 3` → `3` ways (`1+1+1`, `1+2`, `2+1`).
- Large `n` → result is a Fibonacci number and fits Python's unbounded `int`.
