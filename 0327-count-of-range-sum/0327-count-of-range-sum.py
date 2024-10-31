class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def update(i: int) -> None:
            while i < n:
                bit[i] += 1
                i += i & -i

        def query(i: int) -> int:
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        psums = [0]
        for num in nums:
            psums.append(psums[-1] + num)
        
        n = len(psums) + 1
        bit = [0] * n
        ssums = sorted(psums)
        count = 0
        for s in psums:
            count += query(bisect_right(ssums, s - lower)) - query(bisect_left(ssums, s - upper))
            update(bisect_left(ssums, s) + 1)
        return count