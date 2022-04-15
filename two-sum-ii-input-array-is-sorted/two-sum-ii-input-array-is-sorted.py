class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def getIndex(num: int) -> int:
            lo, hi = 0, n - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if numbers[mid] == num:
                    return  mid
                elif numbers[mid] > num:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1
        
        n = len(numbers)
        for i in range(n):
            idx = getIndex(target - numbers[i])
            if idx > -1 and idx != i:
                if i > idx:
                    return [idx + 1, i + 1]
                else:
                    return [i + 1, idx + 1]
        return []