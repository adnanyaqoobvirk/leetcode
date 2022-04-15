class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        max_bits = int(math.log2(n)) + 1
        
        original_bit_count = [0] * max_bits
        for num in range(1, n + 1):
            for i in range(max_bits):
                if num & (1 << i):
                    original_bit_count[i] += 1
        
        bit_count = [0] * max_bits
        for num in nums:
            for i in range(max_bits):
                if num & (1 << i):
                    bit_count[i] += 1
        ans = 0
        for i in range(max_bits):
            if bit_count[i] - original_bit_count[i] > 0:
                ans |= (1 << i)
        return ans