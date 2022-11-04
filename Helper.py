import json
import numpy as np


def verifyBoard(array):
    if not (array["Dimensions"][0] >= array["CastlePosition"][0] >= 1 and
            array["Dimensions"][1] >= array["CastlePosition"][1] >= 1):
        return False  # check the castle is in the correct place

    if not (array["Dimensions"][0] >= array["KingPosition"][0] >= 1 and
            array["Dimensions"][1] >= array["KingPosition"][1] >= 1):
        return False  # check the king is in the correct place

    for cell in array["Walls"]:
        if not (array["Dimensions"][0] >= cell[0] >= 1 and
                array["Dimensions"][1] >= cell[1] >= 1):
            return False
    return True


def readJson(filename):
    if len(filename) < 1:
        filename = "Board.json"
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        return None
    else:
        board = json.loads(f.read())
        if verifyBoard(board):
            return board
        else:
            return None


def generateBoard(dimensions, Walls, CastlePosition, KingPosition):
    array = np.full(dimensions, 'X')
    for cell in Walls:
        array[cell[0] - 1][cell[1] - 1] = 'O'
    array[CastlePosition[0] - 1][CastlePosition[1] - 1] = 'C'
    array[KingPosition[0] - 1][KingPosition[1] - 1] = 'K'
    return array


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
