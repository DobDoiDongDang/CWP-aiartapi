import math
def cross_pattern(location, boardsize):
    '''check cross pattern'''
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
        if location != list([min(6, upperstart_x+i), min(6, upperstart_y+i)]):
            aim.append(list([min(6, upperstart_x+i), min(6, upperstart_y+i)]))
    for i in range(0, boardsize+1):
        for j in range(0, boardsize+1):
            if i+j == x+y and location != list([i, j]):
                aim.append(list([i, j]))
    return aim

def plus_pattern(location, boardsize):
    '''check rook pattern'''
    aim = []
    x = location[0]
    y = location[1]
    rowstart = [1, y]
    colstart = [x, 1]
    for i in range(1, boardsize + 1):
        if list([i, y]) not in aim and list[(i, y)] != list[(x, y)]:
                aim.append(list([i, y]))
        if list([x, i]) not in aim and list[(x, i)] != list[(x, y)]:
                aim.append(list([x, i]))
    return aim

def pawn_pattern(location, boardsize):
    '''check pawn pattern'''
    aim = []
    x = location[0]
    y = location[1]
    if y - 1 < 1:
        if x - 1 < 0:
            aim.append(list([x+1, y+1]))
        elif x + 1 > boardsize:
            aim.append(list([x-1, y-1]))
        else:
            aim.append(list([x+1, y-1]))
            aim.append(list([x-1, y-1]))
    return aim

def queen_pattern(location, boardsize):
    '''check queen pattern'''
    aim = []
    aim.extend(cross_pattern(location, boardsize))
    aim.extend(plus_pattern(location, boardsize))
    return aim


def isking(board):
    '''Check if king in board'''
    return True if board.count("K") == 1 else False

def issquare(board):
    '''Check if board is square'''
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
    '''render board'''
    for i in board:
        print(i, end="")
    print()

def finding_pieces_location(board):
    '''Find a pieces location'''
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
                dic[key]["aim"] = plus_pattern(location, boardsize)
            elif i == "B":
                dic[key]["aim"] = cross_pattern(location, boardsize)
            elif i == "Q":
                dic[key]["aim"] = queen_pattern(location, boardsize)
            elif i == "P":
                dic[key]["aim"] = pawn_pattern(location, boardsize)
            pieces += 1
        index_x += 1
    return dic


def checkmate(board):
    '''Checkmate bro'''
    board = board.replace(" ", "")
    render_board(board)
    print("Is square : ", issquare(board))
    print("Is King : ", isking(board))
    dic = finding_pieces_location(board)
    print("dic : ", dic)


if __name__ == "__main__":
    board = """\
            P....
            .K...
            ..Q..
            .....
            .....\
            """
    checkmate(board)
