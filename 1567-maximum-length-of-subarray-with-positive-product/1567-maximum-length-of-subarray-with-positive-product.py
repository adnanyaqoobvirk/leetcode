class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        
        ans = 0
        neg_cnt = 0
        left = 0
        for right, num in enumerate(nums):
            if num == 0:
                if neg_cnt & 1:
                    left_pos_cnt = 1
                    for i in range(left, right):
                        if nums[i] < 0:
                            break
                        left_pos_cnt += 1
                    
                    right_pos_cnt = 1
                    for i in reversed(range(left, right)):
                        if nums[i] < 0:
                            break
                        right_pos_cnt += 1
                    ans = max(ans, right - left - min(left_pos_cnt, right_pos_cnt))
                else:
                    ans = max(ans, right - left)
                neg_cnt = 0
                left = right + 1
            elif num < 0:
                neg_cnt += 1
        return ans