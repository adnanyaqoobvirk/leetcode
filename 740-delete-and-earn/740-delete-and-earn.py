class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_map, max_num = defaultdict(int), 0
        for num in nums:
            num_map[num] += num
            max_num = max(max_num, num)
            
        prev, curr = 0, num_map[1]
        for num in range(2, max_num + 1):
            prev, curr = curr, max(curr, num_map[num] + prev)
        return curr