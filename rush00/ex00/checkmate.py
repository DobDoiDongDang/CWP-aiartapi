import math
import sys
def king_pattern(location, boardsize):
    '''check king pattern'''
    aim = []
    king_x = location[0]
    king_y = location[1]
    for x in range(king_x-1, king_x+2):
        for y in range(king_y-1, king_y+2):
            if [x, y] == [king_x, king_y]:
                continue
            if x-1 < 0 or x+1 > boardsize+1:
                continue
            if y-1 < 0 or y+1 > boardsize+1:
                continue
            aim.append(list([x, y]))
    return aim



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
        if location != list([min(boardsize, upperstart_x+i), min(boardsize, upperstart_y+i)]):
            aim.append(list([min(boardsize, upperstart_x+i), min(boardsize, upperstart_y+i)]))
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
    if y - 1 > 0:
        if x - 1 < 1:
            aim.append(list([x+1, y-1]))
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

def is_check(location_list):
    king_location = location_list["K"]["Location"]
    for pieces in location_list.keys():
        if pieces[0] != "K":
            for aim in location_list[pieces]["aim"]:
                if aim == king_location:
                    return True
    return False

def is_checkmate(location_list):
    list_point = []
    king_location = location_list["K"]["Location"]
    list_point.append(king_location)
    list_point.extend(location_list["K"]["aim"])
    for pieces in location_list.keys():
        if pieces[0] != "K":
            for aim in location_list[pieces]["aim"]:
                if aim in list_point:
                    list_point.pop(list_point.index(aim))
                if len(list_point) == 0:
                    return True
    return False



def is_king(board):
    '''Check if king in board'''
    return True if board.count("K") == 1 else False

def is_square(board):
    '''Check if board is square'''
    boardsize = len(board.replace("\n", ""))
    row = 1
    for i in board:
        if i == "\n":
            row += 1
    row -= 1
    if row**2 == boardsize:
        return True
    else:
        return False

def render_board(pieces_list, boardsize):
    '''render board'''
    pieces_location = []
    pieces_name = []
    aim_location = []
    col_indi = 1
    row_indi = 1
    for pieces in pieces_list.keys():
        pieces_location.append(pieces_list[pieces]["Location"])
        pieces_name.append(pieces)
        if pieces != "K":
            aim_location.extend(pieces_list[pieces]["aim"])
    print(" D", end="")
    for y in range(0, boardsize+1):
        for x in range(0, boardsize+1):
            if y == 0 and col_indi > boardsize:
                continue
            if y == 0 and col_indi <= boardsize:
                print(f" {col_indi} ", end="")
                col_indi += 1
            elif x == 0 and row_indi <= boardsize:
                print(f" {row_indi}", end="")
                row_indi += 1
            elif list([x, y]) in pieces_location: 
                print(f" {pieces_name[pieces_location.index(list([x,y]))][0]} ", end="")
            elif list([x, y]) in aim_location:
                print(" X ", end="")
            else:
                print(" . ", end="")
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
            if i == "K":
                key = "K"
            else:
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
            elif i == "K":
                dic["K"]["aim"] = king_pattern(location, boardsize)
                pieces -= 1
            pieces += 1
        index_x += 1
    return dic


def checkmate(board):
    '''Checkmate bro'''
    board = board.replace(" ", "")
    dic = finding_pieces_location(board)
    render_board(dic, int(math.sqrt(len(board.replace("\n", "")))))
    print("="*(int(math.sqrt(len(board.replace("\n", ""))))*3), end="=\n")
    if not is_king(board):
        print("ERROR!! No King input")
        return
    if not is_square(board):
        print("ERROR!! Not a square board")
        return
    if is_checkmate(dic):
        print("SUCCESS!!!!!")
    elif is_check(dic):
        print("SUCCESS")
    else:
        print("FAIL")
    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            with open(sys.argv[i], 'r') as f:
                checkmate(f.read())
    else:
        board = """\
                ......R.
                ........
                R.......
                ........
                ........
                ........
                ...K....
                ........

                """
        checkmate(board)
