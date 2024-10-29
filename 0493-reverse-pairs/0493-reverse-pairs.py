class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def update(i):
            while i <= n:
                bit[i] += 1
                i += i & -i
        
        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res
        
        nmap = {v: i for i, v in enumerate(sorted(set(nums)), 1)}
        n = 2 * len(nmap) + 1
        bit = [0] * (n + 1)

        ans = 0
        for num in nums:
            if num <= 0:
                ans += query(n) - query(nmap[num] // 2 - 1)
            else:
                ans += query(n) - query(2 * nmap[num])
            update(nmap[num])
        return ans