class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        ans = 0
        for num in nums:
            count = 0
            nnum = num
            while nnum in num_set:
                num_set.remove(nnum)
                count += 1
                nnum -= 1
            
            nnum = num + 1
            while nnum in num_set:
                num_set.remove(nnum)
                count += 1
                nnum += 1
            ans = max(ans, count)
        return ans