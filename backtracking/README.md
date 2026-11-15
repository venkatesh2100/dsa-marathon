# Backtracking

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Subsets](subsets/) | Include/exclude backtracking | O(n · 2ⁿ) | O(n) | At each index branch include/exclude; copy `sub[:]` at leaves — appending `sub` by reference would record a buffer that keeps mutating and end up all-empty |
