import time
from PriorityQueue import PriorityQueue


class UCS:
    MAX_INT = 999999

    def __init__(self, board):
        self.dist = [[UCS.MAX_INT for _ in range(board.Dimensions[1] + 1)] for _ in
                     range(board.Dimensions[0] + 1)]  # dist list
        self.q = PriorityQueue()  # priority queue for ucs implementation
        self.board = board
        self.w = 1  # edge cost is always 1
        self.parent = {}
        self.n = 0

    def ucs(self):
        x, y = self.board.CastlePosition
        self.dist[x][y] = 0
        self.q.push((self.board, 0))  # mark it as visited
        self.parent[(x, y)] = (-1, -1)

        while not self.q.isEmpty():
            current_state, path = self.q.pop()  # pop the node we want to process from the queue

            x, y = current_state.CastlePosition

            if path > self.dist[x][y]:
                continue

            for child in current_state.get_next_states():
                self.n += 1
                x, y = child.CastlePosition  # x and y of child
                if path + self.w < self.dist[x][y]:
                    self.parent[(x, y)] = current_state.CastlePosition
                    self.dist[x][y] = path + self.w
                    self.q.push((child, self.dist[x][y]))

    def loop(self):
        t1 = time.perf_counter()
        self.ucs()
        t2 = time.perf_counter()
        print(self.dist[10][10])
        print("the path:")

        i = (10, 10)
        while i != (-1, -1):
            print(i, end=' ')
            i = self.parent[i]

        print()
        print("the number of nodes is:", self.n)
        print("time elapsed:", round(t2 - t1, 4), "s")
