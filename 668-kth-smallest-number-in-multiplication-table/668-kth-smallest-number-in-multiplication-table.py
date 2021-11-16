class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def valid(c: int) -> bool:
            count = 0
            for i in range(1, m + 1):
                count += min(c // i, n)
            return count >= k
        
        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            
            if valid(mid):
                right = mid
            else:
                left = mid + 1
        return left