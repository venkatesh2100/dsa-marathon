# Remove Nth Node From End of List

**Problem:** Given the head of a linked list and `n`, remove the nth node from the **end** and return the modified head — in one pass.

**Links:** [NeetCode](https://neetcode.io/problems/remove-node-from-end-of-linked-list) · [LeetCode 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

## My Solution — One-pass fast/slow with an n-wide gap (already optimal)

Count-free target finding: open a gap of exactly `n` nodes between `fast` and `slow`, both anchored at a dummy in front of the head, then advance them in lockstep. When `fast` reaches the last node, `slow` is standing on the node *before* the target, so `slow.next = slow.next.next` unlinks it in one line.

Why the math holds: after the gap loop `fast` sits on the nth node from the start; the list has `L` nodes, so lockstep advances exactly `L − n` times before `fast.next is None`. That lands `slow` at position `L − n + 1` (from the dummy), which is precisely the nth-from-end node — `slow.next = slow.next.next` drops it.

The dummy is the quiet hero: deleting the *first* node (when `n == L`) would otherwise be a head-reassignment special case; with the dummy it's the same `slow.next` re-link, and the return is `dummy.next` rather than `head` — which is load-bearing, not cosmetic: after deleting the head the original `head` variable still points at the unlinked node's stale subtree, so `return head` would hand back the whole untouched list.

| | |
|---|---|
| **Time** | O(n) — single traversal: `n` gap steps + `L − n` lockstep steps |
| **Space** | O(1) — two pointer variables plus the dummy |

**Caveat:** Two guard-level quirks, both papered over by LeetCode's constraints (`1 ≤ sz`, `1 ≤ n ≤ sz`). The gap-opening loop `for _ in range(n): fast = fast.next` has no bounds check — if `n > L`, `fast` walks off the tail and the next `fast.next` is an `AttributeError`; real code that can't trust its inputs should count the nodes or bound the gap walk. And the `if not head: return []` branch returns a Python *list*, not a `ListNode`, breaking the `Optional[ListNode]` contract — unreachable under the constraints (the list always has ≥ 1 node), but in an interview the right shape is `return None`, or no guard at all since the dummy logic degrades gracefully.

## Optimal Solution — Same, Polished

Identical algorithm. Polish: the dead `if not head` guard is dropped (the constraints make it unreachable, and it returned the wrong type anyway — the comment states the reliance on `1 ≤ n ≤ sz`), the dummy is built in one expression `ListNode(0, head)`, and the comments pin down what each pointer *means* at each moment (fast = nth from start, slow = node before target). Same **O(n) / O(1)**, single pass.

It can't be beaten asymptotically: you must look at every node (O(n) floor), and two pointers plus a dummy is the minimum bookkeeping (O(1) space).

## Alternative — Two-pass: count, then walk

Pass 1 counts `L`; pass 2 advances `L − n` steps from a dummy and unlinks. Same **O(n) / O(1)** asymptotically, but two traversals and a length variable. Correct and often clearer on a first pass of reasoning; in an interview it's worth volunteering only as a sanity check — this problem is famous *specifically* because one pass is offered as the follow-up challenge.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| One-pass fast/slow gap + dummy | **O(n)** | **O(1)** | **Default — my solution already is it**; the expected star answer |
| Two-pass (count then walk `L − n`) | O(n) | O(1) | Solid fallback if the gap trick doesn't surface mid-interview |
| Array of node refs → relink by index | O(n) | O(n) | Rescue mode — but you must splice links into the same nodes, not rebuild them |

**Interview answer:** Put a dummy in front of the head, open an `n`-wide gap between `fast` and `slow`, then advance both until `fast` hits the last node — `slow` now sits on the node before the target, unlink it with `slow.next = slow.next.next` and return `dummy.next`. One pass, O(1) space; the dummy deletes the head-deletion special case. Mention the `n ≤ length` reliance out loud — it shows you know where the code would break.

## Edge Cases

- **Empty input** → illegal per constraints (`sz ≥ 1`); LeetCode never sends it. My code's dead guard returns `[]` (a list — wrong type); the polished version would crash on the gap walk. Interview-correct behavior: return `None`.
- **Single node, `n = 1`** (`[1]` → empty, return `None`) → `slow` stays on the dummy, `slow.next = None` empties the list — *the* case the dummy exists for.
- **`n = length` (remove head)** → same single-node mechanic scaled up: zero lockstep steps, dummy leads.
- **`n = 1` (remove tail)** → `fast` never advances in the lockstep loop; chain rewires one earlier.
- **Middle removal** (`[1,2,3,4,5], n=2` → `[1,2,3,5]`) → the textbook case; gap lands `slow` on 3.
- **Duplicate values** (`[7,7,7,7], n=2` → `[7,7,7]`) → position-based, values irrelevant; verify by node identity, not values.
- **Node identity, not values** → the actual nth-from-end node object gets unlinked, and it's spliced out — not rebuilt or mutated (`slow.next.next` is left dangling into nothing; setting `removed.next = None` is optional hygiene).
- **Return contract** → return `dummy.next`, never `head`: after a head removal, `head` still points into the unlinked subtree and would silently hand back the unmodified list.
- **`n > length`** → illegal per constraints, but the gap loop would walk `fast` off the end and crash on `fast.next` — the one place a bounds check would be kind.
