# Heap / Priority Queue

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Last Stone Weight](last-stone-weight/) | Max-heap via negated values | O(n log n) | O(n) | Python's `heapq` is a min-heap, so push negated values and negate on the way out; `heapify` on a pre-negated list builds in O(n) (n `heappush` calls cost O(n log n)); a tie destroys both stones, otherwise `x - y` re-enters the pool |
