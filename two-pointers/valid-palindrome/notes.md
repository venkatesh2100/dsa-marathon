# Valid Palindrome

**Problem:** Given a string `s`, return `true` if it reads the same forward and backward after lowercasing it and removing all non-alphanumeric characters.

**Links:** [NeetCode 125](https://neetcode.io/problems/is-palindrome) · [LeetCode 125](https://leetcode.com/problems/valid-palindrome/)

---

## My Solution — Filter, Then Compare with Reverse

Build a list of lowercased alphanumeric characters, then compare it against its reverse (`s[::-1]`). If the two match, the string is a palindrome.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

**Caveat:** This allocates two lists — the filtered list and the reversed slice. The reverse copy is unnecessary: two pointers can compare in place with O(1) extra space. Also, `isalnum()` recognizes Unicode letters and digits, while LeetCode 125 guarantees printable ASCII; the result is the same on the given constraints, but state the ASCII assumption if asked.

## Optimal Solution — Two Pointers, Skip Non-Alphanumeric In Place

Keep one pointer at each end. Advance `left` past non-alphanumeric characters, retreat `right` past them, then compare the two characters case-insensitively. Move both inward and repeat. Return `false` on the first mismatch.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

```python
while left < right:
    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1

    if s[left].lower() != s[right].lower():
        return False

    left += 1
    right -= 1
```

This is optimal: every character is inspected at most once, and no filtered copy is built. O(n) time is a lower bound because the whole string may need to be checked, and O(1) extra space is the best possible. The `left < right` guard inside each skip loop prevents the pointers from crossing or running off the ends.

## Alternative Approaches

- **Two pointers (optimal):** O(n) time, O(1) space. Standard interview answer.
- **Filter + reverse (my solution):** O(n) time, O(n) space. Shortest code; fine when memory is not a concern.
- **Regex + reverse:** `re.sub(r"[^a-z0-9]", "", s.lower())` then compare with its reverse. O(n) time, O(n) space; readable but allocates and pulls in a regex.
- **Recursion from both ends:** O(n) time, O(n) call-stack space. Avoid — same comparisons with extra overhead.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Two pointers | **O(n)** | **O(1)** | **Default interview answer** |
| Filter + reverse | O(n) | O(n) | Quick code, memory not a concern |
| Regex + reverse | O(n) | O(n) | Readable one-liner, allocation acceptable |
| Recursion | O(n) | O(n) | Never — call-stack cost for no benefit |

**Interview answer:** Use two pointers from both ends. Skip characters that are not alphanumeric, compare the remaining characters in lowercase, and return `false` on the first mismatch. O(n) time and O(1) extra space, with no filtered copy.

## Edge Cases

- **Empty string** → `true`; an empty sequence is a palindrome.
- **Only non-alphanumeric characters** (`".,!"`, `" "`) → `true`; everything is skipped.
- **Single character** → `true`.
- **Mixed case** (`"aA"`, `"A man, a plan, a canal: Panama"`) → `true`; comparison is case-insensitive.
- **Digits** (`"0P"`) → `false`; `"0"` and `"p"` do not match.
- **Punctuation inside** (`"ab_a"`) → `true`; `_` is skipped, leaving `"aba"`.
- **Numeric palindrome** (`"12.21"`) → `true`.
- **Non-palindrome** (`"race a car"`) → `false`.
- **Unicode input** → `isalnum()` treats Unicode letters/digits as alphanumeric; LeetCode 125 only uses ASCII, so this does not arise there.
