# Contains Duplicate

**Problem:** Given an integer array `nums`, return `true` if any value appears more than once, otherwise `false`.

**Links:** [NeetCode 217](https://neetcode.io/problems/duplicate-integer) · [LeetCode 217](https://leetcode.com/problems/contains-duplicate/)

---

## My Solution — Hash Map Count

Track how many times each value has appeared. Bail out as soon as a count exceeds 1.

| | |
|---|---|
| **Time** | O(n) average |
| **Space** | O(n) |

**Caveat:** Worst-case time is O(n²) if every key collides into the same bucket. Python's `dict` uses open addressing and randomized hashing for strings, so this is only a theoretical concern for integer keys.

## Optimal Solution — Hash Set

We only care *whether* a value was seen, not how many times. A `set` drops the count bookkeeping and early-exits on the first repeat.

| | |
|---|---|
| **Time** | O(n) average |
| **Space** | O(n) |

```python
seen = set()
for num in nums:
    if num in seen:
        return True
    seen.add(num)
return False
```

## One-liner

```python
return len(nums) != len(set(nums))
```

Also O(n) time / O(n) space, but it always builds the full set — no early exit on the first duplicate.

## O(1) Space Alternative — Sorting

```python
nums.sort()
for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        return True
return False
```

| | |
|---|---|
| **Time** | O(n log n) |
| **Space** | O(1) extra (ignoring sort internals) |

Only valid if mutating the input is allowed. Otherwise use `sorted(nums)`, which costs O(n) extra space and loses the advantage.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Hash set | **O(n)** | O(n) | **Default answer.** Fastest, early exit, does not mutate input |
| Hash map count | O(n) | O(n) | Fine, but unnecessary bookkeeping for this problem |
| Sorting | O(n log n) | O(1) | Memory is tight and the input may be mutated |
| Brute force | O(n²) | O(1) | Never — only mention it to justify the better approaches |

**Interview answer:** Say the hash set is optimal for time, mention sorting as the O(1)-space tradeoff, then code the hash set.

## Edge Cases

- Empty array → `False` (loop never runs).
- Single element → `False` (nothing to compare against).
- All distinct → `False`, and the set stores all `n` values.
- Duplicate at the very start → `True` after the first two elements.
- Negative numbers / large values → no issue; Python hashing handles them.
