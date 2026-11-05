# Group Anagrams

**Problem:** Given an array of strings `strs`, group the anagrams together. An anagram is a word formed by rearranging the letters of another, using every letter exactly once. Return the groups in any order.

**Links:** [NeetCode 49](https://neetcode.io/problems/anagram-groups) · [LeetCode 49](https://leetcode.com/problems/group-anagrams/)

---

## My Solution — Sorted String as Key

Two words are anagrams exactly when their sorted characters match. Sort each word, convert it to a tuple, and use it as a hash map key. Every word that maps to the same key joins the same group.

| | |
|---|---|
| **Time** | O(n · k log k) |
| **Space** | O(n · k) |

Where `n` is the number of strings and `k` is the maximum string length.

**Caveat:** Sorting every word is the bottleneck. The `res` list is unnecessary — `list(hmap.values())` returns the groups directly.

## Optimal Solution — Frequency Tuple as Key

A counting key avoids sorting: count the 26 letters in each word and use the count tuple as the key. All anagrams produce an identical count vector, so they land in the same bucket.

| | |
|---|---|
| **Time** | O(n · k) |
| **Space** | O(n · k) |

```python
counts = [0] * 26
for ch in word:
    counts[ord(ch) - ord("a")] += 1
groups[tuple(counts)].append(word)
```

**Caveat:** The 26-slot count assumes lowercase English letters. If the alphabet is arbitrary, fall back to the sorted-key approach or use a general `Counter` tuple.

## Alternative Approaches

- **Sorting key (my solution):** O(n · k log k) time. Simple, works for any character set, often fast enough in practice.
- **Counting key (optimal):** O(n · k) time. Best when the alphabet is small and fixed.
- **Prime-product key:** Map letters to primes and multiply. Elegant in theory, but risks integer overflow in most languages — avoid in interviews unless asked.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Frequency tuple key | **O(n · k)** | O(n · k) | **Default** for lowercase `a`–`z` |
| Sorted string key | O(n · k log k) | O(n · k) | Arbitrary characters, shortest code |
| Prime-product key | O(n · k) | O(n · k) | Never — overflow risk, hard to explain |

**Interview answer:** Group words by a canonical key. Count the 26 letters of each word and use the count tuple as the key — O(n · k) time. Mention the sorted-string key as the simpler alternative at O(n · k log k).

## Edge Cases

- Empty string `""` → key `(0, 0, ...)`, forms its own group.
- Multiple empty strings → grouped together.
- Single string → one group.
- All words are anagrams → one group containing every word.
- No anagrams → one group per word.
- Different lengths → different count keys, so automatically separate groups.
- Duplicate words → both copies stay in the same group.
