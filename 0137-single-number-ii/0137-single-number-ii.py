class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bcount, neg = [0] * 32, 0
        for num in nums:
            if num < 0:
                neg += 1
                num = -num
                
            i = 0
            while num > 0:
                if num & 1:
                    bcount[i] += 1
                num >>= 1
                i += 1
                
        ans = 0
        for i in range(32):
            if bcount[i] % 3 != 0:
                ans |= 1 << i
                
        return -ans if neg % 3 != 0 else ans