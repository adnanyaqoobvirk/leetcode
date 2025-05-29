class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = digits[::]
        for i in reversed(range(len(digits))):
            if digits[i] != 9:
                ans[i] += 1
                return ans
            else:
                ans[i] = 0
        return [1] + ans