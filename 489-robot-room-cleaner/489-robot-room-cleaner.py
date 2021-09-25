from typing import Tuple

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        def backtrack(cell: Tuple[int, int], d: int) -> None:
            robot.clean()
            seen.add(cell)
            
            for i in range(4):
                nd = (d + i) % 4
                ncell = (cell[0] + directions[nd][0], cell[1] + directions[nd][1])
                if ncell not in seen and robot.move():
                    backtrack(ncell, nd)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()
                
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        seen = set()
        backtrack((0, 0), 0)
        
            