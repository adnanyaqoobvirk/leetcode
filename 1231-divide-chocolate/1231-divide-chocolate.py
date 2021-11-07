class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def valid_plan(plan: int) -> bool:
            run_sum = cuts = 0
            for sweet in sweetness:
                run_sum += sweet
                if run_sum >= plan:
                    cuts += 1
                    run_sum = 0
            if run_sum >= plan:
                cuts += 1
            return cuts >= k + 1
    
        left, right = min(sweetness), sum(sweetness) + 1
        while left <= right:
            mid = left + (right - left >> 1)
            
            if valid_plan(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1