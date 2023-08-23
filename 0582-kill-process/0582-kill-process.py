class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)
        for i in range(len(ppid)):
            graph[ppid[i]].append(pid[i])
        
        ans, stack = [], [kill]
        while stack:
            curr = stack.pop()
            ans.append(curr)
            stack.extend(graph[curr])
            
        return ans
                