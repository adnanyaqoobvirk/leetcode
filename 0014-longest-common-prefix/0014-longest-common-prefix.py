class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)

        if min_len == 0:
            return ""

        prefix = []
        for i in range(min_len):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j - 1][i]:
                    break
            else:
                prefix.append(strs[0][i])
                continue
            break
        return "".join(prefix)