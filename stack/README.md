# Stack

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Valid Parentheses](valid-parentheses/) | Stack + pairs map | O(n) | O(n) | Pop only on a matching closer |
| [Min Stack](min-stack/) | Auxiliary min stack | O(1) | O(n) | Conditional push (`<=`) keeps the min stack small |
| [Evaluate Reverse Polish Notation](evaluate-reverse-polish-notation/) | Stack with operator table | O(n) | O(n) | One-pass evaluation, operator dict |
| [Daily Temperatures](daily-temperatures/) | Monotonic stack | O(n) | O(n) | Pop on next warmer; unresolved keep 0 |
| [Car Fleet](car-fleet/) | Monotonic stack of arrival times | O(n log n) | O(n) | Sort by position desc; merge when time ≤ fleet ahead |
