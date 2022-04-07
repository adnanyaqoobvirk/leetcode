class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans, counts = 0, Counter(arr)
        for i in range(101):
            if i not in counts:
                continue
            for j in range(i, 101):
                if j not in counts:
                    continue
                
                k = target - (i + j)
                if k < j or k not in counts:
                    continue
                    
                if i == j == k:
                    if counts[i] >= 3:
                        ans += comb(counts[i], 3)
                elif i == j:
                    if counts[i] >= 2:
                        ans += comb(counts[i], 2) * counts[k]
                elif j == k:
                    if counts[j] >= 2:
                        ans += comb(counts[j], 2) * counts[i]
                else:
                    ans += counts[i] * counts[j] * counts[k]
        return ans % (10**9 + 7)