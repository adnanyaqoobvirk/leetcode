class Solution:
    def kthCharacter(self, k: int) -> str:
        word = [0]
        l = 1
        j = 0
        for i in range(k - 1):
            if j == l:
                j = 0
                l = len(word)
            word.append((word[j] + 1) % 26)
            j += 1
        return chr(ord('a') + word[-1])