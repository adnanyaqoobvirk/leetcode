class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        max_bits = int(math.log2(n)) + 1
        masks = [(1 << i) for i in range(max_bits)]
        
        original_bit_count = [0] * max_bits
        bit_count = [0] * max_bits
        for i in range(1, n + 2):
            for j in range(max_bits):
                if i <= n and i & masks[j]:
                    original_bit_count[j] += 1
                if nums[i - 1] & masks[j]:
                    bit_count[j] += 1
        ans = 0
        for i in range(max_bits):
            if bit_count[i] - original_bit_count[i] > 0:
                ans |= (1 << i)
        return ans