class Solution:
    def grayCode(self, n: int) -> List[int]:
        def getBit(pos: int) -> int:
            while True:
                for _ in range(pos):
                    yield 0
                for _ in range(pos * 2):
                    yield 1
                for _ in range(pos):
                    yield 0
        
        ans = []
        bits = [getBit(2**i) for i in range(n)]
        for _ in range(1 << n):
            num = 0
            for i in range(n):
                num |= next(bits[i]) << i
            ans.append(num)
        return ans