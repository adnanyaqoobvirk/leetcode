class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = []
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            d.append((a, b))
        ans = 0
        for c in Counter(d).values():
            ans += (c * (c - 1)) // 2
        return ans
            