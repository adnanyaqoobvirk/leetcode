class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        output = []
        start = ord('a') - 1
        left = 0
        right = 2
        while left < n:
            if right < n and s[right] == '#':
                output.append(
                    chr(start + int(s[left]) * 10 + int(s[left + 1]))
                )
                left += 3
                right += 3
            else:
                output.append(chr(start + int(s[left])))
                left += 1
                right += 1
        return "".join(output)