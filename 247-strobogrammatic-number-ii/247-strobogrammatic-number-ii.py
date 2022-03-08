class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n & 1:
            ans = ["0", "1", "8"]
            n -= 1
        else:
            ans = [""]
            
        for i in range(0, n, 2):
            nans = []
            for left, right in ["00", "11", "88", "69", "96"]:
                for num in ans:
                    nans.append(f"{left}{num}{right}")
            ans = nans
        return [num for num in ans if len(num) == 1 or num[0] != "0"]