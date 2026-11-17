from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dic = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        row, col = len(heights), len(heights[0])

        # 1. Start from all Pacific border cells (top row & left col)
        que = deque()
        vis = set()
        for r in range(row):
            que.append((r, 0))
            vis.add((r, 0))
        for c in range(col):
            que.append((0, c))
            vis.add((0, c))

        while que:
            r, c = que.popleft()  # Fixed: moved outside the 'for' loop

            for dr, dc in dic:
                dx, dy = r + dr, c + dc

                if dx < 0 or dx >= row or dy < 0 or dy >= col or (dx, dy) in vis:
                    continue

                # Fixed: >= because we go uphill from the ocean
                if heights[dx][dy] >= heights[r][c]:
                    que.append((dx, dy))
                    vis.add((dx, dy))  # Fixed: .add() instead of .append()

        # 2. Do the exact same thing for Atlantic border cells (bottom row & right col)
        que2 = deque()
        vis2 = set()
        for r in range(row):
            que2.append((r, col - 1))
            vis2.add((r, col - 1))
        for c in range(col):
            que2.append((row - 1, c))
            vis2.add((row - 1, c))

        while que2:
            r, c = que2.popleft()

            for dr, dc in dic:
                dx, dy = r + dr, c + dc

                if dx < 0 or dx >= row or dy < 0 or dy >= col or (dx, dy) in vis2:
                    continue

                if heights[dx][dy] >= heights[r][c]:
                    que2.append((dx, dy))
                    vis2.add((dx, dy))

        # 3. Collect cells that appear in BOTH visited sets
        res = []
        for r, c in vis:
            if (r, c) in vis2:
                res.append([r, c])

        return res
