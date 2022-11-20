import bisect


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def push(self, data):
        bisect.insort_left(self.queue, data, key=lambda element: element[1])

    def pop(self):
        return self.queue.pop()
