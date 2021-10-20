class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        word = []
        for c in s:
            if c == ' ':
                if word:
                    ans.append("".join(word))
                    word = []
            else:
                word.append(c)
        
        if word:
            ans.append("".join(word))
            
        return " ".join(reversed(ans))