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
            return UserPlay(b).loop()
        case "2":
            return DFS(b).loop()
        case "3":
            return BFS(b).loop()
        case "4":
            return UCS(b).loop()
        case "5":
            return Astar(b).loop()
        case "6":
            b1 = Board(b.Dimensions, b.KingPosition, b.CastlePosition, b.Walls)
            b2 = Board(b.Dimensions, b.KingPosition, b.CastlePosition, b.Walls)
            b3 = Board(b.Dimensions, b.KingPosition, b.CastlePosition, b.Walls)
            b4 = Board(b.Dimensions, b.KingPosition, b.CastlePosition, b.Walls)
            c1 = UCS(b1).loop()
            c2 = DFS(b2).loop()
            c3 = BFS(b3).loop()
            c4 = Astar(b4).loop()
            print(" UCS stats:", c1, "\n", "DFS stats:", c2, "\n", "BFS stats:",
                  c3, "\n", "A* stats:", c4)
        case _:
            exit()


if __name__ == '__main__':
    board = Board((4, 4), (2, 2), (4, 4), [(1, 1)], filename='Board.json', path=None)

    board.print()

    prompt(board)
    input()
    exit()
