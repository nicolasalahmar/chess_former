import Helper


class Board:
    def __init__(self, Dimensions, KingPosition, CastlePosition, Walls, filename=None, path=None):
        if path is None:
            path = []

        self.Dimensions = None
        self.KingPosition = None
        self.CastlePosition = None
        self.Walls = None
        self.path = path

        if filename is not None:
            self.file_constructor(filename)
        else:
            self.deepCopy(Dimensions, KingPosition, CastlePosition, Walls, path)

    def not_parent(self, x):
        return x not in self.path

    def file_constructor(self, filename):
        extracted = Helper.readJson(filename)
        if extracted is not None:
            self.Dimensions = tuple(extracted['Dimensions'])
            self.KingPosition = tuple(extracted['KingPosition'])
            self.CastlePosition = tuple(extracted['CastlePosition'])
            self.Walls = [tuple(x) for x in extracted['Walls']]
        else:
            raise ValueError("Could not read board from selected file.")

    def deepCopy(self, Dimensions, KingPosition, CastlePosition, Walls, path):
        self.Dimensions = Dimensions
        self.KingPosition = KingPosition
        self.CastlePosition = CastlePosition
        self.Walls = Walls
        self.path = path[:]

    def Equals(self, obj):
        return set(obj.path) == set(self.path) and self.CastlePosition == obj.CastlePosition

    def print(self):
        board = Helper.generateBoard(self.Dimensions, self.Walls,
                                     self.CastlePosition, self.KingPosition)
        valid_moves = self.check_moves() + self.check_moves_up()
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == 'X':
                    print(f"{Helper.bcolors.MAGENTA}{cell}{Helper.bcolors.ENDC}", end=' ')
                elif cell == 'O':
                    if (i + 1, j + 1) in valid_moves:
                        print(f"{Helper.bcolors.GREEN}{cell}{Helper.bcolors.ENDC}", end=' ')
                    else:
                        print(f"{Helper.bcolors.YELLOW}{cell}{Helper.bcolors.ENDC}", end=' ')
                elif cell == 'C':
                    print(f"{Helper.bcolors.CYAN}{cell}{Helper.bcolors.ENDC}", end=' ')
                elif cell == 'K':
                    print(f"{Helper.bcolors.BLUE}{cell}{Helper.bcolors.ENDC}", end=' ')
            print()

    def inside_board(self, position):
        if not (self.Dimensions[0] >= position[0] >= 1 and self.Dimensions[1] >= position[1] >= 1):
            return False
        if position in self.Walls:
            return False
        else:
            return True

    def Solved(self):
        if self.CastlePosition == self.KingPosition:
            return True
        else:
            return False

    def check_moves_left(self):
        result = []

        (i, j) = self.CastlePosition
        while True:  # checking the left
            j -= 1
            if not (self.inside_board((i, j)) and not (i, j) in self.Walls):
                break
            else:
                result.append((i, j))
        return result

    def check_moves_right(self):
        result = []

        (i, j) = self.CastlePosition
        while True:  # checking the right
            j += 1
            if not (self.inside_board((i, j)) and not (i, j) in self.Walls):
                break
            else:
                result.append((i, j))
        return result

    def check_moves_up(self):
        result = []
        (i, j) = self.CastlePosition
        while self.inside_board((i, j)):  # checking up
            i -= 1
            if not (self.inside_board((i, j)) and not (i, j) in self.Walls):
                break
            else:
                result.append((i, j))
        return result

    def check_moves_down(self, position):
        result = []
        (i, j) = position
        while self.inside_board((i, j)):  # checking down
            i += 1
            if not (self.inside_board((i, j)) and not (i, j) in self.Walls):
                break
            else:
                result.append((i, j))
        return result

    def check_moves(self):
        return self.check_moves_left() + self.check_moves_right() + self.check_moves_up()

    def move(self, position):
        moves = self.check_moves()
        if position in moves:
            down = self.check_moves_down(position)
            if not down:
                return Board(self.Dimensions, self.KingPosition, position, self.Walls, None, self.path)
            else:
                if position == self.KingPosition:
                    return Board(self.Dimensions, self.KingPosition, position, self.Walls, None, self.path)
                destination = down.pop()
                return Board(self.Dimensions, self.KingPosition, (destination[0], destination[1]), self.Walls, None,
                             self.path)

        else:
            print(f"{position} is an Illegal Move.")
            return None, []

    def get_next_states(self):
        next_states = []
        for move in self.check_moves():
            next_states.append(self.move(move))  # move function return a tuple consisting of the board
        return next_states  # object and the path it took to get where it went
