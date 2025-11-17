class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zero_count = k
        for num in nums:
            if num == 1:
                if zero_count < k:
                    return False
                zero_count = 0
            else:
                zero_count += 1
        return True