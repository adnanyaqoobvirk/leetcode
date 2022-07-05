class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        
        ans = neg_cnt = left = 0
        first_neg = last_neg = -1
        for right, num in enumerate(nums):
            if num == 0:
                if neg_cnt & 1:
                    ans = max(
                        ans, 
                        right - left - min(
                            first_neg - left + 1, right - last_neg
                        )
                    )
                else:
                    ans = max(ans, right - left)
                
                neg_cnt = 0
                left = right + 1
                first_neg = last_neg = -1
            elif num < 0:
                if first_neg < 0:
                    first_neg = last_neg = right
                else:
                    last_neg = right
                neg_cnt += 1
        return ans