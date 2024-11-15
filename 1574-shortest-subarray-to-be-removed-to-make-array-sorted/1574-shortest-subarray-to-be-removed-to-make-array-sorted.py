class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        def possible(l: int) -> bool:
            if rs[l]:
                return True

            for i in range(l + 1, n):
                if s[i - l - 1] and rs[i] and arr[i - l - 1] <= arr[i]:
                    return True
            return False

        n = len(arr)
        s = [False] * n
        s[0] = True
        for i in range(1, n):
            if arr[i - 1] <= arr[i]:
                s[i] = True
            else:
                break

        rs = [False] * n
        rs[-1] = True
        for i in reversed(range(n - 1)):
            if arr[i] <= arr[i + 1]:
                rs[i] = True
            else:
                break
        
        lo, hi = -1, len(arr) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if possible(mid):
                hi = mid
            else:
                lo = mid
        return hi