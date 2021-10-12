# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            ss = (right - left) // 3
            mid1 = left + ss
            mid2 = mid1 + ss
            
            result1 = guess(mid1)
            result2 = guess(mid2)
            
            if result1 == 0:
                return mid1
            elif result1 == -1:
                right = mid1 - 1
            else:
                left = mid1 + 1
                
            if result2 == 0:
                return mid2
            elif result2 == -1:
                right = mid2 - 1
            else:
                left = mid2 + 1