class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        invalids = {'2', '3', '4', '5', '7'}
        six_nine = {'6', '9'}
        lo, hi = 0, len(num) - 1
        while lo <= hi:
            if num[lo] in invalids or num[hi] in invalids:
                return False
            
            if num[lo] == num[hi] and (num[lo] == '6' or num[lo] == '9'):
                return False
            
            if num[lo] != num[hi] and (num[lo] not in six_nine or num[hi] not in six_nine):
                return False
            
            lo, hi = lo + 1, hi - 1
        return True