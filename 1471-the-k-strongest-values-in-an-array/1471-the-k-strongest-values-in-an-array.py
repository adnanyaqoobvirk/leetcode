class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        
        ans = []
        l, r = 0, len(arr) - 1
        while len(ans) < k:
            if abs(arr[l] - m) > abs(arr[r] - m):
                ans.append(arr[l])
                l += 1
            else:
                ans.append(arr[r])
                r -= 1
        return ans