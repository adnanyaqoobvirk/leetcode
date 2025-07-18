class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        total = 0
        h = []
        for i in range(n):
            total += nums[i]
            h.append(-nums[i])
        heapify(h)

        sums = [total]
        for i in range(n, 2 * n):
            total += nums[i]
            heappush(h, -nums[i])
            total += heappop(h)
            sums.append(total)
        
        total = 0
        h = []
        for i in reversed(range(2 * n, 3 * n)):
            total += nums[i]
            h.append(nums[i])
        heapify(h)

        res = sums[-1] - total
        for i in reversed(range(n, 2 * n)):
            total += nums[i]
            heappush(h, nums[i])
            total -= heappop(h)
            res = min(res, sums[i - n] - total)

        return res