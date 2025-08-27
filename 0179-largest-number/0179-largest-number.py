class SNum:
    def __init__(self, v: int) -> None:
        self.v = str(v)
    
    def __lt__(self, other: 'Snum') -> bool:
        return self.v + other.v < other.v + self.v

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        snums = [snum.v for snum in sorted((SNum(num) for num in nums), reverse=True)]
        res = []
        for snum in snums:
            for c in snum:
                if c == "0" and not res:
                    continue
                res.append(c)
        return "".join(res) if res else "0"