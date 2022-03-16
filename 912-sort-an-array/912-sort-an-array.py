class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        q = [[num] for num in nums]
        while len(q) > 1:
            nq = []
            for i in range(0, len(q), 2):
                left, right = q[i], q[i + 1] if i + 1 < len(q) else []
                
                merged, n, m = [], len(left), len(right)
                lp = rp = 0
                while lp < n and rp < m:
                    if left[lp] <= right[rp]:
                        merged.append(left[lp])
                        lp += 1
                    else:
                        merged.append(right[rp])
                        rp += 1
                
                remaining, p, l = (left, lp, n) if lp < n else (right, rp, m)
                while p < l:
                    merged.append(remaining[p])
                    p += 1
                
                nq.append(merged)
            q = nq
        return q[0]