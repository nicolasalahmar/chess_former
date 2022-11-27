import json
import numpy as np
import math
import Board


def verifyBoard(array):
    if not (array["Dimensions"][0] >= array["CastlePosition"][0] >= 1 and
            array["Dimensions"][1] >= array["CastlePosition"][1] >= 1):
        return "Castle Position doesn't conform with dimensions."  # check the castle is in the correct place

    if not (array["Dimensions"][0] >= array["KingPosition"][0] >= 1 and
            array["Dimensions"][1] >= array["KingPosition"][1] >= 1):
        return "King position doesn't conform with dimensions."  # check the king is in the correct place

    for cell in array["Walls"]:
        if not (array["Dimensions"][0] >= cell[0] >= 1 and
                array["Dimensions"][1] >= cell[1] >= 1):
            return f"({cell} wall position is not correct."

    for cell in array["Walls"]:
        if (cell[0] == array["CastlePosition"][0] and cell[1] == array["CastlePosition"][1]) or (
                cell[0] == array["KingPosition"][0] and cell[1] == array["KingPosition"][1]):
            return "Castle or King are in the same position as a wall."
    return True


def readJson(filename):
    if len(filename) < 1:
        filename = "Board.json"

    f = open(filename, 'r')
    board = json.loads(f.read())

    error_message = verifyBoard(board)
    if isinstance(error_message, str):
        return error_message
    else:
        return board


def generateBoard(dimensions, Walls, CastlePosition, KingPosition):
    array = np.full(dimensions, 'O')
    for cell in Walls:
        array[cell[0] - 1][cell[1] - 1] = 'X'
    array[CastlePosition[0] - 1][CastlePosition[1] - 1] = 'C'
    array[KingPosition[0] - 1][KingPosition[1] - 1] = 'K'
    return array


def print_blind_search(solution, n, t2, t1):
    print()
    if solution is None:
        print("there is no solution!")
        return
    for x in solution.path:
        temp = Board.Board(solution.Dimensions, solution.KingPosition, x, solution.Walls)
        temp.print()
        print()

    print("number of nodes in path is:", len(solution.path))
    print(solution.path)

    print("number of nodes traversed:", n)

    print("time elapsed:", round(t2 - t1, 4), "s")


def initialize_dict(board):
    temp = {}
    for i in range(board.Dimensions[0] + 1):
        for j in range(board.Dimensions[1] + 1):
            temp[(i, j)] = []
    return temp


def absolute_distance(position1, position2):
    return math.sqrt(((position1[0] - position2[0]) ** 2) + (position1[1] - position2[1]) ** 2)


class bcolors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m'
    ENDC = '\033[0m'
