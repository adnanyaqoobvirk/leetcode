class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def partition(lo: int, hi: int, guess: int) -> int:
            nums[hi], nums[guess] = nums[guess], nums[hi]
            
            b = lo
            for f in range(lo, hi):
                if nums[f] < nums[hi]:
                    nums[b], nums[f] = nums[f], nums[b]
                    b += 1
            nums[b], nums[hi] = nums[hi], nums[b]
            return b
        
        def select(left: int, right: int, m: int) -> int:
            if left == right:
                return left
            
            idx = partition(left, right, randint(left, right))
            if idx == m:
                return idx
            elif idx < m:
                return select(idx + 1, right, m)
            else:
                return select(left, idx - 1, m)
        
        n = len(nums)
        median = nums[select(0, n - 1, n // 2)]
        
        ans = 0
        for num in nums:
            ans += abs(median - num)
        return ans