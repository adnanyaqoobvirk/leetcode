class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = defaultdict(list)
        for i, c in enumerate(s):
            if not intervals[c]:
                intervals[c].append(i)
                intervals[c].append(i)
            else:
                intervals[c][-1] = i
        
        ans, (start, end) = [], intervals[s[0]] 
        for i in range(1, len(s)):
            istart, iend = intervals[s[i]]
            if start <= istart <= end:
                end = max(iend, end)
            else:
                ans.append(end - start + 1)
                start, end = istart, iend
        ans.append(end - start + 1)
        return ans