# Longest Consecutive Sequence

**Problem:** Given an unsorted integer array `nums`, return the length of the longest run of consecutive integers. Duplicates may appear, and the numbers do not need to be adjacent in the input.

**Links:** [NeetCode 128](https://neetcode.io/problems/longest-consecutive-sequence) · [LeetCode 128](https://leetcode.com/problems/longest-consecutive-sequence/)

---

## My Solution — Hash Set, Count Downward from Run Ends

Put every number in a set for O(1) membership checks. A value is the **end** of a run when `val + 1` is not in the set. For each run end, walk downward while `val - 1` exists, count the run length, and track the maximum.

| | |
|---|---|
| **Time** | O(n) expected |
| **Space** | O(n) |

**Caveat:** The `while` loop runs only for run ends, so each element is counted at most once overall — that is what keeps the solution linear. Reassigning `val` inside the loop is safe in Python (the iterator is unaffected) but slightly confusing; a separate `cur` variable reads better. Set iteration order is arbitrary but does not affect the result.

## Optimal Solution — Hash Set, Count Upward from Run Starts

Same idea, but identify **starts** with `num - 1 not in values` and count upward. It reads naturally and never mutates the loop variable.

| | |
|---|---|
| **Time** | O(n) expected |
| **Space** | O(n) |

```python
for num in values:
    if num - 1 in values:
        continue

    length = 1
    while num + length in values:
        length += 1

    longest = max(longest, length)
```

This is optimal: every number must be inspected at least once, giving an O(n) lower bound, and the hash set provides O(1) expected membership. O(n) space is the tradeoff for avoiding sorting.

## Alternative Approaches

- **Hash set from run boundaries (my solution / optimal):** O(n) expected time, O(n) space. Standard interview answer.
- **Sorting:** O(n log n) time, O(n) extra for a sorted copy (or O(1) extra if mutating in place). Simple and robust; use it if hashing is unavailable or worst-case guarantees matter.
- **Brute force:** For each number, repeatedly scan the array looking for its successor. O(n²) or worse. Never.
- **Union-Find:** O(n α(n)) time and O(n) space. Correct but far more machinery than needed.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Hash set from run boundaries | **O(n)** expected | O(n) | **Default answer** |
| Sorting | O(n log n) | O(n) | Hashing unavailable, or need a deterministic worst case |
| Brute force | O(n²) | O(1) | Never — only for comparison |
| Union-Find | O(n α(n)) | O(n) | Overkill; only if already using DSU |

**Interview answer:** Put all numbers in a set. Only begin counting when `num - 1` is absent, then walk upward while consecutive values exist. Each number is visited at most twice, so it is O(n) expected time and O(n) space.

## Edge Cases

- **Empty array** → `0`.
- **Single element** → `1`.
- **All duplicates** (`[5, 5, 5]`) → `1`; the set collapses them.
- **No consecutive pairs** (`[10, 5, 100]`) → `1`.
- **Negative numbers** (`[-3, -2, -1, 0]`) → `4`; set membership and arithmetic handle negatives.
- **Crossing zero** (`[-1, 0, 1]`) → `3`.
- **Unsorted input** → no effect; the set removes order dependence.
- **Duplicates inside a run** (`[1, 2, 2, 3, 3, 4]`) → `4`, with no double counting.
- **Reverse-sorted input** (`[9, 8, 7, 6, 5]`) → `5`; still linear.
- **Large gaps** → separate runs, membership checks fail fast.
