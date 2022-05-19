class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        nodes, ans = {i for i in range(n)}, 0
        while nodes:
            stack = [nodes.pop()]
            while stack:
                src = stack.pop()
                for dst in range(n):
                    if isConnected[src][dst] == 1 and dst in nodes:
                        stack.append(dst)
                        nodes.remove(dst)
            ans += 1
        return ans