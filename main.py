import random


class AnalysisArray:
    arr = list()

    def __init__(self):
        self.arr = list()

    def generate_up(self, n):
        self.arr = list(range(1, n+1))

    def generate_rand(self, n):
        self.arr.clear()
        for i in range(n):
            self.arr.append(random.randint(1, n))

    def generate_down(self, n):
        self.arr = list(range(n, 0, -1))

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

    def shell_sort(self):
        total_swaps = 0
        total_compares = 0
        d = len(self.arr) // 2
        while d:
            for i in range(d):
                for j in range(i+d, len(self.arr), d):
                    k = j
                    total_compares += 1
                    while k > d-1 and self.arr[k] < self.arr[k-d]:
                        self.arr[k], self.arr[k-d] = self.arr[k-d], self.arr[k]
                        total_swaps += 1
                        k -= d
            d = d // 2

        return total_compares, total_swaps

    def count_sort(self):
        counts = [0] * (len(self.arr) + 1)
        for el in self.arr:
            counts[el] += 1

        new_arr = []

        for i in range(len(counts)):
            new_arr.extend([i]*counts[i])

        self.arr = new_arr


if __name__ == "__main__":
    test = AnalysisArray()
    test.generate_up(100)
    print(*test.arr)
    test.shell_sort()
    print(*test.arr)
