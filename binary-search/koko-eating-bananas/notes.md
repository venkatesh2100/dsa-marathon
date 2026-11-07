# Koko Eating Bananas

**Problem:** Koko eats one pile per hour at a fixed rate `k` chosen once, up front. Each hour she takes one pile and eats up to `k` bananas from it (finishing it early wastes the rest of the hour). Given `piles` and `h` hours, return the minimum `k` so she finishes within `h` hours. (`h ≥ len(piles)` is guaranteed.)

**Links:** [NeetCode](https://neetcode.io/problems/eating-bananas) · [LeetCode 875](https://leetcode.com/problems/koko-eating-bananas/)

---

## My Solution — Binary Search on the Answer (lower-bound template)

The search space is no longer array indices — it is the **value** of the answer itself: every integer rate from `1` to `max(piles)`. The predicate "does rate `k` finish in time?" is monotone: if it holds for `k`, it holds for every larger rate. So the feasible region is a suffix of the range, and we want its leftmost point — solved by binary search.

Two details carry the whole solution:

- **`r = max(piles)`** — eating faster than the largest pile cannot help anymore. Cutting a pile to zero still takes a full hour, so total time bottoms out at `len(piles)` hours; anything past `max(piles)` changes nothing.
- **`(p + rate - 1) // rate`** — integer ceiling division. Same as `math.ceil(p / rate)` but with no float rounding traps; the third spelling is `-(-p // rate)`.

| | |
|---|---|
| **Time** | O(n · log m), n = len(piles), m = max(piles) ≤ 10⁹ |
| **Space** | O(1) |

`log m ≈ 30`, so this is about `30n` comparisons — e.g. n = 10⁴ gives ~300,000 hours-computed per search.

**Caveat:** Termination and correctness here are hostage to the template pairing `while l < r` with `r = mid` / `l = mid + 1`. It is self-consistent (`mid < r` always holds when `l < r`, so `r = mid` strictly shrinks), but this exact pairing matters — see the template table below.

## The Template Split — This Problem vs the Last Three

Three problems in, there are now **two distinct binary search templates** in play, and mixing their parts is the classic way to get an infinite loop or skip the answer:

| | Template A: exact match (LC 704, 74) | Template B: lower bound (LC 875) |
|---|---|---|
| Loop condition | `while l <= r` | `while l < r` |
| Found at `mid` | return `mid` (or search was a miss) | keep `mid` as a candidate: `r = mid` |
| Rejecting mid | `r = mid - 1` / `l = mid + 1` — safe, mid was compared | `l = mid + 1` — but never `r = mid - 1` |
| Range at exit | `l > r`, answer known or absent | `l == r`, answer *is* that index |
| Failure if mispaired | `r = mid` with `l == r` → `mid == l` → `r` never moves → **infinite loop** | `r = mid - 1` can discard the answer itself → **wrong result** |

The sticky rule: in Template B the answer may equal `mid` itself (you're looking for a boundary, not a value), so `mid` must stay inside the window; that forces `l < r` and `r = mid`.

## Optimal Solution — Same, Polished

Identical algorithm; the polish is canonical naming (`h` per problem statement), a named `hours_needed` helper, and a comment on the ceiling trick. Complexity is unchanged — there is no known faster approach for general inputs.

| | |
|---|---|
| **Time** | O(n · log m) |
| **Space** | O(1) |

## Alternative Approaches

- **Brute force:** try every rate `1..max(piles)`, summing hours each time: O(n · m) — up to 10⁹ × n operations. Never.
- **Micro-opt:** short-circuit inside `hours_needed` the moment the running total exceeds `h`. Real-world speedup on infeasible probes, but worst-case complexity is unchanged; adds a branch, kept out of the clean version.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Binary search on answer | **O(n · log m)** | **O(1)** | **Default — my solution already is it** |
| Brute force rate scan | O(n · m) | O(1) | Never |

**Interview answer:** The answer's feasibility is monotone in the rate, so binary search the rate itself in `[1, max(piles)]`: compute total hours with ceiling division per pile; if it fits in `h`, try smaller (`r = mid`), otherwise go faster (`l = mid + 1`). O(n log m) time, O(1) space.

## Edge Cases

- **`h == len(piles)`** → answer is `max(piles)`: one pile per hour, no hour to spare.
- **`h` very large** → answer is `1` (l never needs to leave the floor).
- **Single giant pile** (`[10⁹]`, h = 2) → `5·10⁸`; ceiling division rounds *up* one extra hour for the final partial.
- **Rounding behavior** (`[2, 2, 2]`, h = 4): rate 1 → 6 hours (no), rate 2 → 3 hours (yes) → answer `2`.
- **Discipline check:** `l` starts at `1`, never `0` — rate 0 divides by zero.
- **`h < len(piles)`** → excluded by constraints; if it ever happened, the code silently returns `max(piles)` as the least-bad rate rather than signaling infeasibility — add a guard only if inputs are untrusted.
- **Overlap quirk:** finishing a pile early strands the remaining hour (e.g. pile of 3 at rate 4 still costs a whole hour) — the ceiling logic models this correctly.
