class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        verticalCuts.sort()
        verticalCuts.append(w)
        max_vertical_cut = verticalCuts[0]
        for i in range(1, len(verticalCuts)):
            max_vertical_cut = max(
                max_vertical_cut, 
                verticalCuts[i] - verticalCuts[i - 1]
            )
        
        horizontalCuts.sort()
        horizontalCuts.append(h)
        max_horizontal_cut = horizontalCuts[0]
        for i in range(1, len(horizontalCuts)):
            max_horizontal_cut = max(
                max_horizontal_cut, 
                horizontalCuts[i] - horizontalCuts[i - 1]
            )
            
        return (max_horizontal_cut * max_vertical_cut) % (10**9 + 7)