class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_idx = -1
        for i in range(len(word)):
            if word[i] == ch:
                ch_idx = i
                break
        
        if ch_idx == -1:
            return word
        
        ans = []
        for i in reversed(range(ch_idx + 1)):
            ans.append(word[i])
        
        for i in range(ch_idx + 1, len(word)):
            ans.append(word[i])
        
        return "".join(ans)