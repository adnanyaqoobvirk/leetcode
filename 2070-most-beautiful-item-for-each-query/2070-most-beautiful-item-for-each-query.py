class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        for i in range(1, len(items)):
            items[i][1] = max(items[i - 1][1], items[i][1])

        ans = []
        for q in queries:
            i = bisect_right(items, q, key=lambda x: x[0])
            if i == 0:
                ans.append(0)
            else:
                ans.append(items[i - 1][1])
        return ans