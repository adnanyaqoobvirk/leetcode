class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        nqueries = []
        for i, (x, y) in enumerate(queries):
            nqueries.append([y, x, i] if x > y else [x, y, i])
        nqueries.sort(reverse=True, key=lambda x: (x[1], x[0]))

        ans = [-1] * len(nqueries)
        stack = deque()
        k = len(heights) - 1
        for x, y, i in nqueries:
            if x == y or heights[x] <= heights[y]:
                ans[i] = y
                continue
            
            while k > y:
                while stack and heights[stack[0]] < heights[k]:
                    stack.popleft()
                stack.appendleft(k)
                k -= 1
            
            j = bisect_right(stack, heights[x], key=lambda a: heights[a])
            if stack and j != len(stack):
                ans[i] = stack[j]
        return ans

