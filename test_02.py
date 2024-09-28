def valid_sudoku(board: list[list[str]]) -> bool:
    # validate row
    local_dict: dict[str, int] = dict()
    for i in range(len(board)):
        for val in board[i]:
            if val not in local_dict and val != ".":
                local_dict[val] = 1
            elif val in local_dict:
                return False
        local_dict.clear()

    # validate column
    local_dict_02: dict[str, int] = dict()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[j][i] not in local_dict_02 and board[j][i] != ".":
                local_dict_02[board[j][i]] = 1
            elif board[j][i] in local_dict_02:
                return False
        local_dict_02.clear()

    # validate 3 by 3 grid
    local_dict_03: dict[str, int] = dict()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[j][i] not in local_dict_03 and board[j][i] != ".":
                local_dict_03[board[j][i]] = 1
            elif board[j][i] in local_dict_03:
                return False
    local_dict_03.clear()

    local_dict_04: dict[str, int] = dict()
    for i in range(0, 3):
        for j in range(3, 6):
            if board[j][i] not in local_dict_04 and board[j][i] != ".":
                local_dict_04[board[j][i]] = 1
            elif board[j][i] in local_dict_04:
                return False
    local_dict_04.clear()

    local_dict_04: dict[str, int] = dict()
    for i in range(0, 3):
        for j in range(6, 9):
            if board[j][i] not in local_dict_04 and board[j][i] != ".":
                local_dict_04[board[j][i]] = 1
            elif board[j][i] in local_dict_04:
                return False
    local_dict_04.clear()

    # ----------------------------

    local_dict_03: dict[str, int] = dict()
    for i in range(3, 6):
        for j in range(0, 3):
            if board[j][i] not in local_dict_03 and board[j][i] != ".":
                local_dict_03[board[j][i]] = 1
            elif board[j][i] in local_dict_03:
                return False
    local_dict_03.clear()

    local_dict_04: dict[str, int] = dict()
    for i in range(3, 6):
        for j in range(3, 6):
            if board[j][i] not in local_dict_04 and board[j][i] != ".":
                local_dict_04[board[j][i]] = 1
            elif board[j][i] in local_dict_04:
                return False
    local_dict_04.clear()

    local_dict_04: dict[str, int] = dict()
    for i in range(3, 6):
        for j in range(6, 9):
            if board[j][i] not in local_dict_04 and board[j][i] != ".":
                local_dict_04[board[j][i]] = 1
            elif board[j][i] in local_dict_04:
                return False
    local_dict_04.clear()

    # ----------------------------

    local_dict_03: dict[str, int] = dict()
    for i in range(6, 9):
        for j in range(0, 3):
            if board[j][i] not in local_dict_03 and board[j][i] != ".":
                local_dict_03[board[j][i]] = 1
            elif board[j][i] in local_dict_03:
                return False
    local_dict_03.clear()

    local_dict_04: dict[str, int] = dict()
    for i in range(6, 9):
        for j in range(3, 6):
            if board[j][i] not in local_dict_04 and board[j][i] != ".":
                local_dict_04[board[j][i]] = 1
            elif board[j][i] in local_dict_04:
                return False
    local_dict_04.clear()

    local_dict_04: dict[str, int] = dict()
    for i in range(6, 9):
        for j in range(6, 9):
            if board[j][i] not in local_dict_04 and board[j][i] != ".":
                local_dict_04[board[j][i]] = 1
            elif board[j][i] in local_dict_04:
                return False
    local_dict_04.clear()

    return True


def main() -> None:
    value = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(valid_sudoku(value))


if __name__ == '__main__':
    main()
