class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        nums = []
        for i in range(len(arr)):
            num = arr[i]
            ones = 0
            while num > 0:
                num &= num - 1
                ones += 1
            nums.append((ones, arr[i]))
        
        nums.sort()
        return [num for _, num in nums]