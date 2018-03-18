def f():
    print('in f() 1')
    yield 1
    print('in f() 2')
    yield 2
    print('in f() 3')
    yield 3


g = f()
g.__next__()
g.__next__()
g.__next__()
g.__iter__()
g2 = f()
for x in g2:
    print('')


class MyNumber:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isMyNumber(self, k):
        if k < 2:
            return False
        for x in range(2, k):
            if k % x == 0:
                return False
        return True

    def __iter__(self):
        for x in range(self.start, self.end):
            if self.isMyNumber(x):
                yield x


for x in MyNumber(1, 10000):
    print(x)
