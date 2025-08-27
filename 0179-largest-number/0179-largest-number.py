class SNum:
    def __init__(self, v: int) -> None:
        self.v = str(v)
    
    def __lt__(self, other: 'Snum') -> bool:
        return self.v + other.v < other.v + self.v

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = "".join(snum.v for snum in sorted((SNum(num) for num in nums), reverse=True))
        return "0" if res[0] == "0" else res