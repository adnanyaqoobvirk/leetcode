class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(pos: int) -> None:
            if pos <= n:
                if len(comb) == k:
                    ans.append(comb[:])
                else:
                    for i in range(pos, n):
                        comb.append(i + 1)
                        backtrack(i + 1)
                        comb.pop()
        
        comb, ans = [], []
        backtrack(0)
        return ans