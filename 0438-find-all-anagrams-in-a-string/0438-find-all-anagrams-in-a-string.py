class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        pcounts = Counter(p)
        scounts = Counter(s[:np])

        ans = []
        if pcounts == scounts:
            ans.append(0)

        for i in range(np, ns):
            scounts[s[i]] += 1
            scounts[s[i - np]] -= 1

            if pcounts == scounts:
                ans.append(i - np + 1)
        
        return ans