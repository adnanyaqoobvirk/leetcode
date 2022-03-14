class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def helper(room: int) -> None:
            for key in rooms[room]:
                if key not in unlocked:
                    unlocked.add(key)
                    helper(key)
        unlocked = {0}
        helper(0)
        return len(unlocked) == len(rooms)