class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = [None] * len(nums)
        for i in range(len(nums)):
            tmp = output[index[i]]
            output[index[i]] = nums[i]
            for j in range(index[i] + 1, len(output)):
                if output[j] is None:
                    output[j] = tmp
                    break
                tmp, output[j] = output[j], tmp
        return output