from Board import Board
from DFS import DFS
from BFS import BFS
from UCS import UCS
from Astar import Astar
from UserPlay import UserPlay


def prompt(b):
    i = input("what would you like to do: \n1)- Play yourself\n2)- DFS\n3)- BFS\n4)- UCS\n5)- A*\n6)- Compare Algorithms\n")
    match i:
        case "1":
            return UserPlay(b)
        case "2":
            return DFS(b)
        case "3":
            return BFS(b)
        case "4":
            return UCS(b)
        case "5":
            return Astar(board)
        case "6":
            b1 = Board(b.Dimensions, b.KingPosition, b.CastlePosition, b.Walls)
            b2 = Board(b.Dimensions, b.KingPosition, b.CastlePosition, b.Walls)
            b3 = Board(b.Dimensions, b.KingPosition, b.CastlePosition, b.Walls)
            b4 = Board(b.Dimensions, b.KingPosition, b.CastlePosition, b.Walls)
            print(" UCS stats:", UCS(b1).loop(), "\n", "DFS stats:", DFS(b2).loop(), "\n", "BFS stats:",
                  BFS(b3).loop(), "\n", "A* stats:", Astar(b4).loop())
            exit()
        case _:
            exit()


if __name__ == '__main__':
    board = Board((4, 4), (2, 2), (4, 4), [(1, 1)], filename='', path=None)

    board.print()

    prompt(board).loop()
    input()
    exit()
