import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        def distance(r , c):

            return ((r*r) + (c*c))**0.5
        for r , c in points:

            dis = distance(r ,c)

            heapq.heappush(heap , (dis , (r,c)))
        res  = []
        while k:
            dis , points = heapq.heappop(heap)
            res.append(points)
            k-=1

        return res
