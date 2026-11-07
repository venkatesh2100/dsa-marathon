# Search in Rotated Sorted Array

**Problem:** An ascending array with **unique values** was rotated at an unknown pivot between once and `n` times. Find the index of `target` in O(log n), or return `-1`.

**Links:** [NeetCode](https://neetcode.io/problems/search-in-rotated-sorted-array) · [LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/)

---

## My Solution — One-pass "which half is sorted" binary search

Already optimal. Every window `[l..r]` has exactly one sorted half; a sorted half's value range settles membership cleanly, so each probe discards half the search space:

- `nums[l] <= nums[mid]` → **left** `[l..mid]` is sorted: if `nums[l] <= target < nums[mid]`, target can only be left (`r = mid - 1`); otherwise it must be in the rotated right half (`l = mid + 1`).
- else → **right** `[mid..r]` is sorted: if `nums[mid] < target <= nums[r]`, go right (`l = mid + 1`); else go left (`r = mid - 1`).

| | |
|---|---|
| **Time** | O(log n) |
| **Space** | O(1) |

**Caveat:** No asymptotic caveat — O(log n) is the floor. The risk is behavioral: the three inequalities below are where almost every wrong-answer bug on this problem lives, and the code silently assumes unique values.

## Where the Bugs Hide — the Three Inequalities

| Check | Form | Why that exact form |
|---|---|---|
| Which half is sorted | `nums[l] <= nums[mid]` | `<=` is load-bearing: with a window of ≤ 2 elements, `mid == l`, so `nums[l] == nums[mid]` and the one-element "left half" is trivially sorted. A strict `<` misclassifies `[3, 1]` → returns `-1` for target `1`. |
| Target in sorted left half | `nums[l] <= target < nums[mid]` | Upper end strict: `target == nums[mid]` was already returned above. |
| Target in sorted right half | `nums[mid] < target <= nums[r]` | Lower end strict for the same reason; upper end inclusive because `nums[r]` was never equality-tested — the target may be sitting there. |

Also note the **mid idiom**: `l + (r - l)//2` is the overflow-safe spelling — unnecessary in Python, but the right habit for interviews in C/Java.

**Template:** This is **Template A** (exact match: `while l <= r`, discard with `mid ± 1`, exit `-1`) like Binary Search and Search a 2D Matrix — *not* the lower-bound Template B of Koko / Find-the-Min, because the target may not exist at all. And it is exactly why this problem's classification reads against the **left** end (`nums[l] <= nums[mid]` = "left half is contiguous") while yesterday's find-min read against the **right** end (`nums[mid] > nums[r]` = "the inflection is right of mid"): different question, different probe.

## Optimal Solution — Same, Polished

Identical algorithm — one-pass with the sorted-half classification. The polish: comments on each branch, no debug `print` in the hot loop, `(l + r) // 2` naming. Same **O(log n) / O(1)**; there is no asymptotically faster approach.

## Alternative Approaches

- **Two-pass:** find the pivot with the find-min trick (`nums[mid] > nums[r]` → pivot is right of mid), then plain binary search over offset-mapped indices. Still O(log n) overall; two small, easy-to-verify pieces at the cost of soldering two templates and a modulo together.
- **Linear scan / `nums.index(target)`:** O(n) — ignores everything the rotation structure offers.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| One-pass sorted-half check | **O(log n)** | **O(1)** | **Default — my solution already is it** |
| Two-pass (pivot + bisect) | O(log n) | O(1) | If one-pass logic feels fragile live — two independent steps are easier to get right |
| Linear scan | O(n) | O(1) | Never |

**Interview answer:** Name the invariant first — "exactly one half of any window is sorted, so its range can veto the other half" — then code Template A with the three inequalities exactly as tabulated above.

## Edge Cases

- **Single element** → one probe: equality returns, else the `[l, mid)` membership is impossible (`l == mid`) and `l` walks past `r` → `-1`.
- **Window of two, rotated** (`[3, 1]`, target `1`) → passes only because the half-detection uses `<=`; see bug table.
- **Not rotated** (`[1, 2, 3, 4, 5]`) → left half is always sorted; silently degrades to plain binary search.
- **Target == `nums[r]`** (`[4, 5, 6, 7, 0, 1, 2]`, target `2`) → still found: right-half membership is inclusive on `nums[r]`.
- **Target absent, inside a half's range** → window empties (`l > r`) → `-1`.
- **Empty input** → excluded by constraints (`n ≥ 1`); if it ever happened, `while 0 <= -1` never runs → `-1`, no `IndexError`. Convenient by accident.
- **Duplicates** → excluded here; with dupes (LC 81) `nums[l] == nums[mid] == nums[r]` can classify neither half → shrink with `l += 1`, worst case O(n).
