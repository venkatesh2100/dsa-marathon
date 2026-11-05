# 3Sum

**Problem:** Given an integer array `nums`, return all unique triplets `[a, b, c]` such that `a + b + c = 0`. The solution set must not contain duplicate triplets.

**Links:** [NeetCode 15](https://neetcode.io/problems/three-integer-sum) · [LeetCode 15](https://leetcode.com/problems/3sum/)

---

## My Solution — Sort, Fix One Index, Two Pointers

Sort the array so equal values are adjacent and the two-pointer sweep is possible. Fix each index `i` as the smallest value of the triplet, then use `left` and `right` on the remaining suffix. If the sum is too small, move `left` right; if too large, move `right` left; on zero, record the triplet and move both inward.

Duplicates are handled in three places: skip a repeated anchor `i`, and after recording a triplet, skip repeated `left` and `right` values.

| | |
|---|---|
| **Time** | O(n²) |
| **Space** | O(1) extra (excluding the output and Python's sort buffer) |

**Caveat:** `nums.sort()` mutates the caller's list. If the original order matters, sort a copy (`nums = sorted(nums)`) at the cost of O(n) extra space. The early `break` when `nums[i] > 0` is safe only because the array is sorted: once the smallest value is positive, every remaining value is positive too.

## Optimal Solution — Sort + Two Pointers (Same Idea, Polished)

The approach above is already the standard optimal solution. The optimal file keeps the same logic with clearer names and the comparison ordered by frequency (`total < 0` first).

| | |
|---|---|
| **Time** | O(n²) |
| **Space** | O(1) extra (excluding the output and Python's sort buffer) |

```python
for i in range(n - 2):
    if nums[i] > 0:
        break
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left, right = i + 1, n - 1
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        ...
```

For each anchor, the two-pointer sweep is O(n), and there are O(n) anchors, giving O(n²). Sorting is O(n log n), which is dominated. No general sub-quadratic algorithm is known for 3SUM, so O(n²) is the accepted optimum.

## Alternative Approaches

- **Sort + two pointers (my solution / optimal):** O(n²) time, O(1) extra space. Best combination of speed and memory.
- **Hash set per anchor:** O(n²) time, O(n) space. Avoids sorting but still needs a dedup set for triplets; more memory and messier.
- **Binary search for the third value:** O(n² log n) time. Correct but slower than the two-pointer sweep.
- **Brute force:** O(n³) time. Never acceptable.
- **Sort + hash map:** O(n²) time, O(n) space. Similar tradeoff to the per-anchor hash set.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Sort + two pointers | **O(n²)** | **O(1)** extra | **Default interview answer** |
| Hash set per anchor | O(n²) | O(n) | Input must not be mutated |
| Binary search | O(n² log n) | O(1) | Educational; slower in practice |
| Brute force | O(n³) | O(1) | Never — only for comparison |

**Interview answer:** Sort the array. For each index, skip duplicates and run two pointers on the suffix. When the sum is zero, record the triplet, move both pointers, and skip duplicates again. Break once the anchor becomes positive. O(n²) time and O(1) extra space excluding the output.

## Edge Cases

- **Fewer than three elements** (`[]`, `[0]`, `[0, 0]`) → `[]`; the loop never runs.
- **Exactly three elements** (`[0, 0, 0]`) → `[[0, 0, 0]]`.
- **Many zeros** (`[0, 0, 0, 0, 0]`) → `[[0, 0, 0]]` once, not ten copies.
- **No solution** (`[1, 2, 3]`, `[-1, -2, -3]`) → `[]`.
- **All positive** → `[]`; the early break exits immediately after sorting.
- **All negative** → `[]`; the two-pointer sweep cannot reach zero.
- **Repeated values** (`[-1, 0, 1, 2, -1, -4]`) → `[[-1, -1, 2], [-1, 0, 1]]`, with no duplicates.
- **Multiple valid triplets** (`[-2, 0, 1, 1, 2]`) → `[[-2, 0, 2], [-2, 1, 1]]`.
- **Duplicates around the pointers** → the post-match `while` loops skip them; removing either skip loop can produce duplicate triplets.
- **Input order matters to the caller** → sort a copy, since this solution sorts in place.
