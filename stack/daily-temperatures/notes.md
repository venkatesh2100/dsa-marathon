# Daily Temperatures

**Problem:** Given an array `temp` of daily temperatures, for each day return how many days you would have to wait until a warmer day. If no warmer day exists on the horizon, the answer is `0`.

**Links:** [NeetCode 739](https://neetcode.io/problems/daily-temperatures) · [LeetCode 739](https://leetcode.com/problems/daily-temperatures/)

---

## My Solution — Monotonic Decreasing Stack

Keep a stack of indices whose warmer day hasn't been found yet. For each new day's temperature, pop every stack top whose temperature is cooler than the current day and record the wait as the difference between the current index and the popped index. Then push the current index. Indices left in the stack have no future warmer day and keep their default `0`.

| | |
|---|---|
| **Time** | O(n) — each index is pushed and popped at most once |
| **Space** | O(n) — the stack holds unresolved indices |

**Caveat:** The resolution expression `res[stack[-1]] = k - stack[-1]` is the day-to-day wait: popped day `i`, current day `k`, answer `k - i`. The `0` default correctly encodes "no warmer day ahead" for whatever survives in the stack. This is the standard LeetCode 739 solution and is optimal.

## Optimal Solution — Monotonic Stack (Same Idea, Polished)

The posted solution is already the optimal approach. The optimal file keeps the identical logic with named variables for readability.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

```python
res = [0] * n
stack = []  # indices with unresolved warmer days

for i, t in enumerate(temp):
    while stack and temp[stack[-1]] < t:
        prev = stack.pop()
        res[prev] = i - prev
    stack.append(i)

return res
```

O(n) time and O(n) space are optimal: every element is pushed once and popped once. The auxiliary stack is necessary because each day can only be resolved by a strictly greater value to its right.

## Alternative Approaches

- **Monotonic stack (my solution / optimal):** O(n) time, O(n) space. Default and optimal.
- **Brute force:** For each day, scan all later days for a warmer one. O(n²) time, O(1) space. Testing oracle only.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Monotonic stack | **O(n)** | **O(n)** | **Default interview answer** |
| Brute force | O(n²) | O(1) | Never — only for comparison |

**Interview answer:** Use a stack of indices with decreasing temperatures. When a hotter day appears, pop all cooler stack entries and set their answers to the current index minus their index; push the current index. Left-over stack entries get `0`. O(n) time, O(n) space.

## Edge Cases

- **Empty array** → `[]`.
- **No warmer day anywhere** → all zeros; e.g. `[1, 2, 3, 4]` wait — this has a warmer day for each. For a strictly decreasing array like `[4, 3, 2, 1]` → all zeros.
- **Strictly increasing array** → `[30, 40, 50, 60, 70]` → `[1, 1, 1, 1, 0]`.
- **All same temperature** → `[20, 20, 20]` → all zeros (warmth must be strictly greater).
- **Single element** → `[73]` → `[0]`.
- **Warmer day at the end** → `[75, 74, 73, 71, 69, 72, 76, 73]` → `[1, 1, 4, 2, 1, 1, 0, 0]`.
- **Multiple consecutive warmer days** → each resolved with its own difference.

---

## Testing

```bash
python3 - <<'PY'
import sys
sys.path.insert(0, "stack/daily-temperatures")
from my_solution import Solution as Mine
from optimal_solution import Solution as Optimal

cases = [
    ([], []),
    ([73], [0]),
    ([30, 40, 50, 60, 70], [1, 1, 1, 1, 0]),
    ([74, 74, 75], [2, 1, 0]),
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([89, 62, 70, 75, 64, 71, 90], [6, 1, 1, 3, 1, 1, 0]),
]

for temp, expected in cases:
    assert Mine().dailyTemperatures(temp) == expected
    assert Optimal().dailyTemperatures(temp) == expected

print("All tests passed")
PY
```
