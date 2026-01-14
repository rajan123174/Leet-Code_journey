import sys

class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.length = [0.0] * (4 * self.n)

    def update(self, v, tl, tr, l, r, add):
        if l > r:
            return
        if l == tl and r == tr:
            self.count[v] += add
        else:
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), add)
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add)
        
        if self.count[v] > 0:
            self.length[v] = self.xs[tr + 1] - self.xs[tl]
        else:
            if tl != tr:
                self.length[v] = self.length[2 * v] + self.length[2 * v + 1]
            else:
                self.length[v] = 0.0

class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        # 1. Collect unique X and Y coordinates
        xs_set = set()
        ys_set = set()
        for x, y, l in squares:
            xs_set.add(x)
            xs_set.add(x + l)
            ys_set.add(y)
            ys_set.add(y + l)
        
        sorted_xs = sorted(list(xs_set))
        sorted_ys = sorted(list(ys_set))
        
        x_map = {val: i for i, val in enumerate(sorted_xs)}
        
        # 2. Prepare events for the Y-sweep
        # (y_coordinate, type, x_start, x_end)
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        events.sort()
        
        # 3. Sweep to calculate area contribution of each Y-interval (slab)
        st = SegmentTree(sorted_xs)
        slab_areas = [] # Stores (y_start, y_end, width_of_union)
        
        event_idx = 0
        total_area = 0.0
        
        for i in range(len(sorted_ys) - 1):
            y_start = sorted_ys[i]
            y_end = sorted_ys[i+1]
            
            # Update segment tree with all events occurring at y_start
            while event_idx < len(events) and events[event_idx][0] <= y_start:
                curr_y, typ, x1, x2 = events[event_idx]
                st.update(1, 0, st.n - 1, x_map[x1], x_map[x2] - 1, typ)
                event_idx += 1
            
            width = st.length[1]
            area = width * (y_end - y_start)
            slab_areas.append((y_start, y_end, width, area))
            total_area += area
            
        # 4. Find the y-coordinate that splits total_area in half
        target_area = total_area / 2
        current_accumulated_area = 0.0
        
        for y_start, y_end, width, area in slab_areas:
            if current_accumulated_area + area >= target_area - 1e-12:
                # If width is 0, the area doesn't increase, we skip to next slab
                # The minimum y will be y_start in a zero-width gap
                if width == 0:
                    current_accumulated_area += area
                    continue
                
                # Interpolate: (target - current) / width gives height inside this slab
                needed = target_area - current_accumulated_area
                return y_start + (needed / width)
            
            current_accumulated_area += area
            
        return float(sorted_ys[-1])