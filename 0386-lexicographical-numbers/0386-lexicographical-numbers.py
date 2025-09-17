class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1]
        curr = 1
        while len(ans) < n:
            if ans[-1] * 10 <= n:
                ans.append(ans[-1] * 10)
                curr = ans[-1]
            else:
                curr, r = divmod(curr, 10)
                if r < 9 and curr * 10 + r + 1 <= n:
                    ans.append(curr * 10 + r + 1)
                    curr = ans[-1]
        return ans