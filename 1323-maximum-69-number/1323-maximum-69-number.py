class Solution:
    def maximum69Number (self, num: int) -> int:
        snum = str(num)
        i = snum.find("6")
        if i < 0:
            return num
        return int(snum[:i] + "9" + snum[i+1:])