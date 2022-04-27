class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h, curr_height = [float('inf')], float('inf')
        for i, height in enumerate(heights):
            if height > curr_height:
                height_diff = height - curr_height
                if len(h) <= ladders:
                    heappush(h, height_diff)
                elif bricks >= h[0] and height_diff > h[0]:
                    bricks -= heappop(h)
                    heappush(h, height_diff)
                elif bricks >= height_diff:
                    bricks -= height_diff
                else:
                    break
            curr_height = height
        else:
            i += 1
        return i - 1