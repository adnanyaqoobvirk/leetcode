class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        wmap, n, intervals = set(words), len(s), []
        for i in range(n):
            for j in range(i, n):
                if s[i:j + 1] in wmap:
                    if intervals and i - 1 <= intervals[-1][1]:
                        intervals[-1][1] = max(j, intervals[-1][1])
                    else:
                        intervals.append([i, j])
                        
        ans, prev = [], 0
        for start, end in intervals:
            ans.append(s[prev:start])
            ans.append("<b>")
            ans.append(s[start:end + 1])
            ans.append("</b>")
            prev = end + 1
        if prev < n:
            ans.append(s[prev:])
        return "".join(ans)