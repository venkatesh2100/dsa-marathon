# Product of Array Except Self

**Problem:** Given an integer array `nums`, return an array `res` where `res[i]` is the product of all elements of `nums` except `nums[i]`. Must run in O(n) time and without using division.

**Links:** [NeetCode 238](https://neetcode.io/problems/products-of-array-discluding-self) · [LeetCode 238](https://leetcode.com/problems/product-of-array-except-self/)

---

## My Solution — Prefix and Suffix Arrays

Build `pre[i]` = product of `nums[0..i-1]` and `suf[i]` = product of `nums[i..n-1]`, both padded with 1 at the ends. Then `res[i] = pre[i] * suf[i+1]`: everything to the left times everything to the right.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) extra |

**Caveat:** Two extra arrays of length `n + 1` are unnecessary. The prefix pass can write directly into the output, and the suffix pass can multiply in place, giving O(1) extra space. Also, `res = []` plus repeated `append` is fine but `[1] * n` makes the in-place approach cleaner.

## Optimal Solution — Running Prefix, Then Running Suffix

Use the output array to hold the prefix products, then sweep backwards with a single running suffix product and multiply it in.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) extra (output not counted) |

```python
prefix = 1
for i in range(n):
    res[i] = prefix
    prefix *= nums[i]

suffix = 1
for i in range(n - 1, -1, -1):
    res[i] *= suffix
    suffix *= nums[i]
```

This is optimal: every element must be read at least once, so O(n) is a lower bound, and only a constant number of extra variables are used.

## Why Not Division?

The obvious `total // nums[i]` breaks on zeros and is disallowed by the follow-up. Handling zeros explicitly (one zero vs two zeros) is possible but messier than the prefix/suffix method.

## Alternative Approaches

- **Prefix + suffix arrays (my solution):** O(n) time, O(n) extra space. Easiest to reason about.
- **Running prefix/suffix (optimal):** O(n) time, O(1) extra space. Standard interview answer.
- **Division with zero handling:** O(n) time, O(1) space, but disallowed and error-prone.
- **Brute force:** O(n²) time. Never acceptable here.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Running prefix + suffix | **O(n)** | **O(1)** | **Default answer** |
| Prefix + suffix arrays | O(n) | O(n) | First idea / easier to explain |
| Division with zeros | O(n) | O(1) | Disallowed by the problem |
| Brute force | O(n²) | O(1) | Never |

**Interview answer:** First pass writes the product of all elements before each index into the result. Second pass walks backwards and multiplies by the product of all elements after each index. O(n) time, O(1) extra space, no division.

## Edge Cases

- **One zero** `([1, 2, 0, 4])` → `[0, 0, 8, 0]`: only the zero's position gets the product of the non-zero values.
- **Two zeros** `([0, 0])` → `[0, 0]`: every product contains a zero.
- **Negative numbers** `([-1, -2, -3])` → `[6, 3, 2]`: sign follows naturally from multiplication.
- **Two elements** `([2, 3])` → `[3, 2]`.
- **Single element** `([5])` → `[1]` (empty product), though constraints usually require `n ≥ 2`.
- **Large values** → Python integers are arbitrary precision; other languages may need 64-bit types.
