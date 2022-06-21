class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]
        for i in range(2, len(coordinates)):
            curr_dy = coordinates[i][1] - coordinates[i - 1][1]
            curr_dx = coordinates[i][0] - coordinates[i - 1][0]
            if dx * curr_dy != dy * curr_dx:
                return False
        return True