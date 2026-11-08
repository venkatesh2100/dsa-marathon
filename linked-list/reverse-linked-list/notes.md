# Reverse Linked List

**Problem:** Reverse a singly linked list *in place* and return the new head (`[1,2,3,4,5]` → `[5,4,3,2,1]`, same node objects relinked).

**Links:** [NeetCode](https://neetcode.io/problems/reverse-a-linked-list) · [LeetCode 206](https://leetcode.com/problems/reverse-linked-list/)

---

## My Solution — In-place three-pointer walk (already optimal)

Flip one arrow per step. `prev` is the head of the already-reversed prefix, `curr` is the first still-unprocessed node. Each iteration: capture `curr.next` into `temp` **first**, then flip the arrow (`curr.next = prev`), then shift both pointers one node right (`prev = curr; curr = temp`). When `curr` walks off the end, `prev` is sitting on the new head. Only three pointers ever exist and the loop touches each node a constant number of times.

| | |
|---|---|
| **Time** | O(n) — one pass, constant work per node |
| **Space** | O(1) — three pointer variables, nothing allocated |

**Caveat:** No asymptotic one. The danger here is pure correctness traps, and the code dodges all three: (1) `temp = curr.next` **must** run before the flip — assigning `curr.next = prev` first destroys the only reference to the rest of the list; (2) `prev` starts as `None`, not a dummy — the original head must become the new tail pointing at nothing; (3) the loop condition is `while curr`, not `while curr.next` — the latter silently returns `None` for a single-node list because the node count is `k` edges, but there are `k + 1` nodes to flip.

## Optimal Solution — Same, Polished

Identical algorithm — it cannot be beaten: every node must be visited (O(n) floor) and O(1) extra space is the best possible for a pointer-swap reversal. Polish: `temp`/parallel-assignment renames, the capture-first trap spelled out where it bites, dropped stray whitespace. Same **O(n) / O(1)**.

## Alternative — Recursion (elegant, but real cost)

Base case: `head is None` or `head.next is None` → return `head`. Otherwise recurse on `head.next`, then `head.next.next = head; head.next = None`, return the new head from the base. O(n) time — but **O(n) call-stack space**, and in Python specifically that is not just a cost, it's a crash: the default recursion cap is ~1000 frames, while realistic list lengths (LeetCode allows 5·10³) raise `RecursionError` where the iterative version runs untouched. Know it for the "do it recursively" follow-up; don't lead with it in Python.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Iterative three pointers | **O(n)** | **O(1)** | **Default — my solution already is it**; in-place, no overflow risk |
| Recursive | O(n) | O(n) stack | Only when explicitly asked for recursing; mention the stack cost yourself |
| Copy values → rebuild | O(n) | O(n) | Never — allocates new data and fails the "in place" expectation |

**Interview answer:** Three pointers, flip one arrow per node, capture `next` before flipping; say "O(n) time, O(1) space, truly in place — same nodes relinked." If recursion comes up: same idea one node deep at a time, but O(n) stack, and in Python that's a real `RecursionError` risk on long lists.

## Edge Cases

- **Empty list** (`head = None`) → `None` (loop never runs; `prev` initialized to `None`).
- **Single node** → returns **the same node**; its `next` was already `None` and the flip re-writes exactly that.
- **List with duplicate values** (`[7,7,7]`) → "reversal" is only verifiable by node identity, not values; tests must check object ids, not contents.
- **Two nodes** (`[1,2]` → `[2,1]`) → smallest case that exercises a *middle* flip where both wrong loop conditions diverge from correct behavior.
- **In-place identity** → the returned chain contains the same node objects as the input (sorted `id()` lists equal), post-reversal `head.next is None` on the original head — the "no new nodes" claim holds literally.
- **Long list (thousands of nodes)** → iterative fine; this is exactly the input length where the recursive variant would crash Python's stack.
