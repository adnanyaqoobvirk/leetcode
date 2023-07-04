class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bcount = [0] * 32
        for num in nums:
            num, i = abs(num), 0
            while num > 0:
                if num & 1:
                    bcount[i] += 1
                num >>= 1
                i += 1
        ans = 0
        for i in range(32):
            if bcount[i] % 3 != 0:
                ans |= 1 << i
        
        neg = 0
        for num in nums:
            if abs(num) == ans and num < 0:
                neg += 1
        return -ans if neg == 1 else ans