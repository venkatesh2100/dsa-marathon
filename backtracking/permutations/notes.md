# Permutations

**Problem:** Given an array of **distinct** integers, return all possible orderings (permutations) of it, in any order.

**Links:** [NeetCode](https://neetcode.io/problems/permutations) · [LeetCode 46](https://leetcode.com/problems/permutations/)

---

## My Solution — Backtracking with a `used` array

Fill positions one at a time: at each depth, scan all indices and take every element not yet used (`used[i]`), recurse, then undo (`pop` + clear the flag). When `len(sub) == len(nums)` the buffer is a full permutation — copied into `res`.

| | |
|---|---|
| **Time** | O(n · n!) — n! permutations, each copied in O(n) at its leaf |
| **Space** | O(n) auxiliary — `used` flags + `sub` buffer + recursion depth; output adds O(n · n!) |

**Caveat:** None algorithmic — this is the canonical optimal. Same load-bearing copy rule as Subsets: `res.append(sub)` without the slice would record a shared buffer that keeps mutating, leaving every permutation empty. Only works as-is for *distinct* elements — with duplicates it emits repeated permutations (see Permutations II).

## Optimal Solution — Same, polished

Identical `used`-array recursion — already optimal, since the output size *is* the Θ(n · n!) lower bound.

| | |
|---|---|
| **Time** | O(n · n!) |
| **Space** | O(n) auxiliary + O(n · n!) output |

### Alternative — Swap-in-place (no `used` array)

Recursion index `i` splits the array into a fixed prefix and a free suffix; swap `nums[i]` with every `nums[j]` (`j ≥ i`), recurse on `i + 1`, swap back. Same O(n · n!) time, and it drops the `used` flags — at the cost of mutating `nums` during the call (restored by the symmetric swaps).

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| `used`-array backtracking (optimal) | **O(n · n!)** | **O(n)** aux | **Default answer** — clearest, generalizes to Permutations II |
| Swap-in-place | O(n · n!) | O(1) aux (besides output) | Follow-up "no extra flags"; mutates/restores input |
| `itertools.permutations` | O(n · n!) | O(n · n!) | Never in an interview — say "I'd write it out" |

**Interview answer:** “Backtrack: try every unused element in the next slot, recurse, undo. n! leaves × O(n) copy = O(n · n!) time, O(n) extra space.”

## Edge Cases

- **Empty input** → `[[]]` — the empty permutation; the base case fires immediately.
- **Single element** → `[[x]]`.
- **All distinct** (LC guarantee) → exactly n! unique permutations.
- **Permutations II follow-up (duplicates)** → sort + skip `nums[i] == nums[i-1]` when `not used[i-1]` (or when at the same branch level); copy-at-leaf unchanged.
- **Large n** → n! explodes past n ≈ 10; flag the combinatorial wall.
- **Negative / zero values** → irrelevant; only positions matter.