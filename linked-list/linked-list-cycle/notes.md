# Linked List Cycle

**Problem:** Return `True` iff the linked list's tail points back to some earlier node (`pos` = index the tail connects to; `pos = -1` means no cycle).

**Links:** [NeetCode](https://neetcode.io/problems/linked-list-cycle-detection) · [LeetCode 141](https://leetcode.com/problems/linked-list-cycle/)

---

## My Solution — Floyd's tortoise and hare (already optimal)

Two pointers walk the list at different speeds: `slow` steps 1 per round, `fast` steps 2 (`fast.next.next` each round, hence the `fast and fast.next` guard). If the list is acyclic, `fast` falls off the end and the guard's `fast.next` is the failure — return `False`. If there's a cycle, fast eventually laps: once both pointers are inside the cycle, fast closes the gap by exactly **1 node per round** (its 2-step vs slow's 1-step in the same lap direction), so the gap cannot be perpetually skipped — it must hit 0, and `slow is fast` returns `True`.

Two form choices, both fine in this code: `fast` starts at `head.next` (equivalent correctness to starting both at `head` and comparing before stepping — the ordering of compare-vs-step just shifts which round the meeting lands in), and the equality check sits at the top of the loop rather than after the steps.

| | |
|---|---|
| **Time** | O(n) — fast hits `None` or catches slow within ~n + cycle rounds; gap math guarantees closure |
| **Space** | O(1) — two pointers, nothing stored |

**Caveat:** The one structural must: `slow == fast` compares **object identity**, and here it happens to write `==`, which on `ListNode` without `__eq__` falls back to identity — correct but fragile. If someone later adds a value-based `__eq__` to the class (very plausible in real codebases), `==` starts comparing *values* and the whole algorithm silently breaks: in ragged lists ~two pointers can briefly... two *distinct nodes with equal values* would falsely report a cycle. The polished version writes `slow is fast` to make the invariant explicit. Worth 2 seconds of interview airtime; otherwise identical to the polish.

## Optimal Solution — Same, Polished

Identical algorithm — proven optimal form: detection must terminate for both acyclic and cyclic inputs and can't beat O(n) pointers-walk / O(1) space (a set-based solution is the natural alternative and costs O(n) space). Polish: the explicit `head == None` prologue is absorbed by the loop guard (`fast` starts `None` with an empty list → loop skipped → `False`), names `slow`/`fast`, and the identity check spelled `slow is fast` for the reason in the caveat above.

## Alternative — Hash set of visited nodes (the readable fallback)

Append each node's `id` to a set as you walk; revisit any node → cycle. O(n) time like Floyd's, but **O(n) space** — the hint Haiyan's comparison exists. Its virtues are real, though: it's obviously correct, trivially causes **finding the cycle's entry node** (the hexagonal bugger: later `head.next`... simply record the first node seen twice), and has no gap-closure argument to defend. Reach for it when you misremember the two-pointer proof under interview pressure.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Floyd's tortoise &hare | **O(n)** | **O(1)** | **Default — my solution already is it**; canonical answer, zero allocation |
| Visited-node hash set | O(n) | O(n) | Readable fallback; extend it to find the entry node in one more line |
| Brute force / counting steps | — | — | Never — no bounded-step budget proves absence of a cycle |

**Interview answer:** Tortoise and hare: slow +1, fast +2, `fast and fast.next` guard against the acyclic exit, meet ⇒ cycle in O(n)/O(1). Follow-ups to have loaded: *why can't fast jump over slow?* — the gap shrinks by exactly 1 per round, and 1-step closure means it lands on the pointer, not past it. *"Find the entry?"* → reset one pointer to `head`, move both 1 step: they meet at the tail's target (the classic `2(a+b)`-distance derivation).

## Edge Cases

- **Empty list** (`head = None`) → `False` (yours handles it with the explicit prologue; the polish with the loop guard alone).
- **Single node, `next = None`** → `False`.
- **Single node pointing at itself** (`pos = 0`, LC's smallest cycle) → `True` — the trickiest small case for any variant that misorders compare/step; randomized battery covers it.
- **Two-node mutual cycle** (`[1,1]`, tail to head) → `True`; values are equal, so duplicate-valued nodes fully test object-identity correctness.
- **Acyclic list with all-equal values** (`[7,7,7]`) → `False` — equal *values* on distinct nodes must not fool identity-based checks.
- **Long tail, tiny cycle** (`[1..40]` tail connects back 2) → `True`; exercises fast's entry into the loop rather than a pure chase.
- **Long cycle** (thousands of nodes) → `True` in a handful of rounds regardless of gap start.
