class Solution:
    def separateSquares(self, squares):
        # Total area
        total_area = 0.0
        min_y = float('inf')
        max_y = float('-inf')

        for _, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        target = total_area / 2.0

        # Binary search on Y
        lo, hi = min_y, max_y

        def area_below(mid):
            area = 0.0
            for _, y, l in squares:
                if mid <= y:
                    continue
                elif mid >= y + l:
                    area += l * l
                else:
                    area += (mid - y) * l
            return area

        for _ in range(60):  # enough for 1e-5 precision
            mid = (lo + hi) / 2
            if area_below(mid) < target:
                lo = mid
            else:
                hi = mid

        return lo
