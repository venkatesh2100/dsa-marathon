# Find Minimum in Rotated Sorted Array

**Problem:** An ascending sorted array (unique values) was rotated between 1 and `n` times at an unknown pivot. Return the minimum element — expected in O(log n).

**Links:** [NeetCode](https://neetcode.io/problems/find-minimum-in-rotated-sorted-array) · [LeetCode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

---

## My Solution — Linear scan for the inflection

Rather than tracking a running minimum, the scan looks for the **one place the sort breaks**: `nums[i-1] > nums[i]`. That drop is the rotation point, and `nums[i]` there is the minimum. If no drop ever happens, the rotation didn't move the seam (rotation by 0 or by a full cycle), so the initial `mini = nums[0]` stands.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

**Caveat:** Correct *because* the input is a rotated sorted array with **unique values** — the code trusts "there is exactly one drop." On arbitrary input it can overshoot: `[1, 2, 3, 2]` records the last drop's `2` while the true min is `1`. Speed-wise it's the same O(n) as plain `min(nums)`, so drop-detection buys structure, not time.

## Optimal Solution — Binary search, compare `mid` against the right end

The minimum hides where the two sorted halves meet. Compare `nums[mid]` to `nums[r]`:

- **`nums[mid] > nums[r]`** → the drop lies strictly inside `(mid, r]`, and `mid` itself can't be the min (something smaller sits at `r`) → `l = mid + 1`
- **`nums[mid] < nums[r]`** → `[mid..r]` is fully sorted, so the inflection is in `[l, mid]` — `mid` *may* be the min → `r = mid`

| | |
|---|---|
| **Time** | O(log n) |
| **Space** | O(1) |

Two details carry the whole solution:

- **Compare with `r`, not `l`.** Against `l` you cannot tell "window fully sorted, min at `l`" ("`[1, 2, 3]`") from "rotated, min in the right half" — that template needs an extra `if nums[l] <= nums[r]` bailout. Against `r`, no special case exists.
- **No infinite loop guaranteed:** `l < r` makes `mid < r` by floor division, so `r = mid` always shrinks the window; `l = mid + 1` strictly raises `l`.

This is **Template B again** (`while l < r` + `r = mid`) — same lower-bound shape as [Koko Eating Bananas](../koko-eating-bananas/notes.md): the answer can equal `mid`, so `mid` must stay in the window and `r = mid - 1` is forbidden (it can discard the answer itself).

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Binary search vs right end | **O(log n)** | **O(1)** | **Default — the rotation structure is the interview point** |
| Linear inflection scan | O(n) | O(1) | My first attempt — fine fallback pattern |
| `min(nums)` | O(n) | O(1) | One-liner prototype; ignores the rotation property |

**Interview answer:** The scan first is a fine warm-up, but the problem statement asks for O(log n): binary search with the condition `nums[mid] > nums[r]` moves left if the seam is right of `mid`, else keeps `mid` (`r = mid`), until `l == r`.

## Edge Cases

- **Single element** → both return `nums[0]`; optimal's loop never runs (`0 < 0` false), mine's `range(1, 1)` is empty.
- **Not rotated** (`[1, 2, 3, 4, 5]`) → no drop detected / `nums[mid] < nums[r]` always → returns `nums[0]`.
- **Min at the last index** (`[2, 3, 4, 5, 1]`) → the single drop is found; binary search walks `r` down to it.
- **`n = 2`** (`[1, 2]`, `[2, 1]`) → smallest window where the `nums[mid] > nums[r]` branch fires (`[2, 1]` → `1`).
- **Empty input** → excluded by constraints (`n ≥ 1`); both versions would raise `IndexError` on `nums[0]`.
- **Duplicates** → excluded here; with dupes (LC 154), `nums[mid] == nums[r]` is undecidable — fall back to `r -= 1`, worst case O(n), everything else still applies.
