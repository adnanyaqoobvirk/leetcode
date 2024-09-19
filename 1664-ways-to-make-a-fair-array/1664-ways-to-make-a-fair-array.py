class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd_total = 0
        even_total = 0
        for i in range(len(nums)):
            if i & 1:
                odd_total += nums[i]
            else:
                even_total += nums[i]
        
        curr_odd_sum = 0
        curr_even_sum = 0
        fairs = 0
        for i in range(len(nums)):
            if i & 1:
                odd_total -= nums[i]
                if curr_even_sum + odd_total == even_total + curr_odd_sum:
                    fairs += 1
                curr_odd_sum += nums[i]
            else:
                even_total -= nums[i]
                if curr_odd_sum + even_total == odd_total + curr_even_sum:
                    fairs += 1
                curr_even_sum += nums[i]
        return fairs