class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = []
        while num > 0:
            num, d = divmod(num, 10)
            digits.append(d)

        ans = 0
        first = True
        for d in reversed(digits):
            if d == 6 and first:
                ans = ans * 10 + 9
                first = False
            else:
                ans = ans * 10 + d
        return ans