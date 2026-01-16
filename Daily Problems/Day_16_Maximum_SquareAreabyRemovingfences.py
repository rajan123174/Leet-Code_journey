class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        MOD = 10**9 + 7

        # Add boundary fences
        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])

        # Compute all possible horizontal gaps
        h_gaps = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_gaps.add(h[j] - h[i])

        # Compute all possible vertical gaps
        v_gaps = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                v_gaps.add(v[j] - v[i])

        # Find largest common side
        common = h_gaps & v_gaps
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD
