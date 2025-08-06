from sortedcontainers import SortedSet

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ss = SortedSet()
        for i, b in enumerate(baskets):
            ss.add(b)
        
        count = 0
        for f in fruits:
            i = ss.bisect_right(f)
            if i == len(ss) and len(ss) > 0 and ss[i - 1] == f:
                ss.pop(i - 1)
            elif i < len(ss) and ss[i] >= f:
                ss.pop(i)
            else:
                count += 1
        return count