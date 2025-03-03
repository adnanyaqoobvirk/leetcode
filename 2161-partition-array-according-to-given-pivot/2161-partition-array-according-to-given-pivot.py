class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = 0
        ans = deque([num for num in nums if num == pivot])
        for r in reversed(range(len(nums))):
            if nums[l] > pivot:
                ans.append(nums[l])
            l += 1
            if nums[r] < pivot:
                ans.appendleft(nums[r])
        return list(ans)