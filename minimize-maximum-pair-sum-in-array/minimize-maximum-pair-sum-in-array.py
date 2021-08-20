class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Sorting the array using counting sort         
        counts = Counter(nums)
        pos = 0
        for num in range(1, 100000):
            for _ in range(counts.get(num, 0)):
                nums[pos] = num
                pos += 1
        
        # Calculating the max pair sum         
        max_pair_sum = 0
        for i in range(n // 2):
            pair_sum = nums[i] + nums[n - i - 1]
            if pair_sum > max_pair_sum:
                max_pair_sum = pair_sum
                
        return max_pair_sum