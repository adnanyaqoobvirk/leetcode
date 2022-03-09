class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def queue_adjacent(
            queue: List[Tuple[int, int, int]], 
            x: int, y: int, distance: int
        ):
            queue.append((x + 1, y, distance))
            queue.append((x, y + 1, distance))
            queue.append((x - 1, y, distance))
            queue.append((x, y - 1, distance))
        
        q, n, m = [], len(rooms), len(rooms[0])
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue_adjacent(q, i, j, 0)
        
        while q:
            nq = []
            for i, j, d in q:
                d += 1
                if 0 <= i < n and 0 <= j < m and rooms[i][j] == 2147483647:
                    rooms[i][j] = d
                    queue_adjacent(nq, i, j, d)
            q = nq