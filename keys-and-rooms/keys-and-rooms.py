class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def helper(room: int) -> None:
            for key in rooms[room]:
                if not unlocked[key]:
                    unlocked[key] = True
                    helper(key)
        unlocked = [False] * len(rooms)
        unlocked[0] = True
        helper(0)
        return all(unlocked)