class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_cnt = [0] * 33
        for i in range(32):
            for num in nums:
                bit_cnt[i] += int(abs(num) & (1 << i) >= 1)
        for num in nums:
            if num < 0:
                bit_cnt[32] += 1
        res = 0
        for i in range(32):
            res |= (bit_cnt[i] % 3) << i
        return -res if bit_cnt[32] % 3 != 0 else res