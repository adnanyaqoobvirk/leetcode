class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(lo, hi):
            if lo > hi:
                return []
            
            if lo == hi:
                return [nums[lo]]
            
            mid = (lo + hi) // 2
            left = mergeSort(lo, mid)
            right = mergeSort(mid + 1, hi)
            
            if not left:
                return right
            
            if not right:
                return left
            
            ans = []
            n, m = len(left), len(right)
            p1 = p2 = 0
            while p1 < n and p2 < m:
                if left[p1] <= right[p2]:
                    ans.append(left[p1])
                    p1 += 1
                else:
                    ans.append(right[p2])
                    p2 += 1
            
            p, arr = (p1, left) if p1 < n else (p2, right)
            for i in range(p, len(arr)):
                ans.append(arr[i])
                
            return ans
        
        return mergeSort(0, len(nums) - 1)