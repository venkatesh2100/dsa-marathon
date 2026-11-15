# Backtracking

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Subsets](subsets/) | Include/exclude backtracking | O(n · 2ⁿ) | O(n) | At each index branch include/exclude; copy `sub[:]` at leaves — appending `sub` by reference would record a buffer that keeps mutating and end up all-empty |
| [Combination Sum](combination-sum/) | Sorted forward backtracking, break-pruned | O(n^(T/M)) | O(T/M) | Recurse on the same `i` for reuse, forward-only order makes every combination a unique multiset; sorting turns the overflow check into an early `break` (M = smallest candidate) |
| [Combination Sum II](combination-sum-ii/) | For-loop backtracking, sibling dedup + break | O(n · 2ⁿ) | O(n) | Each candidate used once (`dfs(i + 1, …)`); skip `nums[i] == nums[i-1]` when `i > start` — dedup lives in generation, not post-filtering; dedup applies to siblings only, sequential duplicate uses are still legal |
