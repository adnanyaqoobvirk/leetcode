class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = ["Push"]
        pos = 0
        stack = [1]
        
        for i in range(2, n + 1):
            if target[pos] > stack[-1]:
                stack.pop()
                ans.append("Pop")
            elif target[pos] == stack[-1]:
                pos += 1
            
            if pos == len(target):
                break
                
            stack.append(i)
            ans.append("Push")
        
        return ans
            
            