# Heap / Priority Queue

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Last Stone Weight](last-stone-weight/) | Max-heap via negated values | O(n log n) | O(n) | Python's `heapq` is a min-heap, so push negated values and negate on the way out; `heapify` on a pre-negated list builds in O(n) (n `heappush` calls cost O(n log n)); a tie destroys both stones, otherwise `x - y` re-enters the pool |
| [K Closest Points to Origin](k-closest-points-to-origin/) | Max-heap of size k on squared distance | O(n log k) | O(k) | The sqrt is monotonic, so squared distance orders identically and stays an exact int; keep a size-k max-heap (negated values) whose root is the farthest kept point — `heappushpop` evicts it when a closer point arrives, so the heap never grows past k |
