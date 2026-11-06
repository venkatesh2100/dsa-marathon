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
| two-pointers | [Two Sum II](two-pointers/two-sum-ii/) | O(n) | O(1) | ✅ |
| two-pointers | [3Sum](two-pointers/three-sum/) | O(n²) | O(1) | ✅ |
| two-pointers | [Container With Most Water](two-pointers/container-with-most-water/) | O(n) | O(1) | ✅ |
| two-pointers | [Trapping Rain Water](two-pointers/trapping-rain-water/) | O(n) | O(1) | ✅ |
| stack | [Valid Parentheses](stack/valid-parentheses/) | O(n) | O(n) | ✅ |
| stack | [Min Stack](stack/min-stack/) | O(1) | O(n) | ✅ |
| stack | [Evaluate Reverse Polish Notation](stack/evaluate-reverse-polish-notation/) | O(n) | O(n) | ✅ |
| stack | [Daily Temperatures](stack/daily-temperatures/) | O(n) | O(n) | ✅ |

## Structure

```
dsa-marathon/
├── arrays/
│   └── contains-duplicate/
│       ├── my_solution.py
│       ├── optimal_solution.py
│       └── notes.md
├── two-pointers/
│   └── valid-palindrome/
│       ├── my_solution.py
│       ├── optimal_solution.py
│       └── notes.md
└── stack/
    ├── valid-parentheses/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    ├── min-stack/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    ├── evaluate-reverse-polish-notation/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    └── daily-temperatures/
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
| Two Sum II | Two pointers on sorted input | O(n) | O(1) |
| 3Sum | Sort + two pointers | O(n²) | O(1) |
| Container With Most Water | Two pointers, move shorter wall | O(n) | O(1) |
| Trapping Rain Water | Two pointers, move smaller wall | O(n) | O(1) |
| Valid Parentheses | Stack with pairs map | O(n) | O(n) |
| Min Stack | Auxiliary min stack | O(1) | O(n) |
| Evaluate Reverse Polish Notation | Stack with operator table | O(n) | O(n) |
| Daily Temperatures | Monotonic stack | O(n) | O(n) |