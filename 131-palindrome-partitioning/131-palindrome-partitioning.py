class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(ss: str) -> bool:
            left, right = 0, len(ss) - 1
            while left < right:
                if ss[left] != ss[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def helper(pos: int, ss: str) -> None:
            if pos == n:
                partition.append(ss)
                for p in partition:
                    if not isPalindrome(p):
                        break
                else:
                    ans.append(partition[:])
                partition.pop()
            else:
                if ss:
                    partition.append(ss)
                    helper(pos + 1, s[pos])
                    partition.pop()
                helper(pos + 1, ss + s[pos])
                
        n, partition, ans = len(s), [], []
        helper(0, "")
        return ans