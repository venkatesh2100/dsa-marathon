from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []  # one arrival time per fleet, strictly increasing bottom -> top

        # Closest car to the target first, so every later car is behind the fleets so far.
        for p, s in sorted(zip(position, speed), reverse=True):
            t = (target - p) / s
            if stack and t <= stack[-1]:
                continue  # catches the fleet ahead before/at the target -> same fleet
            stack.append(t)

        return len(stack)
