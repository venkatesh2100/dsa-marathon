# Arrays

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Contains Duplicate](contains-duplicate/) | Hash set | O(n) | O(n) | Early exit on first repeat |
| [Is Anagram](is-anagram/) | Frequency array | O(n) | O(1) | Lowercase `a`–`z` only |
| [Two Sum](two-sum/) | One-pass hash map | O(n) | O(n) | Check complement before inserting |
| [Group Anagrams](group-anagrams/) | Frequency tuple key | O(n · k) | O(n · k) | `k` = max string length |
| [Top K Frequent Elements](top-k-frequent-elements/) | Bucket sort | O(n) | O(n) | Frequencies bounded by `n` |
| [Encode and Decode Strings](encode-and-decode-strings/) | Length-prefixed chunks | O(N) | O(N) | `N` = total characters |
| [Product of Array Except Self](product-of-array-except-self/) | Running prefix + suffix | O(n) | O(1) | No division; output not counted |
