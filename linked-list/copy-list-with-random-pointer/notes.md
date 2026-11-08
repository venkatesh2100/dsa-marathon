# Copy List with Random Pointer

**Problem:** Deep-copy a linked list whose nodes carry both a `next` pointer and a `random` pointer that can point anywhere in the list (or `None`); return the head of the new copy, with originals untouched.

**Links:** [NeetCode](https://neetcode.io/problems/copy-linked-list-with-random-pointer) · [LeetCode 138](https://leetcode.com/problems/copy-list-with-random-pointer/)

---

## My Solution — Two-pass old→new hash map (optimal in time; O(n) space)

Pass 1 clones every node *bare* — no wiring — and records the pair in `old_to_new`. Pass 2 walks the originals again and wires each clone through the map: `copy.next = old_to_new[curr.next]` and `copy.random = old_to_new[curr.random]`.

The quiet trick is pre-seeding `old_to_new = {None: None}`: both fields can then be raw dict lookups with zero branching, since "next/random is `None`" (tail, original-less random) resolves to `None` through the map automatically. And the two passes aren't a luxury — randoms point **forward** (up the list) as freely as backward, so any wiring done mid-clone travels into clones that don't exist yet. Building the whole map first makes pointer direction irrelevant.

| | |
|---|---|
| **Time** | O(n) — two linear passes, constant work per node |
| **Space** | O(n) — one map entry per node, plus the clones themselves |

**Caveat:** None asymptotic — this is the canonical answer. The practical one is conversational: this problem is *famous* for its follow-up, "can you do it without the extra map?" — be ready to walk into the O(1) version below. (Note unlike LeetCode 19, `sz = 0` is a legal input here, so the `if not head: return None` guard is reachable and correct as written.)

## Optimal Solution — Interweave, then split (O(1) extra space)

Skip the map by making the list *itself* the map — each clone is threaded directly after the node it clones (`A → A' → B → B'`), so "the clone of `X`" is always `X.next`:

1. **Weave:** `curr.next = Node(curr.val, curr.next)` inserts the clone mid-chain; hop by `next.next`.
2. **Wire randoms:** the clone of `curr.random` now sits one hop right of it, so `curr.next.random = curr.random.next`. Self-randoms and forward randoms come free — originals never get physically moved, only their `next` re-threaded.
3. **Split:** sweep through once peeling copies into their own list while restoring every original's `next` — two re-links per braid step.

Same **O(n) time**, but the bookkeeping that dwarfed the map lives *inside* the output nodes, so auxiliary space is **O(1)** — the famous follow-up answer. Deleting the `{None: None}` trick's guarantee means the random step needs its explicit `if curr.random` (the weave inserts no clone for `None`).

## Alternative — Recursion with a memo map

Clone `head` recursively, memoizing in the same old→new dict, so the wiring is inline. O(n) time, but **O(n) × 2** space (map *and* call stack) — and the call stack is the trap: Python's ~1000-frame default is right at this problem's legal maximum (`sz = 1000`), so deep lists can `RecursionError` (see [Reverse Linked List](../reverse-linked-list/notes.md)). Treat it as understanding-only.

## Brute force — Index-walk twice

Build the plain next-chain (O(n)), then to set each copy's random, walk the original from head while counting steps to the target, then walk the copy list that many steps. **O(n²) time, O(1) space** — no trick, no map, quadratic isn't a conversation-stopper even though the constraint sizes would let you get away with it.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Two-pass old→new map | **O(n)** | O(n) | **Default answer** — the expected first solution |
| Interweave + split | **O(n)** | **O(1)** | Say it *second* — when asked to drop the map |
| Recursion with memo | O(n) | O(n) + O(n) stack | Never — same stack trap as Reverse Linked List |
| Index-walk brute force | O(n²) | O(1) | Never — only to show what the tricks buy |

**Interview answer:** Two passes with an `old → new` dict: first clone every node bare (with `None` pre-seeded as a key, so final wiring is branch-free dict lookups), then wire `next` and `random` through the map — **O(n) time, O(n) space**. When asked for constant space: weave each clone directly after its original — clone of `X` is `X.next` — wire `copy.random = cur.random.next`, then split the braid back into two clean lists, same O(n) time, O(1) extra.

## Edge Cases

- **Empty list** → *legal here* (LeetCode notes `sz = 0`); return `None` — my solution's guard is correct.
- **Single node, `random → itself`** (`[[7,0]]`) → clone's random is its *own* clone — map pass resolves it, weave pass via `curr.random.next`.
- **`random → None`** → resolved by the seeded `{None: None}` key (or the weave's explicit `if`); remap must yield `None`, not skip the assignment.
- **Forward randoms** (`[[1,4],[2,3],[3,2],[4,1],[5,0]]`) → the reason cloning bare first is mandatory — pass 2 wires into clones that didn't exist while pass 1 ran.
- **Duplicate values** (`[[3,0],[3,0],[3,0]]`) → matching is by node identity via the dict keys, never by value; test that the copy's node ids and the original's share no single object.
- **Original integrity** → hash-map version never touches the originals at all; the weave version rewrites `next` mid-call (the caller sees a braid if it peeked — unobservable contract) but must restore them fully — assert the input structure after the call.
- **Long list (`sz = 1000`)** → both iterative passes are fine; the recursive memo alternative is right at Python's ~1000-frame cap.
- **Return contract** → return the *clone* of head (`old_to_new[head]`), never `head` itself — the copy sharing zero node objects with the input is the whole point of "deep".
