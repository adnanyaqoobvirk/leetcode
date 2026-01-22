class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        min_ops = 0
        arr = nums[::]
        not_sorted = True
        while not_sorted:
            not_sorted = False
            min_sum = inf
            pair_idx = -1
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    not_sorted = True

                if arr[i] + arr[i - 1] < min_sum:
                    min_sum = arr[i] + arr[i - 1]
                    pair_idx = i
            if not_sorted:
                arr.pop(pair_idx)
                arr.pop(pair_idx - 1)
                arr.insert(pair_idx - 1, min_sum)
                min_ops += 1
        return min_ops