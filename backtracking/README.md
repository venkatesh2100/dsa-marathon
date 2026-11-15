# Backtracking

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Subsets](subsets/) | Include/exclude backtracking | O(n · 2ⁿ) | O(n) | At each index branch include/exclude; copy `sub[:]` at leaves — appending `sub` by reference would record a buffer that keeps mutating and end up all-empty |
| [Combination Sum](combination-sum/) | Sorted forward backtracking, break-pruned | O(n^(T/M)) | O(T/M) | Recurse on the same `i` for reuse, forward-only order makes every combination a unique multiset; sorting turns the overflow check into an early `break` (M = smallest candidate) |
| [Combination Sum II](combination-sum-ii/) | For-loop backtracking, sibling dedup + break | O(n · 2ⁿ) | O(n) | Each candidate used once (`dfs(i + 1, …)`); skip `nums[i] == nums[i-1]` when `i > start` — dedup lives in generation, not post-filtering; dedup applies to siblings only, sequential duplicate uses are still legal |
| [Permutations](permutations/) | Backtracking with a `used` array | O(n · n!) | O(n) | Try every unused element in the next slot, recurse, undo; copy `sub[:]` at leaves; swap-in-place variant drops the `used` array but mutates/restores the input |
| [Generate Parentheses](generate-parentheses/) | Backtracking on open/close counters | O(4ⁿ / √n) | O(n) | Add `(` while `o < n`, `)` while `c < o` — the `c < o` rule *is* the balance condition, so only valid prefixes are ever built; output count = Catalan number Cₙ |
| [Subsets II](subsets-ii/) | For-loop backtracking, sibling dedup | O(n · 2ⁿ) | O(n) | Sort first, record at every tree node, skip equal siblings (`i > start` guard); dedup bakes into generation — with multiplicities the real count is ∏(countᵢ + 1) |
| [Word Search](word-search/) | DFS from each cell, mark + backtrack | O(m · n · 4ᴸ) | O(L) | Mark the current cell (`"#"`) or track a visited set, probe 4 neighbors, unmark on backtrack; really ≤ 3ᴸ after the first step since you can't re-enter the previous cell (L = len(word)) |
