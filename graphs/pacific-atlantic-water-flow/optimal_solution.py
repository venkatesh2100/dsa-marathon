from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

        def flow_from(seeds):
            # Reverse flow: start at an ocean's border cells and walk uphill —
            # every cell reached is one the ocean can receive water from.
            que = deque(seeds)
            vis = set(seeds)
            while que:
                r, c = que.popleft()
                for dr, dc in dirs:
                    dx, dy = r + dr, c + dc
                    if (
                        0 <= dx < row
                        and 0 <= dy < col
                        and (dx, dy) not in vis
                        and heights[dx][dy] >= heights[r][c]
                    ):
                        que.append((dx, dy))
                        vis.add((dx, dy))
            return vis

        pacific = flow_from([(r, 0) for r in range(row)] + [(0, c) for c in range(col)])
        atlantic = flow_from(
            [(r, col - 1) for r in range(row)] + [(row - 1, c) for c in range(col)]
        )

        return [list(rc) for rc in pacific & atlantic]
