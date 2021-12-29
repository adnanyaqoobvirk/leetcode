class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = prev_cnt = curr_cnt = 0
        for num in nums:
            if num:
                curr_cnt += 1
                prev_cnt += 1
            else:
                ans = max(ans, prev_cnt)
                prev_cnt, curr_cnt = curr_cnt + 1, 0
        ans = max(ans, prev_cnt)
        return ans