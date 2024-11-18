class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k > 0:
            for i in range(1, k + 1):
                ans[0] += code[i]

            for i in range(1, n):
                ans[i] = ans[i - 1] - code[i] + code[(i + k) % n]
        elif k < 0:
            start = n + k
            for i in range(start , n):
                ans[0] += code[i]

            for i in range(1, n):
                ans[i] = ans[i - 1] + code[i - 1] - code[(start + i - 1) % n]
        return ans