class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        counts = {word: Counter(word) for word in words}
        stack = []
        for word in words:
            if stack and counts[word] == counts[stack[-1]]:
                continue
            stack.append(word)
        return stack