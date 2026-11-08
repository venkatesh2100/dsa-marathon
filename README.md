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
| stack | [Car Fleet](stack/car-fleet/) | O(n log n) | O(n) | ✅ |
| stack | [Largest Rectangle in Histogram](stack/largest-rectangle-in-histogram/) | O(n) | O(n) | ✅ |
| binary-search | [Binary Search](binary-search/binary-search/) | O(log n) | O(1) | ✅ |
| binary-search | [Search a 2D Matrix](binary-search/search-a-2d-matrix/) | O(log(m·n)) | O(1) | ✅ |
| binary-search | [Koko Eating Bananas](binary-search/koko-eating-bananas/) | O(n · log m) | O(1) | ✅ |
| binary-search | [Find Minimum in Rotated Sorted Array](binary-search/find-minimum-in-rotated-sorted-array/) | O(log n) | O(1) | ✅ |
| binary-search | [Search in Rotated Sorted Array](binary-search/search-in-rotated-sorted-array/) | O(log n) | O(1) | ✅ |
| binary-search | [Median of Two Sorted Arrays](binary-search/median-of-two-sorted-arrays/) | O(log min(m, n)) | O(1) | ✅ |
| sliding-window | [Best Time to Buy and Sell Stock](sliding-window/best-time-to-buy-and-sell-stock/) | O(n) | O(1) | ✅ |
| sliding-window | [Longest Substring Without Repeating Characters](sliding-window/longest-substring-without-repeating-characters/) | O(n) | O(min(n, Σ)) | ✅ |
| sliding-window | [Longest Repeating Character Replacement](sliding-window/longest-repeating-character-replacement/) | O(n) | O(Σ) | ✅ |
| linked-list | [Reverse Linked List](linked-list/reverse-linked-list/) | O(n) | O(1) | ✅ |
| linked-list | [Merge Two Sorted Lists](linked-list/merge-two-sorted-lists/) | O(n + m) | O(1) | ✅ |
| linked-list | [Linked List Cycle](linked-list/linked-list-cycle/) | O(n) | O(1) | ✅ |

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
    ├── daily-temperatures/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    ├── car-fleet/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    └── largest-rectangle-in-histogram/
        ├── my_solution.py
        ├── optimal_solution.py
        └── notes.md
└── binary-search/
    ├── binary-search/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    ├── search-a-2d-matrix/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    ├── koko-eating-bananas/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    ├── find-minimum-in-rotated-sorted-array/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    ├── search-in-rotated-sorted-array/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    ├── median-of-two-sorted-arrays/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
└── sliding-window/
    ├── best-time-to-buy-and-sell-stock/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    ├── longest-substring-without-repeating-characters/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    └── longest-repeating-character-replacement/
        ├── my_solution.py
        ├── optimal_solution.py
        └── notes.md
└── linked-list/
    ├── reverse-linked-list/
    │   ├── my_solution.py
    │   ├── optimal_solution.py
    │   └── notes.md
    └── merge-two-sorted-lists/
        ├── my_solution.py
        ├── optimal_solution.py
        └── notes.md
    └── linked-list-cycle/
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
| Car Fleet | Monotonic stack of arrival times | O(n log n) | O(n) |
| Largest Rectangle in Histogram | Monotonic stack of indices | O(n) | O(n) |
| Binary Search | Halve window with `mid ± 1` | O(log n) | O(1) |
| Search a 2D Matrix | Flatten to 1D, `divmod` map | O(log(m·n)) | O(1) |
| Koko Eating Bananas | Binary search on the answer | O(n · log m) | O(1) |
| Find Minimum in Rotated Sorted Array | Binary search: compare mid vs right end | O(log n) | O(1) |
| Search in Rotated Sorted Array | One-pass sorted-half range check | O(log n) | O(1) |
| Median of Two Sorted Arrays | Partition-cut binary search on smaller array | O(log min(m, n)) | O(1) |
| Best Time to Buy and Sell Stock | One-pass running min | O(n) | O(1) |
| Longest Substring Without Repeating Characters | Shrink-on-duplicate window | O(n) | O(min(n, Σ)) |
| Longest Repeating Character Replacement | One-slide-per-step window + stale max_freq | O(n) | O(Σ) |
| Reverse Linked List | In-place three-pointer walk | O(n) | O(1) |
| Merge Two Sorted Lists | Dummy-head tail splice | O(n + m) | O(1) |
| Linked List Cycle | Floyd's tortoise & hare | O(n) | O(1) |