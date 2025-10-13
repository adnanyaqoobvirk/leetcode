class Solution:
    def __init__(self):
        self.counts = {}

    def removeAnagrams(self, words: List[str]) -> List[str]:
        for word in words:
            if word not in self.counts:
                self.counts[word] = Counter(word)

        stack = []
        for word in words:
            if stack and self.counts[word] == self.counts[stack[-1]]:
                continue
            stack.append(word)
        return stack