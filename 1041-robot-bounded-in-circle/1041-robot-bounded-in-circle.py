class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr, direction = [0, 0], 'N'
        for _ in range(4):
            for i in instructions:
                if i == 'G':
                    if direction == 'N':
                        curr[0] += 1
                    elif direction == 'S':
                        curr[0] -= 1
                    elif direction == 'E':
                        curr[1] += 1
                    else:
                        curr[1] -= 1
                elif i == 'L':
                    if direction == 'N':
                        direction = 'W'
                    elif direction == 'S':
                        direction = 'E'
                    elif direction == 'E':
                        direction = 'N'
                    else:
                        direction = 'S'
                else:
                    if direction == 'N':
                        direction = 'E'
                    elif direction == 'S':
                        direction = 'W'
                    elif direction == 'E':
                        direction = 'S'
                    else:
                        direction = 'N'
            if curr[0] == 0 and curr[1] == 0:
                return True
        return False