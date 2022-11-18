from Board import Board
from DFS import DFS
from BFS import BFS
from UserPlay import UserPlay


def prompt(board):
    # i = input("what would you like to do: \n1)- Play yourself\n2)- DFS\n3)- BFS\n4)- UCS\n5)- A*\n")
    i = "3"
    match i:
        case "1":
            return UserPlay(board)
        case "2":
            return DFS(board)
        case "3":
            return BFS(board)
        # case "4":
        #    return UCS(board)
        # case "5":
        #    return Astar(board)
        case _:
            return None


if __name__ == '__main__':
    b = Board((4, 4), (2, 2), (4, 4), [(1, 1)], '')

    b.print()

    prompt(b).loop()
