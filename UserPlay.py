class UserPlay:
    def __init__(self, board):
        self.board = board

    def prompt(self):
        moves = self.board.check_moves()
        position = input(f"where do you want to move the castle?\nP.S: the allowed moves are {moves}\n")

        if len(position) < 1:
            position = moves[0]
        else:
            position = tuple([int(x) for x in position.split(',')])

        new_board = self.board.move(position)
        if new_board is not None:
            self.board = new_board
            self.board.print()
        else:
            self.board.print()

    def loop(self):
        while not self.board.Solved():
            self.prompt()
        print('Hooray!')
