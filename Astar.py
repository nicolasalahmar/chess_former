import time
from PriorityQueue import PriorityQueue
import Helper

MAX_INT = 999999


class Astar:

    def find_holes(self, position):
        return [(position[0], x) for x in range(1, self.board.Dimensions[1] + 1) if
                (position[0] + 1, x) not in self.board.Walls]

    def heuristic(self, position):
        if self.board.KingPosition[0] > self.board.CastlePosition[0]:  # in case of elevation from the king find the
            hole_list = []  # nearest hole to this position and calculate the distance from it
            for hole in self.find_holes(position):
                hole_list.append(Helper.absolute_distance(position, hole))
            if hole_list:
                return min(hole_list) * 1000
            else:
                return MAX_INT
        elif self.board.KingPosition[0] == self.board.CastlePosition[0]:  # in case we are on the same level as the king
            return Helper.absolute_distance(position, self.board.KingPosition) * 1000
        else:
            return MAX_INT

    def __init__(self, board):
        self.dist = [[MAX_INT for _ in range(board.Dimensions[1] + 1)] for _ in
                     range(board.Dimensions[0] + 1)]  # dist list
        self.q = PriorityQueue()  # priority queue for ucs implementation
        self.board = board
        self.w = 1  # edge cost is always 1
        self.parent = Helper.initialize_dict(self.board)
        self.n = 0
        self.m = 0
        self.arr = []

    def Astar(self):
        x, y = self.board.CastlePosition
        self.dist[x][y] = 0
        self.q.push((self.board, 0))  # mark it as visited

        while not self.q.isEmpty():
            current_state, path = self.q.pop()  # pop the node we want to process from the queue

            x, y = current_state.CastlePosition

            self.m += 1
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
                    h = self.heuristic((current_state.CastlePosition[0], y))
                    self.q.push((child, self.dist[x][y] + h))

    def print_solution(self, i):
        if i is None:
            print("there is no solution!")
            return
        if not self.parent[i.CastlePosition]:
            self.arr.append(i)
            return
        self.print_solution(self.parent[i.CastlePosition].pop())
        print("=====================================================")
        i.print()
        self.arr.append(i)

    def loop(self):
        t1 = time.perf_counter()
        solution = self.Astar()
        t2 = time.perf_counter()

        self.print_solution(solution)
        print("\nthe path: ")
        solution_path = [x.CastlePosition for x in self.arr]
        print(solution_path)

        print()
        print("number of nodes traversed is:", self.n)
        print("number of nodes processed is:", self.m)
        print("the perfect amount of moves to get to the answer:",
              self.dist[self.board.KingPosition[0]][self.board.KingPosition[1]])
        print("time elapsed:", round(t2 - t1, 4), "s")

        return {"time_elapsed": round(t2 - t1, 4), "instantiated_nodes": self.n, "processed_nodes": self.m, "path": solution_path}
