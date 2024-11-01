class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        def helper(l: int, r: int) -> List[int]:
            if l == r:
                return [psums[l]]
            
            m = l + (r - l) // 2
            left = helper(l, m)
            right = helper(m + 1, r)

            res = []
            nl, nr = len(left), len(right)
            i = j = k = 0
            for j in range(nr):
                while i < nl and right[j] > left[i]: i += 1

                ans[0] += i
                while k < nl and left[k] <= right[j]:
                    res.append(left[k])
                    k += 1
                res.append(right[j])
                
            for k in range(k, nl):
                res.append(left[k])
            return res
            
        psums = [0]
        for num in nums:
            psums.append(psums[-1] + (-1 if num == 0 else 1))
        
        ans = [0]
        helper(0, len(psums) - 1)
        return ans[0]