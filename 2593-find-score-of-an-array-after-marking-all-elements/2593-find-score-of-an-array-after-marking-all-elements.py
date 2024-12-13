class Solution:
    def findScore(self, nums: List[int]) -> int:
        unmarked = set(range(len(nums)))
        h = [(nums[i], i) for i in range(len(nums))]
        heapify(h)
        score = 0
        while unmarked:
            num, i = heappop(h)
            if i in unmarked:
                score += num
                unmarked.remove(i)
                unmarked.discard(i + 1)
                unmarked.discard(i - 1)
        return score