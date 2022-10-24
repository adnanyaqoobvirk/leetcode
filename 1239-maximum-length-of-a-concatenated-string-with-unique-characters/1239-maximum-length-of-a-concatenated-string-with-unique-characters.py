class Solution:
    def maxLength(self, arr: List[str]) -> int:
        @cache
        def helper(i: int, mask: int) -> int:
            if i >= n:
                return bin(mask).count("1")
            
            cmask = 0
            for c in arr[i]:
                smask = 1 << (ord(c) - ord("a") + 1)
                if cmask & smask:
                    cmask = 0
                    break
                cmask |= smask
        
            return max(
                helper(i + 1, mask),
                helper(i + 1, mask if cmask & mask else (cmask | mask)),
                helper(i + 1, 0)
            )
        n = len(arr)
        return helper(0, 0)