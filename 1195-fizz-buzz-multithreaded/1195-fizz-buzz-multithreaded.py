from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.f = Lock()
        self.b = Lock()
        self.fb = Lock()
        self.num = Lock()
        
        self.f.acquire()
        self.b.acquire()
        self.fb.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.f.acquire()
            if self.n == 0:
                break
            printFizz()
            self.num.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.b.acquire()
            if self.n == 0:
                break
            printBuzz()
            self.num.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fb.acquire()
            if self.n == 0:
                break
            printFizzBuzz()
            self.num.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.num.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fb.release()
            elif i % 3 == 0:
                self.f.release()
            elif i % 5 == 0:
                self.b.release()
            else:
                printNumber(i)
                self.num.release()
            
        self.num.acquire()
        self.n = 0
        self.fb.release()
        self.b.release()
        self.f.release()