class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        m, n, o = len(arr1), len(arr2), len(arr3)
        i = j = k = 0
        ans = []
        while i < m and j < n and k < o:
            if arr1[i] == arr2[j] == arr3[k]:
                ans.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        return ans