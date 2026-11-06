# Trapping Rain Water

**Problem:** Given `height` of elevation bars, return the total water trapped between the bars after it rains. Water above index `i` is `min(max height to the left, max height to the right) − height[i]` (never negative).

**Links:** [NeetCode 42](https://neetcode.io/problems/trapping-rain-water) · [LeetCode 42](https://leetcode.com/problems/trapping-rain-water/)

---

## My Solution — Two Pointers, Move the Smaller Wall

Keep two pointers at the ends and running maxima `lmax` / `rmax`. Whichever side has the smaller wall is processed first: update that side's running max, add `bound − height` to the answer, and move the pointer inward. Equal heights fall to the `else` branch and process the right side, which is safe.

| | |
|---|---|
| **Time** | O(n) — one pass; each pointer moves at most `n` steps |
| **Space** | O(1) |

**Caveat:** No correctness issue — the subtle part is *why* `lmax` is enough on the left. When `height[l] < height[r]`, some wall at index `r′ ≥ r` (processed earlier or current) exceeds `height[l]`, and `lmax` was set from a step whose opposing wall already proved it fits under the right side. In short, the running max on the processed side always equals `min(left bound, right bound)` for that cell. The commented `# print(res)` debug line can be dropped.

## Optimal Solution — Two Pointers (Same Idea, Polished)

The attempt above is already the standard O(n) / O(1) optimal solution. The optimal file keeps identical logic with descriptive names.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

```python
while left < right:
    if height[left] < height[right]:
        left_max = max(left_max, height[left])
        water += left_max - height[left]
        left += 1
    else:
        right_max = max(right_max, height[right])
        water += right_max - height[right]
        right -= 1
```

O(n) time is a lower bound since every bar must be read; O(1) space beats the prefix/stack alternatives, so this is the optimum.

## Alternative Approaches

- **Two pointers (my solution / optimal):** O(n) time, O(1) space. The standard optimum.
- **Prefix max arrays:** For each index, compute `leftmax[i]` and `rightmax[i]` in two passes, then `min(...)` − height each cell. O(n) time, O(n) space. Easiest to reason about; great stepping stone.
- **Monotonic stack:** Maintain a decreasing stack of bars; pop when a taller bar arrives, filling horizontal layers between pops. O(n) time, O(n) space. More cases to handle.
- **Brute force:** For each index, scan left and right for the bounds. O(n²) time, O(1) space. Testing oracle, never an answer.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Two pointers | **O(n)** | **O(1)** | **Default interview answer** |
| Prefix max arrays | O(n) | O(n) | If two pointers feels risky; easy to verify |
| Monotonic stack | O(n) | O(n) | When the interviewer asks for a stack-based variant |
| Brute force | O(n²) | O(1) | Never — only as a testing oracle |

**Interview answer:** Two pointers from both ends with running maxima. Move the pointer at the smaller wall, adding `runmax − wall` to the total, because the smaller side's water is already fully determined by its own running max. O(n) time, O(1) space.

## Edge Cases

- **Empty input** → `0`.
- **Single bar / two bars** (`[1, 2]`, `[5, 5]`) → `0`; no gap to fill.
- **Monotonic arrays** (`[1, 2, 3]`, `[3, 2, 1]`) → `0`; nothing is enclosed.
- **Uniform zeros or flats** (`[0, 0, 0]`, `[4, 4, 4]`) → `0`.
- **Valley** (`[3, 0, 2, 0, 4]`) → `7`.
- **Deep container** (`[9, 0, 0, 0, 9]`) → `27`.
- **Classic LeetCode example** (`[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`) → `6`.
- **Peak at an end** (`[5, 4, 1, 2]`) → `1`; the lower end wall limits everything it encloses.
- **Tall bar inside** (`[2, 8, 2]`) → `0`; a bar can rise above its neighbors' water level.
- **Large heights** → Python ints are arbitrary precision; other languages may need 64-bit sums.
