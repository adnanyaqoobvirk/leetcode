class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_positions = defaultdict(list)
        for i in range(len(s)):
            char = s[i]
            if len(char_positions[char]) < 2:
                char_positions[char].append(i)
            else:
                char_positions[char][1] = i
        
        subsequence_count = 0
        for char, positions in char_positions.items():
            if len(positions) < 2:
                continue
            
            unique_chars = set()
            for i in range(positions[0] + 1, positions[1]):
                unique_chars.add(s[i])
            
            if len(unique_chars) >= 1:
                subsequence_count += len(unique_chars)
        return subsequence_count