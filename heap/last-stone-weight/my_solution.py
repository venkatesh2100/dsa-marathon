import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # heap = heapq.heapify(stones)
        heap = []
        for num in stones:
            heapq.heappush(heap , -num)

        while len(heap) > 1:
            x , y = -heapq.heappop(heap) , -heapq.heappop(heap)

            if abs(x - y) > 0:
                heapq.heappush(heap, -abs(x-y))

        return -heap[0] if heap else 0
