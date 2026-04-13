class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)
        for _ in range(volume):
            min_idx = k
            for i in reversed(range(k)):
                if heights[i] > heights[min_idx]:
                    break

                if heights[i] < heights[min_idx]:
                    min_idx = i
            
            if min_idx != k:
                heights[min_idx] += 1
                continue

            for i in range(k + 1, n):
                if heights[i] > heights[min_idx]:
                    break

                if heights[i] < heights[min_idx]:
                    min_idx = i
            
            heights[min_idx] += 1
        return heights