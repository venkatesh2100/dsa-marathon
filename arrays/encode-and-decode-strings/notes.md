# Encode and Decode Strings

**Problem:** Design `encode(strs)` and `decode(s)` so that a list of strings can be serialized to a single string and reconstructed exactly: `decode(encode(strs)) == strs`. The strings may contain any characters.

**Links:** [NeetCode 271](https://neetcode.io/problems/string-encode-and-decode) · [LeetCode 271](https://leetcode.com/problems/encode-and-decode-strings/)

---

## My Solution — Character Ordinals + Delimiters

Encode every character as its decimal ordinal followed by `#`, and terminate each word with `-`. Decode by scanning to `#` to grab an ordinal, and to `-` to finish a word. An empty list maps to `""`, while `[""]` maps to `"-"`, so the two stay distinct.

| | |
|---|---|
| **Time** | O(N) conceptually, O(N²) as written |
| **Space** | O(N) |

Where `N` is the total number of characters.

**Caveats:**

- **String concatenation in a loop:** `ans += ...` repeatedly rebuilds the string. CPython sometimes optimizes this, but the safe bound is O(N²). Collect pieces in a list and `"".join(...)` instead.
- **Encoded size inflation:** every character becomes up to 3 digits plus `#`, so the payload can grow ~4×.
- **Correctness is fine** because the encoder only ever emits digits, `#`, and `-`, so no input character can be mistaken for a delimiter.

## Optimal Solution — Length-Prefixed Chunks

For each word, write its length, a `#`, then the word itself: `"5#hello"`. Decoding reads the length, skips the `#`, and slices exactly that many characters. Because the length is explicit, any character — including `#`, `-`, or digits — is safe inside a word.

| | |
|---|---|
| **Time** | O(N) |
| **Space** | O(N) |

```python
parts.append(f"{len(s)}#{s}")
return "".join(parts)
```

No sentinel is needed: `[]` encodes to `""`, and `[""]` encodes to `"0#"`, so they remain distinct.

## Alternative Approaches

- **Escaping delimiters:** Choose a delimiter and escape occurrences inside words. Works, but escaping logic is fiddly and easy to get wrong.
- **JSON / `str(list)`:** Trivially works in Python, but it is a library shortcut — not what the interviewer is testing.
- **Character ordinals (my solution):** Correct, but inflates the payload and needs care with string building.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Length-prefixed chunks | **O(N)** | O(N) | **Default answer** — safe for any characters |
| Character ordinals | O(N²) as written | O(N) | Works, but avoid the `+=` loop |
| Escaped delimiters | O(N) | O(N) | If the format must stay human-readable |
| JSON / repr | O(N) | O(N) | Prototyping only, not in an interview |

**Interview answer:** Prefix every string with its length and a separator, then concatenate. Decoding reads the length, slices that exact number of characters, and moves on — O(N) time, O(N) space, and it works for arbitrary characters.

## Edge Cases

- `[]` → encodes to `""` → decodes to `[]`.
- `[""]` → encodes to `"0#"` (optimal) or `"-"` (mine) → decodes to `[""]`; must not be confused with `[]`.
- `["", ""]` → two empty strings, preserved.
- Words containing `#`, `-`, or digits → length prefix handles them; naive delimiter splitting would break.
- Unicode / multi-byte characters → Python string length and slicing operate on code points, so both solutions round-trip.
- Very long single word → length prefix reads it in one slice; O(N).
