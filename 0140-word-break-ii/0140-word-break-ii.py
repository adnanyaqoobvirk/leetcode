class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(i: int) -> None:
            if i >= n:
                ans.append(" ".join(st))
            else:
                t = trie
                for j in range(i, n):
                    if s[j] not in t:
                        break
                    t = t[s[j]]
                    if "#" in t:
                        st.append(s[i:j + 1])
                        backtrack(j + 1)
                        st.pop()  

        n = len(s)

        trie = {}
        for word in wordDict:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["#"] = {}

        ans = []
        st = []
        backtrack(0)
        return ans