class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n & 1:
            n -= 1
            ans = ["0", "1", "8"] 
        else:
            ans = [""]
            
        for i in range(n, 0, -2):
            nans = []
            for s in ans:
                if i != 2:
                    nans.append(f"0{s}0")
                nans.extend([f"1{s}1", f"8{s}8", f"6{s}9", f"9{s}6"])
            ans = nans
        return ans