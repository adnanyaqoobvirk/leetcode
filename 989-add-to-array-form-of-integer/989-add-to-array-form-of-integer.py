class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = k
        for i in reversed(range(len(num))):
            carry, num[i] = divmod(num[i] + carry, 10)
        digits = []
        while carry > 0:
            carry, d = divmod(carry, 10)
            digits.append(d)
        return digits[::-1] + num