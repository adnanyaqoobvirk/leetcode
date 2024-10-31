class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def count(l: int, r: int) -> int:
            if l == r:
                return [psums[l]]

            m = l + (r - l) // 2
            left = count(l, m)
            right = count(m + 1, r)

            i = j = k = p = 0
            ln, rn = len(left), len(right)
            res = []
            for i in range(ln):
                while j < rn and right[j] - left[i] < lower: j += 1
                while k < rn and right[k] - left[i] <= upper: k += 1
                ans[0] += k - j

                while p < rn and right[p] <= left[i]:
                    res.append(right[p])
                    p += 1
                res.append(left[i])
            for p in range(p, rn):
                res.append(right[p])
            return res

        psums = [0]
        for num in nums:
            psums.append(psums[-1] + num)

        ans = [0]
        count(0, len(psums) - 1)
        return ans[0]