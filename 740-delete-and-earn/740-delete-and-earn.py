class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += num
            
        elems = sorted(num_map.keys())
        prev, curr = 0, num_map[elems[0]]
        for i in range(1, len(elems)):
            num = elems[i]
            if num == elems[i - 1] + 1:
                prev, curr = curr, max(curr, num_map[num] + prev)
            else:
                prev, curr = curr, curr + num_map[num]
        return curr