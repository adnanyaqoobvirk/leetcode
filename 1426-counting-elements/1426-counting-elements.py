class Solution:
    def countElements(self, arr: List[int]) -> int:
        counts = Counter(arr)
        ans = 0
        for num in arr:
            if num + 1 in counts:
                ans += 1
        return ans