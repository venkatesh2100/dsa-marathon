import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq is a min-heap; negated values turn it into a max-heap —
        # the smallest entry is the heaviest stone. heapify builds in O(n).
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)  # heaviest
            y = -heapq.heappop(heap)  # second heaviest
            if x != y:                # a tie destroys both stones
                heapq.heappush(heap, -(x - y))

        return -heap[0] if heap else 0
