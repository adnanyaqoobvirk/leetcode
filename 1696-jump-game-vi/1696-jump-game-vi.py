class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        score = [0] * n
        score[-1] = nums[-1]
        
        max_heap = [(-nums[-1], n - 1)]
        for i in reversed(range(n - 1)):
            while max_heap and max_heap[0][1] > i + k:
                heappop(max_heap)
            score[i] = nums[i] + score[max_heap[0][1]]
            heappush(max_heap, (-score[i], i))
        return score[0]