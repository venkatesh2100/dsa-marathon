# DSA Marathon 🏃 — Interview Prep

Daily problem-solving log for coding interviews. See [PUSHGUIDE.md](PUSHGUIDE.md) for the workflow and a paste-ready prompt.

Every problem folder contains:

- `my_solution.py` — my first working attempt
- `optimal_solution.py` — the optimal approach
- `notes.md` — complexity, tradeoffs, and which one to pick in an interview

## Progress

| Topic | Problem | Time | Space | Status |
|---|---|---|---|---|
| arrays | [Contains Duplicate](arrays/contains-duplicate/) | O(n) | O(n) | ✅ |
| arrays | [Is Anagram](arrays/is-anagram/) | O(n) | O(1) | ✅ |
| arrays | [Two Sum](arrays/two-sum/) | O(n) | O(n) | ✅ |
| arrays | [Group Anagrams](arrays/group-anagrams/) | O(n · k) | O(n · k) | ✅ |
| arrays | [Top K Frequent Elements](arrays/top-k-frequent-elements/) | O(n) | O(n) | ✅ |
| arrays | [Encode and Decode Strings](arrays/encode-and-decode-strings/) | O(N) | O(N) | ✅ |
| arrays | [Product of Array Except Self](arrays/product-of-array-except-self/) | O(n) | O(1) | ✅ |
| arrays | [Valid Sudoku](arrays/valid-sudoku/) | O(1) | O(1) | ✅ |
| arrays | [Longest Consecutive Sequence](arrays/longest-consecutive-sequence/) | O(n) | O(n) | ✅ |
| two-pointers | [Valid Palindrome](two-pointers/valid-palindrome/) | O(n) | O(1) | ✅ |

## Structure

```
dsa-marathon/
├── arrays/
│   └── contains-duplicate/
│       ├── my_solution.py
│       ├── optimal_solution.py
│       └── notes.md
└── two-pointers/
    └── valid-palindrome/
        ├── my_solution.py
        ├── optimal_solution.py
        └── notes.md
```

## Quick Reference

| Problem | Best Approach | Time | Space |
|---|---|---|---|
| Contains Duplicate | Hash set | O(n) | O(n) |
| Is Anagram | Frequency array | O(n) | O(1) |
| Two Sum | One-pass hash map | O(n) | O(n) |
| Group Anagrams | Frequency tuple key | O(n · k) | O(n · k) |
| Top K Frequent Elements | Bucket sort | O(n) | O(n) |
| Encode and Decode Strings | Length-prefixed chunks | O(N) | O(N) |
| Product of Array Except Self | Running prefix + suffix | O(n) | O(1) |
| Valid Sudoku | Bitmask | O(1) | O(1) |
| Longest Consecutive Sequence | Hash set from run boundaries | O(n) | O(n) |
| Valid Palindrome | Two pointers, skip non-alphanumeric | O(n) | O(1) |
