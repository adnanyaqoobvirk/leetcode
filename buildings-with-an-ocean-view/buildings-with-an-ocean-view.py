class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        output = []
        max_height = None
        for i in range(len(heights) - 1, -1, -1):
            if max_height is None or heights[i] > max_height:
                output.append(i)
                max_height = heights[i]
        return output[::-1]