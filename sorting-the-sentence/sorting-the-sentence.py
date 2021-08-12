class Solution:
    def sortSentence(self, s: str) -> str:
        output = [None] * 9
        for subStr in s.split():
            output[int(subStr[-1]) - 1] = subStr[:len(subStr) - 1]
        return " ".join(subStr for subStr in output if subStr)