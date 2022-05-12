class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper() -> None:
            if len(comb) == n:
                combs.add(tuple(num for num, _ in comb))
            else:
                for i, num in enumerate(nums):
                    if (num, i) not in comb:
                        comb.append((num, i))
                        helper()
                        comb.pop()
        n, combs, comb = len(nums), set(), []
        helper()
        return combs