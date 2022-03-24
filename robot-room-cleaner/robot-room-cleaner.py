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
        """
        :type robot: Robot
        :rtype: None
        """
        def backtrack(i: int, j: int, d: int) -> None:
            for k in range(4):
                nd = (d + k) % 4
                x, y = i + dmap[nd][0], j + dmap[nd][1]
                if (x, y) not in cleaned:
                    if robot.move():
                        robot.clean()
                        cleaned.add((x, y))
                        backtrack(x, y, nd)
                        robot.turnRight()
                        robot.turnRight()
                        robot.move()
                        robot.turnRight()
                        robot.turnRight()
                robot.turnRight()
        dmap = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        cleaned = {(0, 0)}
        robot.clean()
        backtrack(0, 0, 0)