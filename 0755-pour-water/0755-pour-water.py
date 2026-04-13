class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)
        for _ in range(volume):
            min_idx = -1
            for i in reversed(range(k)):
                if heights[i] > heights[k]:
                    break

                if min_idx != -1 and heights[i] > heights[min_idx]:
                    break

                if min_idx == -1 or heights[i] < heights[min_idx]:
                    min_idx = i
            
            if min_idx != -1 and heights[min_idx] != heights[k]:
                heights[min_idx] += 1
                continue
            
            min_idx = -1
            for i in range(k + 1, n):
                if heights[i] > heights[k]:
                    break

                if min_idx != -1 and heights[i] > heights[min_idx]:
                    break

                if min_idx == -1 or heights[i] < heights[min_idx]:
                    min_idx = i
            
            if min_idx != -1 and heights[min_idx] != heights[k]:
                heights[min_idx] += 1
                continue
            
            heights[k] += 1
        return heights