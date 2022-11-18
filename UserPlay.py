class UserPlay:
    def __init__(self, board):
        self.board = board

    def prompt(self):
        moves = self.board.check_moves() + self.board.check_moves_up()
        position = input(f"where do you want to move the castle?\nP.S: the allowed moves are {moves}\n")

        if len(position) < 1:
            position = moves[0]
        else:
            position = tuple([int(x) for x in position.split(',')])

        new_board, path = self.board.move(position)
        if new_board is not None:
            self.board = new_board
            self.board.print()
            print('the path:', self.board.path)     # todo this might be changed the second i figure out what the fuck path is 
        else:
            self.board.print()

    def loop(self):
        while not self.board.Solved():
            self.prompt()
        print('Hooray!')
