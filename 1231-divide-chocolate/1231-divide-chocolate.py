class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        left, right = min(sweetness), sum(sweetness) // (k + 1)
        while left <= right:
            mid = left + (right - left >> 1)
            
            run_sum = cuts = 0
            for sweet in sweetness:
                run_sum += sweet
                if run_sum >= mid:
                    cuts += 1
                    run_sum = 0
            if run_sum >= mid:
                cuts += 1
                
            if cuts >= k + 1:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1