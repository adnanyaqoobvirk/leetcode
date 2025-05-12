class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        dcounts = Counter(digits)
        for num in range(100, 1000):
            ndigits = [num // 100, num // 10 % 10, num % 10]
            hasEven = False
            for d, count in Counter(ndigits).items():
                if dcounts[d] < count:
                    break
            else:
                if ndigits[-1] % 2 == 0:
                    ans.append(num)
        return ans