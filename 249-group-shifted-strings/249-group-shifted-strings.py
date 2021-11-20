class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)
        for s in strings:
            ans[
                tuple((ord(s[i - 1]) - ord(s[i])) % 26 
                      for i in range(1, len(s)))
            ].append(s)
        return ans.values()