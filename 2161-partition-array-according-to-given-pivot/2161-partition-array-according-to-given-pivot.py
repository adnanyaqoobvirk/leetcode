class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans, pcount = [], 0
        for num in nums:
            if num < pivot:
                ans.append(num)
            elif num == pivot:
                pcount += 1
                
        for _ in range(pcount):
            ans.append(pivot)
            
        for num in nums:
            if num > pivot:
                ans.append(num)
        return ans