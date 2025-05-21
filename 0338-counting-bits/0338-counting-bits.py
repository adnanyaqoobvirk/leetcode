class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        j = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                j = 0
            ans.append(ans[j] + 1)
            j += 1
        return ans