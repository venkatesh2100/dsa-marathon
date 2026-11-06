# Largest Rectangle in Histogram

**Problem:** Given an array of bar `heights` (every bar has width 1), return the area of the largest rectangle that fits entirely inside the histogram.

**Links:** [NeetCode 84](https://neetcode.io/problems/largest-rectangle-in-histogram) · [LeetCode 84](https://leetcode.com/problems/largest-rectangle-in-histogram/)

---

## My Solution — Monotonic Increasing Stack of Indices

For every bar, the largest rectangle that uses its full height stretches from the first shorter bar on its left to the first shorter bar on its right. Keep a stack of indices whose heights are strictly increasing. When the current bar is shorter than the stack top, the top bar has just found its right boundary — pop it; its left boundary is the new stack top (the first shorter bar to its left). Width is `k - stack[-1] - 1`, or `k` when the stack is empty (the popped bar is the smallest so far, so it spans from index 0). Appending a `0` sentinel forces every remaining bar to pop at the end.

| | |
|---|---|
| **Time** | O(n) — each index is pushed and popped at most once |
| **Space** | O(n) — the stack of unresolved indices |

**Caveat:** `heights.append(0)` mutates the caller's list — fine on LeetCode, but worth calling out in an interview (iterate over `heights + [0]` instead). Strict `>` keeps equal-height bars on the stack; that is still correct because the leftmost bar of an equal run eventually pops with the full run's width, and the undercounted widths of the other equal bars never win the max.

## Optimal Solution — Monotonic Stack (Same Idea, Polished)

The posted solution is already the optimal approach. The optimal file keeps the identical logic but builds the sentinel on the fly instead of mutating the input.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

```python
stack = []  # indices of bars with strictly increasing heights
res = 0

for k, v in enumerate(heights + [0]):  # trailing 0 flushes the stack
    while stack and heights[stack[-1]] > v:
        h = heights[stack.pop()]
        # first shorter bar on the right is k, on the left is stack[-1]
        width = k if not stack else k - stack[-1] - 1
        res = max(res, h * width)
    stack.append(k)

return res
```

O(n) time and O(n) space are optimal: every bar must be examined, and each bar's best rectangle is finalized exactly once — at the moment its next-smaller bar appears.

## Alternative Approaches

- **Monotonic stack (my solution / optimal):** O(n) time, O(n) space. Default and optimal.
- **Divide & conquer on the minimum bar:** the answer is the max of (min bar × full span, left part, right part). O(n log n) average with a segment tree for range-min, but degrades to O(n²) on sorted input without one. Rarely worth it here.
- **Brute force:** for each bar, expand left and right while heights are ≥ it. O(n²) time, O(1) space. Testing oracle only.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Monotonic stack | **O(n)** | **O(n)** | **Default interview answer** |
| Divide & conquer | O(n log n) avg, O(n²) worst | O(log n)–O(n) | Never here — stack is simpler and faster |
| Brute force | O(n²) | O(1) | Never — only for comparison |

**Interview answer:** Keep a stack of indices with increasing heights. When a shorter bar arrives, pop each taller bar — its rectangle ends at the current index and starts just after the new stack top — and record `height × width`. A trailing sentinel `0` flushes the stack at the end. O(n) time, O(n) space.

## Edge Cases

- **Single bar** → its own height, e.g. `[5]` → `5`.
- **All equal heights** → `n × h`, e.g. `[2, 2, 2]` → `6`.
- **Strictly increasing** → `[1, 2, 3, 4, 5]` → `9` (height 3 × width 3).
- **Strictly decreasing** → `[5, 4, 3, 2, 1]` → `9` (mirror image).
- **Zero splits the histogram** → `[2, 0, 2]` → `2` (no rectangle can cross the 0).
- **Valley shape** → `[2, 1, 2]` → `3` (height 1 across all three beats either 2×1).
- **Empty input** → `0` (LeetCode guarantees at least one bar, but the code handles it).

---

## Testing

```bash
python3 - <<'PY'
import sys
sys.path.insert(0, "stack/largest-rectangle-in-histogram")
from my_solution import Solution as Mine
from optimal_solution import Solution as Optimal

cases = [
    ([2, 1, 5, 6, 2, 3], 10),       # LeetCode example 1
    ([2, 4], 4),                    # LeetCode example 2
    ([5], 5),                       # single bar
    ([2, 2, 2], 6),                 # all equal
    ([1, 2, 3, 4, 5], 9),           # strictly increasing
    ([5, 4, 3, 2, 1], 9),           # strictly decreasing
    ([2, 0, 2], 2),                 # zero splits the histogram
    ([2, 1, 2], 3),                 # valley
    ([6, 7, 5, 2, 4, 5, 9, 3], 16), # mixed
    ([], 0),                        # empty (outside constraints)
]

# fresh list per call: my_solution appends a sentinel 0 to its input
for heights, expected in cases:
    assert Mine().largestRectangleArea(list(heights)) == expected
    assert Optimal().largestRectangleArea(list(heights)) == expected

print("All tests passed")
PY
```
