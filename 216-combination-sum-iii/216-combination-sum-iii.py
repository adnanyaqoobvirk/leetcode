class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(num: int, total: int) -> None:
            if len(comb) == k:
                if total == n:
                    combs.append(comb[:])
            else:
                for i in range(num, 10):
                    comb.append(i)
                    helper(i + 1, total + i)
                    comb.pop()        
        combs, comb = [], []
        helper(1, 0)
        return combs