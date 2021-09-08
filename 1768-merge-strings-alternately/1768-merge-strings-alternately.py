class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        l1, l2 = len(word1), len(word2)
        output = []
        while p1 < l1 or p2 < l2:
            if p1 < l1:
                output.append(word1[p1])
                p1 += 1
            
            if p2 < l2:
                output.append(word2[p2])
                p2 += 1
        return "".join(output)