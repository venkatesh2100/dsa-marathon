# Sliding Window

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock/) | One-pass running min | O(n) | O(1) | Window reading: `profit = p - min_so_far`; abs/red drops since min-update guarantees non-negative |