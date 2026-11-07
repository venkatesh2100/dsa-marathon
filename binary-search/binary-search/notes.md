# Binary Search

**Problem:** Given a sorted (ascending) array `nums` of distinct integers and a `target`, return the index of `target` in `nums`, or `-1` if it does not exist. Must run in O(log n) time.

**Links:** [NeetCode](https://neetcode.io/problems/binary-search) · [LeetCode 704](https://leetcode.com/problems/binary-search/)

---

## My Solution — Binary Search with a Shrinking Window (off-by-one step)

Classic half-open scan: `mid` is compared to `target`, and pointers shrink the window when the answer can't be there. The bug: `r -= 1` / `l += 1` moves the pointers **one step per iteration** instead of jumping to `mid ± 1`.

Why this silently breaks the O(log n) guarantee: if `nums[mid] > target`, the target lies at an index `< mid`, so decrementing `r` by 1 keeps the window valid (correctness holds), but the window only shrinks by a single element each round. On a miss against a large sorted array (target smaller than everything), `r` walks from `n-1` down to `-1` one step at a time — effectively a backwards linear scan wearing a binary search costume.

| | |
|---|---|
| **Time** | O(n) worst case |
| **Space** | O(1) |

**Caveat:** Correct results on all inputs, but it fails the problem's O(log n) requirement. The `elif`/`else` on one line makes it easy to miss that both branches move by exactly one — `mid` itself costs nothing. Two iterations can pass with `mid` barely moving, so the halving never happens.

## Optimal Solution — True Binary Search (halve the window)

Same skeleton, but each branch eliminates the entire half *including* `mid`:

- `nums[mid] > target` → every index `>= mid` is too big → `r = mid - 1`
- `nums[mid] < target` → every index `<= mid` is too small → `l = mid + 1`

So the window size halves every iteration: `n → n/2 → n/4 → …` which is what earns the O(log n) bound. Since `mid` was already checked and ruled out, jumping past it is always safe — no element can be skipped.

| | |
|---|---|
| **Time** | O(log n) |
| **Space** | O(1) |

```python
mid = l + (r - l) // 2   # overflow-safe form; in Python just (l + r) // 2 works
```

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Binary search (`mid ± 1`) | **O(log n)** | **O(1)** | **Default — this is the answer** |
| My version (±1 steps) | O(n) | O(1) | Never — fails the O(log n) requirement |
| Linear scan | O(n) | O(1) | Never — ignores that input is sorted |

**Interview answer:** On a sorted array, binary search: keep `l`, `r` pointers, compute `mid = l + (r - l) // 2`, return `mid` on a match; otherwise recurse into the half that can contain the target by setting `r = mid - 1` or `l = mid + 1`. O(log n) time, O(1) space.

**The takeaway:** a binary search that moves a pointer by one instead of to `mid ± 1` is still *a* binary search syntactically but is O(n) asymptotically. If pointer updates don't jump around `mid`, complexity quietly reverts to linear. This is also the classic source of infinite loops in versions with `l < r` or `r = mid`, so the pointer arithmetic is the whole game.

## Edge Cases

- **Target smaller than every element** (`[-5, 0, 3, 7]`, target `-9`) → `-1`. This is where my version degrades worst: `r` walks all the way down step by step.
- **Target larger than every element** (`[1, 2, 3]`, target `10`) → `-1`; `l` runs off the right end.
- **Single element hit** (`[5]`, target `5`) → `0`.
- **Single element miss** (`[5]`, target `1`) → `-1`.
- **Empty array** (`[]`, target `1`) → `-1`; `r` starts at `-1` so the loop never runs.
- **Target at index 0 or len - 1** → both reachable; boundaries must not be skipped.
- **Window narrows to two elements** → `mid == l`, so `l = mid + 1` must move; a non-moving pointer is an infinite-loop smell.
- **Two elements** (`[1, 3]`, target `3`) → `1`; catches `mid` sticking at `l`.
