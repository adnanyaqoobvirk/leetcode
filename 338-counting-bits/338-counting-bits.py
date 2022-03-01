class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        while True:
            for i in range(len(ans)):
                if len(ans) == n + 1:
                    return ans
                ans.append(ans[i] + 1)