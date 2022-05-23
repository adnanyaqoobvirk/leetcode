class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def helper(pos: int, one_count: int, zero_count: int) -> int:
            if one_count > n or zero_count > m:
                return -1
            
            if pos >= l:
                return 0
            
            return max(
                helper(pos + 1, one_count, zero_count),
                helper(pos + 1, one_count + ones[pos], zero_count + zeros[pos]) + 1
            )
        
        l = len(strs)
        ones, zeros = [0] * l, [0] * l
        for i, s in enumerate(strs):
            for c in s:
                if c == '1':
                    ones[i] += 1
                else:
                    zeros[i] += 1
        return helper(0, 0, 0)