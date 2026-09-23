import math
def boardprint(row, col):
    return
def bishop(location, boardsize):
    aim = []
    x = location[0]
    y = location[1]
    if x > y:
        upperstart_y = 1
        upperstart_x = x - (y - 1)
    else:
        upperstart_x = 1
        upperstart_y = y - (x - 1)
    for i in range(0, 1+boardsize-max(upperstart_x, upperstart_y)):
        aim.append(list([min(6, upperstart_x+i), min(6, upperstart_y+i)]))
    return aim

def rook(location, boardsize):
    aim = []
    x = location[0]
    y = location[1]
    rowstart = [1, y]
    colstart = [x, 1]
    for i in range(1, boardsize+1):
        if list([i, y]) not in aim and list[(i, y)] != list[(x, y)]:
                aim.append(list([i, y]))
        if list([x, i]) not in aim and list[(x, i)] != list[(x, y)]:
                aim.append(list([x, i]))
    return aim


def isking(board):
    return True if board.count("K") == 1 else False
def issquare(board):
    boardsize = len(board.replace("\n", ""))
    row = 1
    for i in board:
        if i == "\n":
            row += 1
    if row**2 == boardsize:
        return True
    else:
        return False
def render_board(board):
    for i in board:
        print(i, end="")
    print()

def finding_pieces_location(board):
    dic = {}
    index_x = 1
    index_y = 1
    pieces = 1
    boardsize = int(math.sqrt(len(board.replace("\n", ""))))
    for i in board:
        if i == "\n":
            index_y += 1
            index_x = 1
            continue
        elif i != ".":
            key = i+str(pieces)
            location = list([index_x, index_y])
            dic[key] = {}
            dic[key]["Location"] = location
            if i == "R":
                dic[key]["aim"] = rook(location, boardsize)
            if i == "B":
                dic[key]["aim"] = bishop(location, boardsize)
            pieces += 1
        index_x += 1
    return dic


def checkmate(board):
    board = board.replace(" ", "")
    render_board(board)
    print("Is square : ", issquare(board))
    print("Is King : ", isking(board))
    dic = finding_pieces_location(board)
    print("dic : ", dic)


if __name__ == "__main__":
    board = """\
            ....B
            .K...
            .....
            .....
            ..B..\
            """
    checkmate(board)
