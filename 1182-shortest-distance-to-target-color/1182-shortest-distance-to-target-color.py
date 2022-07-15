class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        color_indices = [[] for _ in range(3)]
        for i, color in enumerate(colors):
            color_indices[color - 1].append(i)
        
        ans = []
        for i, c in queries:
            indices = color_indices[c - 1]
            if not indices:
                ans.append(-1)
                continue
            
            lo, hi = 0, len(indices) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if indices[mid] >= i:
                    hi = mid
                else:
                    lo = mid + 1
            if lo > 0:
                ans.append(
                    min(
                        abs(indices[lo - 1] - i),
                        abs(indices[lo] - i)
                    )
                )
            else:
                ans.append(abs(indices[lo] - i))
        return ans
            