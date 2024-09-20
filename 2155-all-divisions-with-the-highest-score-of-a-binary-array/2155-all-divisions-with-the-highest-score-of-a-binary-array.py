class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
        
        div_score_map = defaultdict(list)
        div_score_map[ones].append(0)

        curr_ones = 0
        for i in range(1, len(nums) + 1):
            if nums[i - 1] == 1:
                curr_ones += 1
                ones -= 1
            div_score_map[i - curr_ones + ones].append(i)
        
        ans = None
        max_div_score = -inf
        for score, indexes in div_score_map.items():
            if score > max_div_score:
                ans = indexes
                max_div_score = score
        return ans