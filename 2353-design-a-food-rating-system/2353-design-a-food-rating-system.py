class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cmap = defaultdict(list)
        self.fmap = {}
        for i in range(len(foods)):
            self.fmap[foods[i]] = [ratings[i], cuisines[i]]
            self.cmap[cuisines[i]].append((-ratings[i], foods[i]))
        for l in self.cmap.values():
            heapify(l)

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating, cuisine = self.fmap[food]
        clist = self.cmap[cuisine]
        
        heappush(clist, (-newRating, food))
        self.fmap[food][0] = newRating

        while clist:
            rating, food = clist[0]
            if self.fmap[food][0] != -rating:
                heappop(clist)
            else:
                break

    def highestRated(self, cuisine: str) -> str:
        return self.cmap[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)