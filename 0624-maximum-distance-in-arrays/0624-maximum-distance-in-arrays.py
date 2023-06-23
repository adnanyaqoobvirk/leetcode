class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        vals = []
        for i, arr in enumerate(arrays):
            vals.append((arr[0], i))
            if len(arr) > 1:
                vals.append((arr[-1], i))
        
        vals.sort(key=lambda x: x[0])
        
        if vals[0][1] == vals[-1][1]:
            return max(abs(vals[1][0] - vals[-1][0]), abs(vals[0][0] - vals[-2][0]))
        else:
            return abs(vals[0][0] - vals[-1][0])
        