class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def getCount(guess: int) -> Tuple[int, int]:
            count, maxval, i, j = 0, float('-inf'), n - 1, 0
            for j in range(n):
                for i in reversed(range(n)):
                    if matrix[i][j] > guess:
                        continue
                    else:
                        maxval = max(maxval, matrix[i][j])
                        count += i + 1
                        break
            return count, maxval
        
        n, lo, hi = len(matrix), matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            guess = lo + (hi - lo) // 2
            count, _ = getCount(guess)
            
            if count > k:
                hi = guess - 1
            else:
                lo = guess + 1
        count, val = getCount(hi)
        if count >= k:
            return val
        else:
            return getCount(lo)[1]