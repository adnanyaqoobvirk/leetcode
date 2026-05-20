class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, d = 0, 0, 0
        seen = {(x, y, d)}
        cleaned = set()
        while True:
            cleaned.add((x, y))
            nx, ny, nd = x, y, d
            for i in range(len(dirs)):
                nd = (d + i) % len(dirs)
                dx, dy = dirs[nd]
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and room[nx][ny] == 0:
                    if (nx, ny, nd) in seen:
                        return len(cleaned)
                    seen.add((nx, ny, nd))
                    break
            else:
                break
            x, y, d = nx, ny, nd
        return len(cleaned)