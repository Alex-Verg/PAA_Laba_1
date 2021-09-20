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

    def bubble_sort(self):
        total_swaps = 0
        total_compares = 0
        for i in range(len(self.arr)-1):
            swaps = 0
            for j in range(len(self.arr)-i-1):
                total_compares += 1
                if self.arr[j+1] < self.arr[j]:
                    self.arr[j+1], self.arr[j] = self.arr[j], self.arr[j+1]
                    swaps += 1
            total_swaps += swaps
            if not swaps:
                break

        return total_compares, total_swaps


if __name__ == "__main__":
    test = AnalysisArray()
    test.generate_rand(50)
    test.bubble_sort()
    print(*test.arr)
