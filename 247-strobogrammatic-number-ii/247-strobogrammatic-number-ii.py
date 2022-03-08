class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n & 1:
            ans = ["0", "1", "8"]
            n -= 1
        else:
            ans = [""]
            
        for i in range(n, 0, -2):
            nans = []
            for left, right in ["00", "11", "88", "69", "96"]:
                if i != 2 or left != "0":
                    for num in ans:
                        nans.append(f"{left}{num}{right}")
            ans = nans
        return ans