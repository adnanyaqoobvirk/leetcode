class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        def countingSort(arr: List[int]) -> List[int]:
            counts = {}
            for num in arr:
                counts[num] = counts.get(num, 0) + 1
            
            pos = 0
            for num in range(1, 100000):
                count = counts.get(num, 0)
                for _ in range(count):
                    arr[pos] = num
                    pos += 1
            return arr
                    
        n = len(nums)
        countingSort(nums)
        
        max_pair_sum = 0
        for i in range(n // 2):
            pair_sum = nums[i] + nums[n - i - 1]
            if pair_sum > max_pair_sum:
                max_pair_sum = pair_sum
        return max_pair_sum