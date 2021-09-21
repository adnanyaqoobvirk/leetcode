class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        tcounts = {}
        acounts = {}
        for i in range(len(arr)):
            tcounts[target[i]] = tcounts.get(target[i], 0) + 1
            acounts[arr[i]] = acounts.get(arr[i], 0) + 1
        
        for k, v in tcounts.items():
            if acounts.get(k, 0) != v:
                return False
        return True
            