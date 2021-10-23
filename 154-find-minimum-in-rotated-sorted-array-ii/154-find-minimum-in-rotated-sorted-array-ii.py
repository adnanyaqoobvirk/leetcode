class Solution:
    def findMin(self, nums: List[int]) -> int:
        def recurse(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                return recurse(left, mid)
            elif nums[mid] == nums[right]:
                return min(recurse(left, mid), recurse(mid + 1, right))
            else:
                return recurse(mid + 1, right)
        return recurse(0, len(nums) - 1)