class DFS:

    def __init__(self, board):
        self.visited = []
        self.board = board

    def equals(self, obj):
        for element in self.arr:
            if element.Equals(obj):
                return True
        return False

    def dfs(self, path=None):
        if path is None:
            path = []

        print(self.board.CastlePosition)

        if self.board.CastlePosition == self.board.KingPosition:
            return

        temp = self.board.get_next_states()

        for move in temp:
            if not self.equals(move):
                path.append(move)
                self.arr.append(move)
                self.board = move
                self.dfs()
                path.remove(move)

    def loop(self):
        print(self.dfs())
