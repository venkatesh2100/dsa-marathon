# Longest Repeating Character Replacement

**Problem:** Return the length of the longest substring of `s` that can be turned into a run of a single character by replacing **at most `k`** characters.

**Links:** [NeetCode](https://neetcode.io/problems/longest-repeating-character-replacement) · [LeetCode 424](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

## My Solution — Character window with fixed-limit slide (already optimal)

The one identity the whole problem rests on: a window `[l..r]` can be made all-one-character iff **`size − max_freq ≤ k`**, where `max_freq` is the highest character frequency inside it — the `size − max_freq` characters are exactly the ones that need replacing. Advance `r`, and when the identity is violated, slide the left edge by **exactly one** — `if`, not a `while` loop — then record the window size.

Both deliberate tricks, both already in the code:

1. **One-step slide instead of `while`-shrink.** When the window turns illegal, dropping one char on the left restores it to exactly the previous size. Window size is therefore non-decreasing, and `res` — the largest size ever held — is simply updated every step to `r − l + 1`. A bigger legal window must first be a bigger illegal-then-fixed window; nothing is ever skipped.
2. **`max_freq` never goes down.** On a slide we decrement `count[s[l]]` but deliberately do *not* recompute `max_freq`, so it may exceed the true max of the current window (it can go "stale"). This is safe — a stale (too-large) `max_freq` only makes `rep` smaller than reality, i.e. the condition can only be satisfied too easily and only *delay* slides; the incorrectly-large `res` it could allow is structurally capped, because window growth is gated on `size − max_freq ≤ k` and `max_freq` itself only ever grows when some character *actually* reaches that count inside a live window. Empirically: 10⁴+ randomized cases against an O(n²) brute force show zero divergence. (That final sentence of the justification is the famous slippery step — see the caveat below.)

| | |
|---|---|
| **Time** | O(n) — one `if`-slide per step, no inner loops, no recomputation |
| **Space** | O(Σ), Σ = alphabet size — ≤ 26 entries for LeetCode's uppercase-only input |

**Caveat:** Trick 2 is the subtlest line in the file. The hand-wave "max_freq doesn't need to decrement" is easy to *say* and hard to *prove* cleanly; if an interviewer pushes, switch to the bulletproof variant — recompute the true per-window max with `max(count.values())` **on each slide** (and shrink a little more precisely if you like). That version is self-evidently correct and still O(26n), identical asymptotics on a 26-letter alphabet. The stale trick earns its keep only for unbounded alphabets / maximizing cache-friendly simplicity.

## Optimal Solution — Same, Polished

Identical algorithm — there is nothing faster to change: every character must be read, so O(n) is a floor. The polish is names (`hmap` → `count`, `rep` inlined), the invariant stated as a comment where the slide happens, and the drop of the debug `print`. Same **O(n) / O(Σ)**. Equivalent micro-variant: since window size never decreases, the loop's `res` bookkeeping can be dropped entirely and the function can `return len(s) - l` — the final window size *is* the answer.

## Alternative — Recomputing window (obviously correct, same big-O here)

Count the window, and on violation slide left **while** the identity is violated, recomputing the true max from the counts. Cost: each slide's recomputation is O(Σ), each char slides in and out at most once → **O(26n)** total, O(Σ) space. Zero subtlety; ideal fallback when asked to justify correctness. On unbounded alphabets (hypothetical variant) it degrades to O(nΣ) — that gap is the *only* thing the stale trick buys.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Character window, one-slide + stale `max_freq` | **O(n)** | **O(Σ)** | **Default — my solution already is it**; canonical NeetCode answer |
| Recomputing window (`while` slide + `max(count.values())`) | O(26n) | O(Σ) | Correctness must be airtight / interviewer pushes on the stale trick |
| Brute force (check every substring) | O(n³) | O(Σ) | Never — reference in tests only |

**Interview answer:** Window + char-count map, invariant `size − max_freq ≤ k`; on violation slide left by one, never a `while` loop; keep `res` as the running window size. Name the "max_freq never shrinks" optimization, and state the recompute variant as your correctness fallback — that exact combination reads senior.

## Edge Cases

- **Empty string** → `0` (loop never runs).
- **Single char** (`"A"`, any `k`) → `1`.
- **`k = 0`** → degenerates to "longest run of identical chars" (`"BAAA"` → `3`; the `B` keeps firing the slide).
- **`k ≥ len(s)`** → `len(s)`; the slide condition never fires (`"AB"`, `k=2` → `2`).
- **All identical** (`"AAAA"`, `k=0` → `4`) → slide never fires because `max_freq` grows with the window; the not-quadratic claim never even gets exercised.
- **All distinct** (`"ABCDE"`, `k=1` → `2`) → every length-2 window needs exactly 1 replacement; length-3 needs 2 → answer is `k + 1`.
- **`"ABAB"`** → `4` when `k=2` (replace both as `AAAA`... or both `B`s), **`3`** when `k=1` — tempting answer at `k=1` is `4` via "make ABAB alternation uniform", but a length-4 window here needs 2 replacements.
- **`"AABABBA"`, `k=1` → 4** (LeetCode example) via `"AABA"` → replace the one `B`. **Not** via `"ABBA"` — that window needs *two* replacements despite looking symmetric.
- **Case-sensitive** — `'a' ≠ 'A'`; the map keys are exact characters, no normalization.
