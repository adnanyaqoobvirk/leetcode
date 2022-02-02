class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcounts, scounts, ans = Counter(p), Counter(s[:len(p)]), []   
        for i in range(len(s) - len(p) + 1):
            if i > 0:
                start, end = s[i - 1], s[i + len(p) - 1]
                scounts[start] -= 1
                scounts[end] += 1
            
            for k, v in pcounts.items():
                if scounts[k] != v:
                    break
            else:
                ans.append(i)
        return ans