class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper() -> None:
            if len(comb) == n:
                combs.append(comb[:])
            else:
                for num in counts.keys():
                    if counts[num] > 0:
                        counts[num] -= 1
                        comb.append(num)
                        helper()
                        comb.pop()
                        counts[num] += 1
        n, combs, comb, counts = len(nums), [], [], Counter(nums)
        helper()
        return combs