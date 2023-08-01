class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(num: int, comb: list) -> None:
            if len(comb) == k:
                ans.append(comb[::])
            else:
                for i in range(num, n + 1):
                    comb.append(i)
                    backtrack(i + 1, comb)
                    comb.pop()
        ans = []
        backtrack(1, [])
        return ans