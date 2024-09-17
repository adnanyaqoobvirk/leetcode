class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def rowMaxRectangle(heights: List[int]) -> int:
            area = 0
            stack = [-1]
            for i in range(len(heights)):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    area = max(area, width * height)
                stack.append(i)
            while stack[-1] != -1:
                height = heights[stack.pop()]
                width = len(heights) - stack[-1] - 1
                area = max(area, width * height)
            return area

        max_area = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
            max_area = max(max_area, rowMaxRectangle(dp))
        return max_area