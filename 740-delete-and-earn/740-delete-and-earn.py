class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num, num_map = 0, defaultdict(int)
        for num in nums:
            num_map[num] += num
            max_num = max(max_num, num)
        
        prev = curr = 0
        for num in reversed(range(max_num + 1)):
            prev, curr = curr, max(
                num_map[num] + prev,
                curr
            )
        return curr