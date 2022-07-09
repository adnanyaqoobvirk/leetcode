class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        ans = nums[-1]
        max_heap = [(-nums[-1], n - 1)]
        for i in reversed(range(n - 1)):
            while max_heap and max_heap[0][1] > i + k:
                heappop(max_heap)
            ans = nums[i] - max_heap[0][0]
            heappush(max_heap, (-ans, i))
        return ans