import Helper


class Board:
    def __init__(self, Dimensions, KingPosition, CastlePosition, Walls, filename=None):
        self.board = None
        self.Dimensions = None
        self.KingPosition = None
        self.CastlePosition = None
        self.Walls = None

        if filename is not None:
            self.file_constructor(filename)
        else:
            self.hardCopy(Dimensions, KingPosition, CastlePosition, Walls)

    def file_constructor(self, filename):
        extracted = Helper.readJson(filename)
        if extracted is not None:
            self.board = Helper.generateBoard(extracted['Dimensions'], extracted['Walls'],
                                              extracted['CastlePosition'], extracted['KingPosition'])
            self.Dimensions = tuple(extracted['Dimensions'])
            self.KingPosition = tuple(extracted['KingPosition'])
            self.CastlePosition = tuple(extracted['CastlePosition'])
            self.Walls = [tuple(x) for x in extracted['Walls']]
        else:
            raise ValueError("Could not read board from selected file.")

    def hardCopy(self, Dimensions, KingPosition, CastlePosition, Walls):
        self.board = Helper.generateBoard(Dimensions, Walls, CastlePosition, KingPosition)
        self.Dimensions = Dimensions
        self.KingPosition = KingPosition
        self.CastlePosition = CastlePosition
        self.Walls = Walls

    def Equals(self, obj):
        return self.CastlePosition == obj.CastlePosition

    def print(self):
        valid_moves = self.check_moves()
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == 'O':
                    print(f"{Helper.bcolors.MAGENTA}{cell}{Helper.bcolors.ENDC}", end=' ')
                elif cell == 'X':
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
        while self.inside_board((i, j)):  # checking the right
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
                return Board(self.Dimensions, self.KingPosition, position, self.Walls)
            else:
                return Board(self.Dimensions, self.KingPosition, (down.pop()[0], down.pop()[1]), self.Walls)

        else:
            print(f"{position} is an Illegal Move.")
            return None

    # def animated_print(self, old_position, new_position):
    #     old_board = Board(self.Dimensions, self.KingPosition, old_position, self.Walls)
    #     new_board = Board(self.Dimensions, self.KingPosition, new_position, self.Walls)
    #     old_board.print()
