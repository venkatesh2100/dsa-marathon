# Merge Two Sorted Lists

**Problem:** Merge two ascending singly linked lists into one ascending list by *relinking the same nodes* and return its head.

**Links:** [NeetCode](https://neetcode.io/problems/merge-two-sorted-linked-lists) · [LeetCode 21](https://leetcode.com/problems/merge-two-sorted-lists/)

---

## My Solution — Dummy-head iterative splice (already optimal)

The dummy-node trick: `ans = ListNode(0)` is a throwaway guard, and cursor `res` walks behind it. Each step compares the two live heads, splices the smaller one onto `res` (`<=` means list1 wins ties — the merge is then *stable*), and advances that list. When one list runs dry, two drain loops append the survivor's remainder. Return `ans.next` — the dummy's job is done, and "return the head" becomes trivial: there is no special case for which list happened to be smaller, or for empty inputs.

| | |
|---|---|
| **Time** | O(n + m) — every loop iteration splices exactly one node; each of the n + m nodes is spliced exactly once |
| **Space** | O(1) — the *only* allocation is the disposable dummy; the output chain is the original nodes relinked |

**Caveat:** No asymptotic one. The risk is boilerplate-shape: two separate drain loops, each three lines that all have to be right (advance `list1`/`list2`, advance `res`, or the chain forks/cycles). Neither is logically complex — but the drain phase is exactly the kind of repeated tail code that grows a bug. The polished version collapses both loops into one comparison.

## Optimal Solution — Same, Polished

Identical algorithm — it cannot be beaten: each output node must be examined once, so O(n + m) is the floor, and the nodes are relinked rather than copied, so O(1) extra stands. Polish: `ans`/`res` → the standard `dummy`/`tail` idiom, and the two drain loops collapse to **`tail.next = list1 if list1 else list2`** — the survivor is *already sorted*, so splicing its remaining prefix in one piece *is* the drain, done in a single assignment. Same **O(n + m) / O(1)**.

## Alternative — Recursion

Base cases: either list empty → return the other. Otherwise the smaller head wins and its `next` becomes the recursive merge of the rest: `list1.next = self.mergeTwoLists(list1.next, list2)`. O(n + m) time, but **O(n + m) call-stack**. Note the honest nuance: this problem's constraints cap each list at ~50 nodes, so recursion is *perfectly safe here* — the O(n) stack trap (and Python's ~1000-frame `RecursionError`) only bites when the pattern is reused on unbounded lists, as in [Reverse Linked List](../reverse-linked-list/notes.md).

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Iterative dummy splice | **O(n + m)** | **O(1)** | **Default — my solution already is it**; in-place, no stack risk |
| Recursive | O(n + m) | O(n + m) stack | Fine at interview size; flag the stack cost yourself |
| Copy values → build new nodes | O(n + m) | O(n + m) | Never — allocates and fails the relink expectation |

**Interview answer:** Dummy head + tail cursor, splice the smaller head per step, attach the survivor whole. Say "O(n + m) time, O(1) space, same nodes relinked, stable on ties." If asked to recurse: one line per branch, but it costs a frame per node.

## Edge Cases

- **Both lists empty** → `None` (dummy's `next` never set — falls out for free with the dummy pattern).
- **One list empty** → the other returned **unchanged**: main loop never runs, drain attaches the whole survivor; identity of every node preserved.
- **Non-overlapping ranges** (`[1,2,3]` + `[4,5]`) → main loop does nothing to list2; the drain does all the work — the code path most likely to break in a botched drain.
- **Fully interleaved** (`[1,3,5]` + `[2,4,6]` → `[1,2,3,4,5,6]`) → alternates branches every step.
- **Duplicates everywhere** (`[1,1,1]` + `[1,1]` → five `1`s) → content is indistinguishable; correctness shows up only as tie *stability*: ties pull from list1 first, so list1's nodes lead the merged chain.
- **Negative values** (`[-3,-1]` + `[-2,0]` → `[-3,-2,-1,0]`).
- **Single nodes each** → one main-loop step, one dummy advance.
- **In-place identity** → output chain ids == exact union of both lists' node ids: no node copied, lost, doubled, and the dummy itself is not in the chain (its id never appears in the input sets).
