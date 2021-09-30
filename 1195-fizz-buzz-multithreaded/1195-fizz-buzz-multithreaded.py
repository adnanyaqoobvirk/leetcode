from threading import Event

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.event = Event()
        self.count = 1

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while self.count <= self.n:
            if self.count % 3 == 0 and self.count % 5 != 0:
                printFizz()
                self.count += 1
                self.event.set()
            else:
                self.event.clear()
                self.event.wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while self.count <= self.n:
            if self.count % 3 != 0 and self.count % 5 == 0:
                printBuzz()
                self.count += 1
                self.event.set()
            else:
                self.event.clear()
                self.event.wait()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.count <= self.n:
            if self.count % 3 == 0 and self.count % 5 == 0:
                printFizzBuzz()
                self.count += 1
                self.event.set()
            else:
                self.event.clear()
                self.event.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.count <= self.n:
            if self.count % 3 != 0 and self.count % 5 != 0:
                printNumber(self.count)
                self.count += 1
                self.event.set()
            else:
                self.event.clear()
                self.event.wait()