# Car Fleet

**Problem:** `n` cars drive toward `target` along a one-lane road, each at its own constant speed. A faster car can never pass a slower one ahead; it catches up and then drives bumper-to-bumper at the slower car's speed for the rest of the way — those cars form one **fleet** (a lone car is also a fleet). Return the number of fleets that reach the target.

**Links:** [NeetCode 853](https://neetcode.io/problems/car-fleet) · [LeetCode 853](https://leetcode.com/problems/car-fleet/)

---

## My Solution — Monotonic Stack of Arrival Times

Sort cars by position, closest to the target first, and compute each car's solo arrival time `(target - position) / speed`. Walking from the target outward, push each time onto a stack; whenever the new time is `<=` the time below it, the car catches the fleet ahead before (or exactly at) the target — pop it, because the fleet ahead's time now represents the merged fleet. Whatever survives on the stack is one time per fleet, so its length is the answer.

| | |
|---|---|
| **Time** | O(n log n) — the sort dominates; the scan is O(n) since each time is pushed and popped at most once |
| **Space** | O(n) — sorted pairs plus the stack |

**Caveat:** The `while` can never pop more than once per car — the stack is strictly increasing bottom → top, so after one pop the invariant already holds. It is equivalent to an `if`. Also note `<=` (not `<`): catching the car ahead exactly at the target still counts as one fleet. If float precision ever worries you, compare cross products `(target - p1) * s2` vs `(target - p2) * s1` instead of dividing.

## Optimal Solution — Monotonic Stack (Same Idea, Polished)

The posted solution is already the optimal approach. The optimal file keeps the identical logic, expressed as a skip-instead-of-pop `if`.

| | |
|---|---|
| **Time** | O(n log n) |
| **Space** | O(n) |

```python
stack = []  # one arrival time per fleet, strictly increasing bottom -> top

for p, s in sorted(zip(position, speed), reverse=True):
    t = (target - p) / s
    if stack and t <= stack[-1]:
        continue  # catches the fleet ahead -> same fleet
    stack.append(t)

return len(stack)
```

Sorting is unavoidable — whether a car catches up depends on the car directly ahead of it, so position order is required. The O(n) scan over the sorted cars is then optimal.

## Alternative Approaches

- **Monotonic stack (my solution / optimal):** O(n log n) time, O(n) space. Canonical interview answer.
- **Running max (stack collapsed):** the stack top is always the max time seen so far, so the whole stack reduces to one `best` variable — count a new fleet whenever `t > best`. O(n log n) time, **O(1)** extra space beyond the sort:

  ```python
  count = best = 0
  for p, s in sorted(zip(position, speed), reverse=True):
      t = (target - p) / s
      if t > best:
          count += 1
          best = t
  return count
  ```

- **Simulation:** repeatedly advance all cars one time step, capping each speed at the car ahead's. O(n²) and fiddly. Only for building intuition.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Monotonic stack | **O(n log n)** | O(n) | **Default interview answer** |
| Running max | O(n log n) | **O(1)** | Follow-up: "can you drop the stack?" |
| Simulation | O(n²) | O(1) | Never — only for comparison |

**Interview answer:** Sort cars by position descending (closest to the target first). Compute each car's time to target; a car merges into the fleet ahead when its time is ≤ that fleet's time, otherwise it leads a new fleet. Keep the fleet times on a stack and return its size — or note the stack is just a running max and count the leaders. O(n log n) time, O(n) space.

## Edge Cases

- **Single car** → `1` fleet.
- **All cars the same speed** → nobody ever catches anyone → `n` fleets.
- **Slow leader, fast followers** → `target=100, position=[0,2,4], speed=[4,2,1]` → everyone piles up behind the slow lead car → `1` fleet.
- **Exact tie at the target** → `target=10, position=[8,0], speed=[2,10]`: both take time `1` → `1` fleet (`<=` handles the boundary).
- **No catch-ups** → `target=10, position=[6,8], speed=[3,2]` → `2` fleets.
- **Empty input** → `0` (LeetCode guarantees at least one car, but the code handles it).

---

## Testing

```bash
python3 - <<'PY'
import sys
sys.path.insert(0, "stack/car-fleet")
from my_solution import Solution as Mine
from optimal_solution import Solution as Optimal

cases = [
    # (target, position, speed, expected)
    (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),  # LeetCode example 1
    (10, [3], [3], 1),                           # single car
    (100, [0, 2, 4], [4, 2, 1], 1),              # slow leader, everyone piles up
    (10, [6, 8], [3, 2], 2),                     # no catch-ups
    (10, [8, 0], [2, 10], 1),                    # exact tie at the target
    (10, [0, 4, 2], [2, 2, 1], 2),               # middle car catches the leader
    (10, [], [], 0),                             # empty (outside constraints)
]

for target, position, speed, expected in cases:
    assert Mine().carFleet(target, position, speed) == expected
    assert Optimal().carFleet(target, position, speed) == expected

print("All tests passed")
PY
```
