class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        llogs, dlogs = [], []
        for idx, log in enumerate(logs):
            i = log.find(' ')
            if log[i + 1].isnumeric():
                dlogs.append(log)
            else:
                llogs.append((log[i + 1:], log[:i + 1], idx))
        llogs.sort()
        
        ans = [logs[idx] for _, _, idx in llogs]
        ans.extend(dlogs)
        return ans
        