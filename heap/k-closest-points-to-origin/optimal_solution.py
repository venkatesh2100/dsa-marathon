import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # SQUARED distance orders identically to Euclidean distance (the sqrt
        # is monotonic) and stays an exact int — no float ties.
        # Max-heap of size k via negated values: the root is the FARTHEST
        # point kept, so pushpop evicts it whenever a closer point arrives.
        heap = []
        for x, y in points:
            d = x * x + y * y
            if len(heap) < k:
                heapq.heappush(heap, (-d, x, y))
            else:
                heapq.heappushpop(heap, (-d, x, y))

        return [[x, y] for _, x, y in heap]
