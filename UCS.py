import time
from PriorityQueue import PriorityQueue


def initialize_dict(board):
    temp = {}
    for i in range(board.Dimensions[0] + 1):
        for j in range(board.Dimensions[1] + 1):
            temp[(i, j)] = []
    return temp


class UCS:
    MAX_INT = 999999

    def __init__(self, board):
        self.dist = [[UCS.MAX_INT for _ in range(board.Dimensions[1] + 1)] for _ in
                     range(board.Dimensions[0] + 1)]  # dist list
        self.q = PriorityQueue()  # priority queue for ucs implementation
        self.board = board
        self.w = 1  # edge cost is always 1
        self.parent = initialize_dict(self.board)
        self.n = 0

    def ucs(self):
        x, y = self.board.CastlePosition
        self.dist[x][y] = 0
        self.q.push((self.board, 0))  # mark it as visited

        while not self.q.isEmpty():
            current_state, path = self.q.pop()  # pop the node we want to process from the queue

            x, y = current_state.CastlePosition

            if current_state.Solved():
                return current_state

            if path > self.dist[x][y]:
                continue

            for child in current_state.get_next_states():
                self.n += 1
                x, y = child.CastlePosition  # x and y of child
                if path + self.w < self.dist[x][y]:
                    self.parent[(x, y)].append(current_state)
                    self.dist[x][y] = path + self.w
                    self.q.push((child, self.dist[x][y]))

    def print_solution(self, i):
        if not self.parent[i.CastlePosition]:
            return
        self.print_solution(self.parent[i.CastlePosition].pop())
        print("=====================================================")
        i.print()

    def loop(self):
        t1 = time.perf_counter()
        solution = self.ucs()
        t2 = time.perf_counter()
        print("the path:")

        self.print_solution(solution)

        print()
        print("the number of nodes is:", self.n)
        print("the perfect amount of moves to get to the answer:",
              self.dist[self.board.KingPosition[0]][self.board.KingPosition[1]])
        print("time elapsed:", round(t2 - t1, 4), "s")

        return {"time_elapsed": round(t2 - t1, 4), "number_of_nodes": self.n}
