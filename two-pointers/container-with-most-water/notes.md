# Container With Most Water

**Problem:** Given `heights`, where `heights[i]` is the height of a vertical line drawn at index `i`, pick two lines that together with the x-axis hold the most water. Return that maximum area: `min(heights[i], heights[j]) * (j - i)`.

**Links:** [NeetCode 11](https://neetcode.io/problems/max-water-container) · [LeetCode 11](https://leetcode.com/problems/container-with-most-water/)

---

## My Solution — Two Pointers (incorrect)

Same skeleton as the optimal two-pointer sweep: shrink the window from both ends and keep a running maximum, updating `res` after each move.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

⚠️ **This solution returns wrong answers** — e.g. `56` instead of `49` on LeetCode's `[1, 8, 6, 2, 5, 4, 8, 3, 7]`.

The bugs:

1. **Missing `min`.** The water level is `min(heights[l], heights[r])`, but the code multiplies by `heights[l]` (after the move) or `heights[r]` alone. On the example above it computes `8 × 7 = 56` although the water is capped at `7`.
2. **Wrong move order.** The area is computed *after* moving a pointer, so the current `(l, r)` pair is never measured. The pair being discarded is often the maximum candidate — in `[3, 1, 4, 2]` the pair `(0, 2)` has area `6`, but the code returns `4`.
3. **Wrong width in the `else` branch.** `heights[r] * (r - 1)` uses width `r - 1`; it must be `r - l`. It only coincides while `l = 0`, and it also ignores that the pair height is a `min`.
4. **Debug leftover.** `print(res)` runs on every iteration.

Caveat: the two-pointer idea itself is right — only the measurement and move order need fixing.

## Optimal Solution — Two Pointers, Measure Then Shrink

Start with the widest container and record its area. Moving the pointer at the **shorter** wall is the only safe discard: any other pair that includes that wall has less width and cannot be taller, so its best possible area was just recorded. Moving the taller wall can never help — the height stays capped by the shorter wall while the width shrinks.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

```python
while left < right:
    area = min(heights[left], heights[right]) * (right - left)
    best = max(best, area)

    if heights[left] < heights[right]:
        left += 1
    else:
        right -= 1
```

This is optimal: a single pass with constant memory. Each step permanently discards one wall whose best possible container is already accounted for, and there is no sublinear way to answer since every wall may be the limiting one.

## Alternative Approaches

- **Two pointers (optimal):** O(n) time, O(1) space. The standard interview answer.
- **Brute force:** O(n²) time, O(1) space. Check every pair — useful as a testing oracle, never as an answer.
- **Divide and conquer / other ideas:** no known benefit here; the greedy discard makes two pointers the natural optimum.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Two pointers, measure then move | **O(n)** | **O(1)** | **Default interview answer** |
| My attempt (move then measure) | O(n) | O(1) | ❌ Incorrect — needs the fixes above |
| Brute force | O(n²) | O(1) | Never — only as a testing oracle |

**Interview answer:** Keep two pointers at the ends. Record `min(heights[l], heights[r]) * (r - l)` for the current pair, then move the pointer at the shorter wall inward. O(n) time, O(1) space, and the discard argument proves no better pair is lost.

## Edge Cases

- **Two elements** (`[1, 1]`) → `1`; the smallest input allowed by LeetCode's constraints (`n ≥ 2`).
- **Maximum at the ends** (`[4, 3, 2, 1, 4]`) → `16`.
- **Peak inside** (`[2, 3, 4, 5, 18, 17, 6]`) → `17` (indices 4 and 5).
- **All equal** (`[5, 5, 5, 5]`) → `15`; the widest pair wins.
- **Monotonic arrays** (`[1, 2, 3, 4, 5]` and its reverse) → `6`.
- **Zero heights** (`[0, 5]`, `[0, 0]`) → `0`.
- **Equal walls** → discarding either is safe, so the equality case can move either pointer.
- **Single element / empty input** → outside LeetCode's constraints; the loop never runs and `0` is returned defensively.
- **Large heights** → Python integers are arbitrary precision; other languages may need 64-bit area arithmetic.
