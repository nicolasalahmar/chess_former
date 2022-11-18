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
            if current_state.Solved():  # check if final state break
                return current_state
            current_state.path.append(current_state)
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
        solution = self.bfs()
        print([x.CastlePosition for x in solution.path])
        solution.print()
