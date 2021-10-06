class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        nums = [[] for _ in range(math.ceil(math.log2(10000)))]
        for i in range(len(arr)):
            num = arr[i]
            ones = 0
            while num > 0:
                num &= num - 1
                ones += 1
            nums[ones].append(arr[i])
        return [num for arr in nums for num in sorted(arr)]