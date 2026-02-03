class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if nums[1] <= nums[0]:
            return False
            
        # finding p
        p = 1
        while p < n:
            if nums[p] == nums[p - 1]:
                return False

            if nums[p] < nums[p - 1]:
                break
            
            p += 1
        
        if p == n:
            return False
        
        # finding q
        q = p
        while q < n:
            if nums[q] == nums[q - 1]:
                return False

            if nums[q] > nums[q - 1]:
                break
            q += 1

        if q == n:
            return False
        
        while q < n:
            if nums[q] <= nums[q - 1]:
                return False
            q += 1

        return True
