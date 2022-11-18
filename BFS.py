class BFS:
    def __init__(self, board):
        self.visited = []
        self.q = []  # queue for bfs implementation
        self.board = board
        self.path = []

    def bfs(self):
        self.path.append(self.board)
        self.visited.append(self.board)     # just append the first position into the queue
        self.q.append(self.board)           # mark it as visited
        while self.q:
            current_state = self.q.pop(0)    # pop the node we want to process from the queue
            next_states = current_state.get_next_states()    # get all next states adjacent to current position
            self.path.append(current_state)
            if current_state.Solved():  # check if final state break
                return current_state

            for state in next_states:
                if self.state_not_in_path(state):
                    
                    if state.Solved():  # check if final state break
                        return state
                    
                    self.q.append(state)
                    self.visited.append(state)

    def state_not_in_path(self, state):
        for obj in self.visited:    # todo this doesn't feel right
            if obj.CastlePosition == state.CastlePosition:
                return False
        return True

    def loop(self):
        solution = self.bfs()
        print([x.CastlePosition for x in self.path])
        solution.print()
