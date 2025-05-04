class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.ss = {(0, 0)}
        self.sq = deque([(0, 0)])
        self.fi = 0
        self.food = food
        self.dmap = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        self.width = width
        self.height = height

    def move(self, direction: str) -> int:
        px, py = self.sq[0]
        px += self.dmap[direction][0]
        py += self.dmap[direction][1]

        if not (0 <= px < self.height and 0 <= py < self.width):
            return -1

        if self.fi < len(self.food) and px == self.food[self.fi][0] and py == self.food[self.fi][1]:
            self.fi += 1
        else:
            r = self.sq.pop()
            self.ss.remove(r)
        
        if (px, py) in self.ss:
            return -1

        self.sq.appendleft((px, py))
        self.ss.add((px, py))
        
        return len(self.ss) - 1
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)