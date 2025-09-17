from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cmap = defaultdict(SortedSet)
        self.fmap = {}
        for i in range(len(foods)):
            self.fmap[foods[i]] = [ratings[i], cuisines[i]]
            self.cmap[cuisines[i]].add((-ratings[i], foods[i])) 

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating, cuisine = self.fmap[food]
        self.cmap[cuisine].remove((-oldRating, food))
        self.cmap[cuisine].add((-newRating, food))
        self.fmap[food][0] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cmap[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)