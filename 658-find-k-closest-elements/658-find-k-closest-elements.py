class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        
        if x >= arr[-1]:
            return arr[n - k:n]
        
        if x <= arr[0]:
            return arr[:k]
        
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] >= x:
                hi = mid
            else:
                lo = lo + 1
        
        ans = deque()
        left, right = lo - 1, lo
        while len(ans) < k:
            if right == n:
                ans.appendleft(arr[left])
                left -= 1
            elif left < 0:
                ans.append(arr[right])
                right += 1
            else:
                if arr[right] - x >= x - arr[left]:
                    ans.appendleft(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
        return ans