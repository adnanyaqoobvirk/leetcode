class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += int(matrix[i][j])
            
            smallest = [n] * n
            stack = []
            for i in reversed(range(n)):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                
                if stack:
                    smallest[i] = stack[-1]
                
                stack.append(i)
            
            stack = []
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                
                max_area = max(
                    max_area,
                    heights[i] * (smallest[i] - stack[-1] - 1 if stack else smallest[i])
                )
                
                stack.append(i)
        return max_area