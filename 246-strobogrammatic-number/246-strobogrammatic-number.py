class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        valids = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        lo, hi = 0, len(num) - 1
        while lo <= hi:
            if num[lo] not in valids or valids[num[lo]] != num[hi]:
                return False
            lo, hi = lo + 1, hi - 1
        return True