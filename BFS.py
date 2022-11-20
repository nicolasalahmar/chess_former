import time


class BFS:
    def __init__(self, board):
        self.visited = []
        self.q = []  # queue for bfs implementation
        self.board = board

    def bfs(self):
        self.visited.append(self.board)  # just append the first position into the queue
        self.q.append(self.board)  # mark it as visited
        while self.q:
            current_state = self.q.pop(0)  # pop the node we want to process from the queue
            current_state.path.append(current_state)
            if current_state.Solved():  # check if final state break
                return current_state
            for state in current_state.get_next_states():
                if self.state_not_in_path(state):
                    self.q.append(state)
                    self.visited.append(state)

    def state_not_in_path(self, obj1):
        for obj2 in self.visited:
            if obj2.Equals(obj1):
                return False
        return True

    def loop(self):
        t1 = time.perf_counter()
        solution = self.bfs()
        t2 = time.perf_counter()
        for x in solution.path:
            x.print()
            print()

        path_list = [x.CastlePosition for x in solution.path]
        print("number of nodes in path is:", len(path_list))
        print(path_list)

        s = 0
        l1 = [x.path for x in self.visited]
        for el in l1:
            temp = [x.CastlePosition for x in el]
            s += len(temp)

        print("number of visited nodes", s)
        print("time elapsed:", round(t2 - t1, 4), "s")
