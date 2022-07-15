class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        color_indices = [[inf] * 3 for _ in range(len(colors))]
        
        indices = [inf] * 3
        for i, c in enumerate(colors):
            indices[c - 1] = i
            for j in range(3):
                color_indices[i][j] = min(color_indices[i][j], abs(i - indices[j]))
        
        indices = [inf] * 3
        for i in reversed(range(len(colors))):
            c = colors[i]
            indices[c - 1] = i
            for j in range(3):
                color_indices[i][j] = min(color_indices[i][j], abs(i - indices[j]))
            
        ans = []
        for i, c in queries:
            if color_indices[i][c - 1] == inf:
                ans.append(-1)
            else:
                ans.append(color_indices[i][c - 1])
        return ans