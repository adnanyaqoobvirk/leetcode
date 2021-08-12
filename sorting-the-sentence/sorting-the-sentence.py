class Solution:
    def sortSentence(self, s: str) -> str:
        word_map = {}
        for word in s.split():
            word_map[int(word[-1])] = word[:len(word) - 1]
        return " ".join(word_map.get(i, "") for i in range(1, len(word_map) + 1))