class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        def search(row: List[int], val: int) -> bool:
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] == val:
                    return True
                elif row[mid] > val:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        
        m, n = len(mat), len(mat[0])
        for i in range(n):
            for j in range(1, m):
                if not search(mat[j], mat[0][i]):
                    break
            else:
                return mat[0][i]
        return -1