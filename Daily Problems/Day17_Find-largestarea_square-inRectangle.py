class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        max_area = 0

        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]

            for j in range(i + 1, n):
                x1b, y1b = bottomLeft[j]
                x2b, y2b = topRight[j]

                # Intersection dimensions
                width = min(x2, x2b) - max(x1, x1b)
                height = min(y2, y2b) - max(y1, y1b)

                if width > 0 and height > 0:
                    side = min(width, height)
                    max_area = max(max_area, side * side)

        return max_area
