class Solution:
    def expand(self, s: str) -> List[str]:
        def helper(pos: int) -> None:
            if pos == n:
                ans.append("".join(word))
            else:
                if s[pos] == '{':
                    options = []
                    for i in range(pos + 1, n):
                        if s[i] == ',':
                            continue
                        elif s[i] != '}':
                            options.append(s[i])
                        else:
                            break

                    for c in sorted(options):
                        word.append(c)
                        helper(i + 1)
                        word.pop()
                else:
                    word.append(s[pos])
                    helper(pos + 1)
                    word.pop()
        
        n, ans, word = len(s), [], []
        helper(0)
        return ans