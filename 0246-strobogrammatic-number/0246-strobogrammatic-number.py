class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        valids = set('018')
        
        lo, hi = 0, len(num) - 1
        while lo <= hi:
            if lo == hi:
                if num[lo] not in valids:
                    return False
            elif num[lo] == num[hi]:
                if num[lo] not in valids:
                    return False
            elif num[lo] != num[hi]:
                if not (
                    (num[lo] == '6' and num[hi] == '9')
                    or 
                    (num[lo] == '9' and num[hi] == '6')
                ):
                    return False
            lo += 1
            hi -= 1
        return True