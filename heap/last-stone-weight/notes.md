# Last Stone Weight

**Problem:** Repeatedly pick the two heaviest stones and smash them together. Equal weights destroy both; otherwise a new stone of weight `|x - y|` rejoins the pool. When at most one stone remains, return its weight — or `0` if none do.

**Links:** [NeetCode](https://neetcode.io/problems/last-stone-weight) · [LeetCode 1046](https://leetcode.com/problems/last-stone-weight/)

---

## My Solution — Max-heap via negation, push-per-element build

Python's `heapq` is a min-heap only, so every stone is pushed **negated** — the smallest negated value is the heaviest stone. Loop while ≥ 2 stones remain: pop two, negate back to positive weights, and push the remainder (negated) if it's nonzero (`abs(x - y) > 0` — on a tie both stones die). Return the negated root, or `0` when the heap is empty.

| | |
|---|---|
| **Time** | O(n log n) — n pushes to build + O(n) smash rounds of O(log n) pops/pushes |
| **Space** | O(n) — a second heap array |

**Caveats:**
- Building with n `heappush` calls costs O(n log n); `heapify` on a pre-negated list builds in O(n). (The commented-out `heap = heapq.heapify(stones)` wouldn't have worked anyway — `heapify` mutates the list in place and returns `None`.)
- `abs(x - y) > 0` is just `x != y`, and since pops come out heaviest-first, `abs(x - y)` is always simply `x - y`.

## Optimal Solution — heapify build, same smash loop

Negate into a fresh list once and `heapify` in O(n); the smash loop is unchanged but reads cleaner (`x != y`, `- (x - y)`). Overall asymptotics are the same O(n log n) — the smash loop dominates either way — the heapify build is a constant-factor and idiom improvement.

| | |
|---|---|
| **Time** | O(n log n) |
| **Space** | O(n) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Max-heap, `heapify` build (optimal) | O(n log n) | O(n) | **Default answer** — the idiom interviewers expect |
| Max-heap, push-per-element build (my solution) | O(n log n) | O(n) | Works; build phase is a log-factor slower but same total class |
| Sorted list + `bisect.insort` of remainders | O(n²) | O(n) | Fine for tiny n; no heap needed but slower |
| Re-sorting the whole list every turn | O(n² log n) | O(1) extra | Never — pays full sort cost per smash |

**Interview answer:** "A max-heap gives the two heaviest stones in O(log n) per turn. Python's heapq is a min-heap, so negate the values, heapify, then loop: pop two, push back the difference if nonzero. Return the last stone or 0. O(n log n) time, O(n) space."

## Edge Cases

- **Single stone** → returned as-is, no smash.
- **Two equal stones** (`[2,2]`) → both destroyed → `0`.
- **Odd count of equal stones** (`[2,2,2]`) → pairs cancel, one survives → `2`.
- **Cascades to zero** (`[9,3,2,10]`) → 10·9→1, 3·2→1, 1·1→0 → `0`.
- **Remainder re-enters the pool** (`[8,10,4]`) → the 2 produced by 10·8 then smashes the 4.
- **Empty list** → not a valid LeetCode input (`n ≥ 1`), but both versions return `0`.
