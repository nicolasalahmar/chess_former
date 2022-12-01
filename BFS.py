import time
import Helper


class BFS:
    def __init__(self, board):
        self.visited = []
        self.q = []  # queue for bfs implementation
        self.board = board
        self.n = 0
        self.m = 0

    def bfs(self):
        self.visited.append(self.board)  # just append the first position into the queue
        self.q.append(self.board)  # mark it as visited
        while self.q:
            current_state = self.q.pop(0)  # pop the node we want to process from the queue
            current_state.path.append(current_state.CastlePosition)
            self.m += 1
            if current_state.Solved():  # check if final state break
                return current_state
            for state in current_state.get_next_states():
                self.n += 1
                if state.not_parent(state.CastlePosition):
                    self.q.append(state)
                    self.visited.append(state)

    def loop(self):
        t1 = time.perf_counter()
        solution = self.bfs()
        t2 = time.perf_counter()
        Helper.print_blind_search(solution, self.n, self.m, t2, t1)
        return {"time_elapsed": round(t2 - t1, 4), "instantiated_nodes": self.n, "processed_nodes": self.m, "path": solution.path}
