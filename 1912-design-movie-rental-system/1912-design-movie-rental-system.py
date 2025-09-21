class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.rented = SortedList()
        self.unrented = defaultdict(SortedList)
        self.prices = defaultdict(int)

        for shop, movie, price in entries:
            self.unrented[movie].add((price, shop))
            self.prices[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        l = len(self.unrented[movie])
        ans = []
        for i in range(5):
            if i >= l:
                break
            price, shop = self.unrented[movie][i]
            ans.append(shop)
        return ans

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.unrented[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        l = len(self.rented)
        ans = []
        for i in range(5):
            if i >= l:
                break
            price, shop, movie = self.rented[i]
            ans.append([shop, movie])
        return ans


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()