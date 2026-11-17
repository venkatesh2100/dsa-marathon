# K Closest Points to Origin

**Problem:** Given an array of `[x, y]` points and an integer `k`, return the `k` points closest to the origin `(0, 0)` by Euclidean distance, in any order.

**Links:** [NeetCode](https://neetcode.io/problems/k-closest-points-to-origin) · [LeetCode 973](https://leetcode.com/problems/k-closest-points-to-origin/)

---

## My Solution — Min-heap of every point, pop k

Compute each point's Euclidean distance and push `(dis, point)` into a min-heap; then pop `k` times. Popping the smallest distance first is exactly "closest first," so the k pops are the answer.

| | |
|---|---|
| **Time** | O(n log n) — n pushes to build + k pops at O(log n) |
| **Space** | O(n) — the heap holds every point |

**Caveats:**
- The `**0.5` sqrt is unnecessary work: sqrt is monotonically increasing, so **squared** distance orders identically and stays an exact int (no float ties/rounding at all).
- The heap pops come out as **tuples** (from the `(dis, (r, c))` entry) — LeetCode's judge accepts them, but the signature promises `List[List[int]]`; normalize with `list(...)` to be safe.
- `dis, points = heapq.heappop(heap)` **rebinds the `points` parameter** to the popped coordinate. Harmless here only because the input list is already fully consumed — a shadowing footgun.
- Pushing all n points overkills when `k ≪ n` (see optimal).

## Optimal Solution — Max-heap of size k on squared distance

Keep only a max-heap of the k best points seen so far: push the first k, then for each remaining point, `heappushpop` — if the new point is closer than the farthest kept, it evicts it. Squared distances (exact ints) rank identically to true distances since sqrt is monotonic. Negated values turn the min-heap into a max-heap whose root is the *farthest* kept point — the one to evict.

| | |
|---|---|
| **Time** | O(n log k) — heap never exceeds k entries |
| **Space** | O(k) — independent of n |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Max-heap of size k (optimal) | O(n log k) | O(k) | **Default answer** — wins when k ≪ n, and O(k) memory |
| Min-heap of all + pop k (my solution) | O(n log n) | O(n) | Works; correct idiom but pays for all n when only k matter |
| `heapq.nsmallest(k, points, key=...)` | O(n log k) | O(k) | Same complexity as optimal — fine one-liner, less instructive |
| Quickselect partition | O(n) average, O(n²) worst | O(1)/O(n) | The follow-up answer if asked to beat the heap |

**Interview answer:** "Squared distance ranks the same as Euclidean, so no sqrt. Keep a max-heap of size k — root is the farthest kept point; each new point either enters while the heap is small or pushpops against the root. O(n log k) time, O(k) space."

## Edge Cases

- **`k == n`** → every point qualifies (heap still does the work correctly).
- **`k == 1`** → single closest point.
- **Distance ties** → any valid selection of the tied points is accepted (judge checks the distance multiset, not order).
- **Duplicate points** → multiplicity respected; a duplicated point may be returned as many times as it occurs.
- **Negative coordinates / max coords (±10⁴)** → squaring keeps everything exact and non-negative.
- **Point at the origin** (`[0,0]`) → distance 0, always among the closest.
