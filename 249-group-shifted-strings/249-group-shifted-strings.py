class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        n = len(strings)
        ans = []
        done = set()
        for i in range(n):
            if i not in done:
                done.add(i)
                group = [strings[i]]
                for j in range(i + 1, n):
                    if j not in done and len(strings[i]) == len(strings[j]):
                        diff = ord(strings[i][0]) - ord(strings[j][0])
                        l = (26 + diff if diff < 0 else diff)
                        for k in range(1, len(strings[i])):
                            diff = ord(strings[i][k]) - ord(strings[j][k])
                            if (26 + diff if diff < 0 else diff) != l:
                                break
                        else:
                            done.add(j)
                            group.append(strings[j])
                ans.append(group)
        return ans