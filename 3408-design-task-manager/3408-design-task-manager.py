class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.pmap = {}
        self.umap = {}
        for u, t, p in tasks:
            self.heap.append((-p, -t, u))
            self.pmap[(t, u)] = p
            self.umap[t] = u

        heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.pmap[(taskId, userId)] = priority
        self.umap[taskId] = userId
        heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.pmap[(taskId, self.umap[taskId])] = newPriority
        heappush(self.heap, (-newPriority, -taskId, self.umap[taskId]))

    def rmv(self, taskId: int) -> None:
        del self.pmap[(taskId, self.umap[taskId])]
        del self.umap[taskId]

    def execTop(self) -> int:
        while self.heap:
            p, t, u = heappop(self.heap)
            if (-t, u) in self.pmap and self.pmap[(-t, u)] == -p:
                self.rmv(-t)
                return u
            
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()