class Solution:
    def sortString(self, s: str) -> str:
        def process(rng):
            stop = True
            for i in rng:
                if char_count[i] > 0:
                    result.append(chr(ord('a') + i))
                    char_count[i] -= 1
                    stop = False
            return stop
        
        char_count = [0] * 26
        for c in s:
            char_count[ord(c) - ord('a')] += 1
        
        result = []
        stop = False
        for _ in range(len(s)):
            stop = process(range(26))
            if stop:
                break
            stop = process(range(25, -1, -1))
        return "".join(result)