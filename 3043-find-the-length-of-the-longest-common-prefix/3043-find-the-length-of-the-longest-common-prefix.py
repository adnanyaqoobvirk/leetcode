class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = {}
        for num in arr1:
            snum = str(num)
            t = trie
            for d in snum:
                if d not in t:
                    t[d] = {}
                t = t[d]
        
        max_len = 0
        for num in arr2:
            snum = str(num)
            t = trie
            count = 0
            for d in snum:
                if d not in t:
                    break
                t = t[d]
                count += 1
            max_len = max(max_len, count)
        return max_len