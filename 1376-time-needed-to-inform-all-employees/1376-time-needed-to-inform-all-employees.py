class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        for employee, manager in enumerate(manager):
            tree[manager].append(employee)
            
        stack, ans = [(headID, 0)], 0
        while stack:
            manager, time = stack.pop()
            ans = max(ans, time)
            for employee in tree[manager]:
                stack.append((employee, time + informTime[manager]))
        return ans