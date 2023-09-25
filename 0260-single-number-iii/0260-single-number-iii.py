class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        for num, count in Counter(nums).items():
            if count == 1:
                res.append(num)
        return res