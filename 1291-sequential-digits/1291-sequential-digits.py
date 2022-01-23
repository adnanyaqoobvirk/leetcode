class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans, low_count, high_count = [], len(str(low)), len(str(high))
        for wsize in range(low_count, high_count + 1):
            for d in range(1, 10):
                num = 0
                for i in range(wsize):
                    if d + i > 9:
                        break
                    num = num * 10 + d + i
                else:
                    if low <= num <= high:
                        ans.append(num)
        return ans