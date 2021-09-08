class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        output = []
        for i in range(max(l1, l2)):
            if i < l1:
                output.append(word1[i])
            
            if i < l2:
                output.append(word2[i])
        return "".join(output)