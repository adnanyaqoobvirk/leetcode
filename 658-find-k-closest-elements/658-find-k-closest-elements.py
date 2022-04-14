class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = bisect_left(arr, x) - 1
        right = left + 1
        ans = deque([])
        while len(ans) < k:
            if left == -1:
                ans.append(arr[right])
                right += 1
                continue
            
            if right == n or abs(arr[left] - x) <= abs(arr[right] - x):
                ans.appendleft(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
        return ans