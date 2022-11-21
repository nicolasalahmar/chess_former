from Board import Board
from DFS import DFS
from BFS import BFS
from UCS import UCS
from UserPlay import UserPlay


def prompt(board):
    i = input("what would you like to do: \n1)- Play yourself\n2)- DFS\n3)- BFS\n4)- UCS\n5)- A*\n6)- Compare Algorithms\n")
    match i:
        case "1":
            return UserPlay(board)
        case "2":
            return DFS(board)
        case "3":
            return BFS(board)
        case "4":
            return UCS(board)
        # case "5":
        #    return Astar(board)
        case "6":
            print(" UCS stats:", UCS(board).loop(), "\n", "DFS stats:", DFS(board).loop(), "\n", "BFS stats:",
                  BFS(board).loop())
            exit()
        case _:
            exit()


if __name__ == '__main__':
    b = Board((4, 4), (2, 2), (4, 4), [(1, 1)], filename='', path=None)

    b.print()

    prompt(b).loop()
    exit()
