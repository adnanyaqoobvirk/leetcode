class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def getCounts(num: int) -> List[int]:
            res = [0] * 10
            while num > 0:
                num, r = divmod(num, 10)
                res[r] += 1
            return res

        while True:
            n += 1
            counts = getCounts(n)
            for i, count in enumerate(counts):
                if count > 0 and i != count:
                    break
            else:
                return n