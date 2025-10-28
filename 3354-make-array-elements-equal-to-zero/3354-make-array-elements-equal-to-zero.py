class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        left_total = 0
        valids = 0
        for num in nums:
            if num == 0:
                right_total = total - left_total
                if right_total == left_total:
                    valids += 2
                elif right_total == left_total + 1 or right_total == left_total - 1:
                    valids += 1
            left_total += num
        return valids