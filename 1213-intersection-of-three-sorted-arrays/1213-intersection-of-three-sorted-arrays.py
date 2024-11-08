class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        n, m = len(arr2), len(arr2)
        ans = []
        for num in arr1:
            i, j = bisect_left(arr2, num), bisect_left(arr3, num)
            if i < n  and j < m and arr2[i] == num and arr3[j] == num:
                ans.append(num)
        return ans