# Word Search

**Problem:** Given an `m × n` grid of characters and a string, return `True` if `word` can be traced by moving to horizontally/vertically adjacent cells, using each cell **at most once**.

**Links:** [NeetCode](https://neetcode.io/problems/search-for-word) · [LeetCode 79](https://leetcode.com/problems/word-search/)

---

## My Solution — DFS with a visited set

From every cell matching `word[0]`, DFS outward: each call validates the cell (bounds → char match → not already on the current path), marks it in a `vis` set, tries all 4 neighbors with `idx + 1`, and unmarks on backtrack. The `idx == len(word)` base fires only after the *previous* cell matched `word[-1]`, so a full match is a real one.

| | |
|---|---|
| **Time** | O(m · n · 4ᴸ) — L = len(word); every start cell spawns a depth-L branchwalk. (After the first step it's really ≤ 3ᴸ — you can't return to where you came from) |
| **Space** | O(L) — recursion depth + the visited set (one entry per path cell) |

**Caveat:** `vis.add`/`remove` on tuples costs hashing per step; the classic alternative is marking the board cell in place (`"#"`) and restoring it — same complexity, faster constants, temporarily mutates the grid during the call (fully restored on return). Also, the neighbor loop recurses even into out-of-bounds cells; the bounds check catches them one frame later — harmless but one stack frame per wasted probe.

## Optimal Solution — Same DFS, board marking instead of a set

Identical search; the cell is marked by writing `"#"` (which matches no letter) into `board[r][c]` and restored to `word[idx]` after the four probes. No set, no tuples, no hashing — the board itself is the visited array, and the symmetric mark/restore leaves it untouched after the call.

| | |
|---|---|
| **Time** | O(m · n · 4ᴸ) |
| **Space** | O(L) — recursion stack only |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| DFS + in-place marking (optimal) | O(m · n · 4ᴸ) | O(L) stack | **Default answer** — fastest constants, board restored on return |
| DFS + visited set (my solution) | O(m · n · 4ᴸ) | O(L) stack + set | When the input must not be touched even transiently (e.g., threaded reads) |
| BFS / brute-force all paths | worse | — | Never — path state is inherently depth-first |

**Interview answer:** “DFS from every cell; mark the current cell (in place or via a set), probe 4 neighbors for `idx+1`, unmark on backtrack. O(m·n·4ᴸ) worst case, O(L) stack.”

## Edge Cases

- **Single cell board** → matches only a 1-char word.
- **Word longer than m·n** → `False` immediately in principle (each cell once); the search exhausts without finding it.
- **Same cell twice forbidden** (`[["a","a"]]`, word `"aaa"`) → `False` — this is what marking prevents.
- **Snake path** (word zig-zags across neighbors) → the 4-direction recursion covers it.
- **All-same-letter board** (`[["A","A"],["A","A"]]`, `"AAAA"`) → marks prevent path loops; `False` when the shape doesn't allow length 4... it does here, actually `True` via a snake — the marking is what makes the search terminate.
- **Word with repeated letters needing different cells** → handled: cells are consumed one at a time.
- **No starting cell matches `word[0]`** → `False` (my version short-circuits this in the outer loop).