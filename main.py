import random


class AnalysisArray:
    arr = list()

    def __init__(self):
        self.arr = list()

    def generate_up(self, n):
        self.arr = range(1, n+1)

    def generate_rand(self, n):
        self.arr.clear()
        for i in range(n):
            self.arr.append(random.randint(1, n))

    def generate_down(self, n):
        self.arr = range(n, 0, -1)


if __name__ == "__main__":
    pass
