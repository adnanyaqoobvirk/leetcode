class StockSpanner:

    def __init__(self):
        self.s = [(0, inf)]

    def next(self, price: int) -> int:
        total = 1
        while self.s[-1][1] <= price:
            total += self.s[-1][0]
            self.s.pop()
        self.s.append((total, price))
        return total

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)