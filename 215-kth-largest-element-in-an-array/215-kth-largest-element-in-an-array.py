class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left: int, right: int, pivot_idx: int) -> int:
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            
            store_idx = left
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            return store_idx
        
        def select(left: int, right: int, nsmallest: int) -> int:
            if left == right:
                return nums[left]
            
            pivot_idx = partition(left, right, randint(left, right))
            if pivot_idx == nsmallest:
                return nums[pivot_idx]
            elif pivot_idx > nsmallest:
                return select(left, pivot_idx - 1, nsmallest)
            else:
                return select(pivot_idx + 1, right, nsmallest)
        return select(0, len(nums) - 1, len(nums) - k)