class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = []
        for i in range(len(word)):
            if word[i] == ch:
                break
        else:
            return word
            
        for j in range(i, -1, -1):
            ans.append(word[j])
        
        for j in range(i + 1, len(word)):
            ans.append(word[j])
        
        return "".join(ans)