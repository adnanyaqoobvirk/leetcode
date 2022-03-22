class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        zero_rows = set()
        for row in range(len(mat1)):
            for column in range(len(mat1[0])):
                if mat1[row][column] != 0:
                    break
            else:
                zero_rows.add(row)
            
        zero_columns = set()
        for column in range(len(mat2[0])):
            for row in range(len(mat2)):
                if mat2[row][column] != 0:
                    break
            else:
                zero_columns.add(column)
        
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        for row in range(len(mat1)):
            if row in zero_rows:
                continue
            
            for column in range(len(mat2[0])):
                if column in zero_columns:
                    continue
                
                for j in range(len(mat2)):
                    ans[row][column] += mat1[row][j] * mat2[j][column]
        return ans
            