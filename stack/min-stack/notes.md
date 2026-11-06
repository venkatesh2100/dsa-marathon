# Min Stack

**Problem:** Design a stack that supports `push`, `pop`, `top`, and `getMin` — retrieve the minimum element — all in O(1) time per operation. LeetCode guarantees `pop`/`top`/`getMin` are called only on a non-empty stack.

**Links:** [NeetCode 155](https://neetcode.io/problems/minimum-stack) · [LeetCode 155](https://leetcode.com/problems/min-stack/)

---

## My Solution — Synced Auxiliary Min Stack

Keep a second stack `mini` in lockstep with the main stack: `mini[i]` is the minimum of everything pushed up to (and including) depth `i`. Each `push` records `min(mini[-1], val)`; each `pop` pops both stacks, so after any number of operations `getMin` is just `mini[-1]`.

| | |
|---|---|
| **Time** | O(1) per operation |
| **Space** | O(n) — `mini` always holds exactly `n` entries |

**Caveat:** Always-correct and easy to reason about. Two refinements: the two `pop` calls must stay in lockstep (they only can crash together, which is fine under the problem's guarantee), and `mini` stores a full mirror of the stack even when the minimum rarely changes — the conditional variant below can shrink that.

## Optimal Solution — Conditional Min Stack

Push onto `mins` only when the new value is `<=` the current minimum; on `pop`, remove from `mins` only when the popped value equals it. The auxiliary stack now records just the minima actually in force, still O(1) per operation.

| | |
|---|---|
| **Time** | O(1) per operation |
| **Space** | O(n) worst case, typically much less |

```python
def push(self, val: int) -> None:
    self.stack.append(val)
    if not self.mins or val <= self.mins[-1]:
        self.mins.append(val)

def pop(self) -> None:
    if self.stack.pop() == self.mins[-1]:
        self.mins.pop()
```

The `<=` is not a typo: pushing a duplicate minimum twice must record it twice, otherwise the later `pop` would discard the minimum record while the same minimum is still on the stack. Worst case (strictly descending pushes) still stores `n` entries, so it does not beat O(n) asymptotically — O(1) time per operation plus O(n) total space is optimal for this problem, since any input can force a growing auxiliary structure.

## Alternative Approaches

- **Conditional min stack (optimal):** O(1) time, O(n) worst-case space. Standard interview answer.
- **Synced min stack (my solution):** O(1) time, O(n) space. Simplest correctness argument.
- **Tuple stack:** Store `(val, min_so_far)` pairs in a single stack. Same O(1)/O(n), one structure instead of two.
- **Encoded differences:** Push `val − previous_min` and recover using sign tricks (with overflow care). O(1) space beyond the data itself; exotic and easy to get wrong — only as a follow-up flourish.
- **Recompute on `getMin`:** Scan the whole stack per query. O(n) per `getMin`; violates the design goal.

---

## Which One to Pick

| Approach | Time (per op) | Space | When to use |
|---|---|---|---|
| Conditional min stack | **O(1)** | O(n) worst, less in practice | **Default interview answer** |
| Synced min stack (mine) | O(1) | O(n) always | Clearest to explain and verify |
| Tuple stack | O(1) | O(n) | Prefer one structure over two |
| Encoded differences | O(1) | O(1) extra | Only when asked to beat O(n) space |
| Scan for min | O(n) on `getMin` | O(1) | Never |

**Interview answer:** Two stacks: the main one, plus one storing the running minimum. Push the new value onto the min stack only when it is `<=` the current minimum; on pop, drop the min-stack top if it equals the popped value. Every operation is O(1) with O(n) worst-case extra space.

## Edge Cases

- **Single element** → `top == getMin == value`.
- **LeetCode example** (`push -2, 0, -3`; `getMin → -3`; `pop`; `top → 0`; `getMin → -2`).
- **Duplicate minimums** (`push 2, push 2, pop`) → `getMin` is still `2`; the `<=` push must record duplicates or the deletion logic breaks.
- **Minimum buried then popped** (`push 3, 1, 2, 1`) → pops recover `1 → 1 → 3`.
- **Descending pushes** (`3, 2, 1`) → every push extends the min stack, then pops unwind it.
- **Ascending pushes** (`1, 2, 3`) → min stack never grows after the first push (conditional variant).
- **Pop to empty, then reuse** → the min stack starts over on the next push.
- **Negative values and interleaved ops** → handled identically; only ordering relative to the running min matters.
- **Empty-stack calls** → prohibited by the constraints; defensive implementations could raise, not required here.
