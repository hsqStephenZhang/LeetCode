class Solution(object):
    def __init__(self, heap):
        self.heap = [0] + heap  # 第一位为哨兵
        self.length = len(heap)

    def smallheap(self):
        start = self.length // 2
        while start > 0:
            cur = start
            a = self.switch(cur)
            while a != cur:
                cur = a
                a = self.switch(cur)
            start -= 1

    def switch(self, i):
        if i * 2 + 1 <= self.length:
            if self.heap[i * 2] < self.heap[i * 2 + \
                1] and self.heap[i * 2] < self.heap[i]:
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                return i * 2
            if self.heap[i * 2 + 1] < self.heap[i * \
                2] and self.heap[i * 2] < self.heap[i]:
                self.heap[i], self.heap[i * 2 +
                                        1] = self.heap[i * 2 + 1], self.heap[i]
                return i * 2 + 1
            return i
        if i * 2 == self.length and self.heap[i * 2] < self.heap[i]:
            self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
        return i


if __name__ == '__main__':
    a = [4, 5, 6, 2, 3, 7, 8, 1]
    s = Solution(a)
    s.smallheap()
    print(s.heap)
