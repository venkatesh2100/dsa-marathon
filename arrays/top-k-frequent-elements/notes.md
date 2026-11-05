# Top K Frequent Elements

**Problem:** Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. The answer may be returned in any order.

**Links:** [NeetCode 347](https://neetcode.io/problems/top-k-elements-in-list) · [LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/)

---

## My Solution — Count, Sort, Take K

Build a frequency map, sort its `(value, count)` pairs by count descending, then take the first `k` values.

| | |
|---|---|
| **Time** | O(n + m log m) — worst case O(n log n) |
| **Space** | O(m) |

Where `n` is the array length and `m` is the number of distinct values.

**Caveat:** Sorting all distinct values is wasteful when only `k` of them are needed. Also, `while k:` mutates the input parameter and would loop forever if `k` were negative; a `for _ in range(k)` is safer.

## Optimal Solution — Bucket Sort by Frequency

Frequencies are bounded: no value can appear more than `n` times. Create `n + 1` buckets where bucket `f` holds all values appearing exactly `f` times, then walk buckets from highest frequency down until `k` values are collected.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

```python
buckets = [[] for _ in range(len(nums) + 1)]
for num, freq in counts.items():
    buckets[freq].append(num)

for freq in range(len(buckets) - 1, 0, -1):
    for num in buckets[freq]:
        ...
```

This is optimal because the output size is at most `k ≤ n`, so O(n) is a lower bound.

## Alternative Approaches

- **Min-heap of size `k`:** O(n log k) time, O(n) space. Good when `n` is huge or the input is a stream and `k` is small.
- **Quickselect:** O(n) average, O(n²) worst case. In-place and fast in practice, but randomized and more code to get right.
- **Sorting (my solution):** O(n log n) time, O(n) space. Simplest to write and explain.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Bucket sort | **O(n)** | O(n) | **Default** — frequencies are bounded by `n` |
| Min-heap | O(n log k) | O(n) | Streaming input or very large `n`, small `k` |
| Quickselect | O(n) avg | O(n) | In-place selection, comfortable with partitioning |
| Sort by count | O(n log n) | O(n) | Simplest, fine for small inputs |

**Interview answer:** Count frequencies, then bucket values by frequency. Scanning buckets from high to low gives the top `k` in O(n) time and O(n) space.

## Edge Cases

- `k == 1` → return the single most frequent value.
- `k == number of distinct values` → return every distinct value.
- All elements identical `([4, 4, 4], 1)` → `[4]`.
- Ties in frequency → any valid order is accepted; bucket order and sort order may differ but both are correct.
- Negative values → no issue; values are only used as keys.
- `nums` length 1 → one bucket entry, returns immediately.
