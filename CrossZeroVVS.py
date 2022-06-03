import requests

board = [1, 2, 3, 4, 5, 6, 7, 8, 9] # создаём список поля
var_win = [
        [0, 1, 2],
        [0, 4, 8],
        [0, 3, 6],
        [6, 7, 8],
        [2, 5, 8],
        [1, 4, 7],
        [3, 4, 5],
        [2, 4, 6]
    ] # выигрышные варианты

steps = board # список доступных для хода полей
human = True
man = ""
comp = ""
step = None
symbol = ""
win = ""

def hello():
    print("                     Игра крестики-нолики!")
    print("Инструкция:")
    print("Дано поле 3х3 клетки, нужно выбрать символы какими будешь играть,")
    print("крестики или нолики. Выигрывает тот у кого получилось три символа в ряд.")
    print('''
    -------------
    1  |  2  |  3
    -------------
    4  |  5  |  6
    -------------
    7  |  8  |  9
    -------------
    ''')

def vopros():
    otvet = input("Вы хотите сделать первый ход (y или n)? ")
    if otvet == "y":
        print("Вы играете крестиками!")
        man = "X"
    else:
        print("Вы играете ноликами!")
        man = "O"

    return man


def board_draw(board): # рисуем доску
    print(" --------------")
    print(" ", board[0], " | ", board[1], " | ", board[2])
    print(" --------------")
    print(" ", board[3], " | ", board[4], " | ", board[5])
    print(" --------------")
    print(" ", board[6], " | ", board[7], " | ", board[8])
    print(" --------------")


def step_board(step, symbol): # вносим в список поля символ Х или О
    ind = board.index(step)
    board[ind] = symbol


def step_human():   # ход который делает человек
    check = True
    while check:
        places = int(input("В какую клетку будете ставить свой ход? (номер клетки 1 - 9): "))
        if 1 <= places <= 9:
            check = False
        else:
            print("Вы указали неправильный номер!")
            check = True

        if places in steps:
            print("Ход сделан!")
            check = False
        else:
            print("Эта клетка уже занята или находится вне игрового поля!")
            check = True

    return places


def available_moves(board):  # проверка доступных для хода полей
    steps = []
    for i in board:
        if board.index(i) != "X" or "O":
            steps.append(i)
        else:
            continue

    return steps


def checking_win(board):  # проверка выигрышных вариантов
    win = ""
    for i in var_win:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O"
    return win


def check_line(sum_O, sum_X):  # поиск победных линий
    step = ""
    for line in var_win:
        o = 0
        x = 0

        for j in range(0, 3):
            if board[line[j]] == "O":
                o = o + 1
            if board[line[j]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if board[line[j]] != "O" and board[line[j]] != "X":
                    step = board[line[j]]

    return step


def step_comp():  # ход который делает компьютер
    step = ""

    # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
    step = check_line(2, 0)

    # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
    if step == "":
        step = check_line(0, 2)

    # 3) если 1 фигура своя и 0 чужих - ставим
    if step == "":
        step = check_line(1, 0)

    # 4) центр пуст, то занимаем центр
    if step == "":
        if board[4] != "X" and board[4] != "O":
            step = 5

    # 5) если центр занят, то занимаем первую ячейку
    if step == "":
        if board[0] != "X" and board[0] != "O":
            step = 1

    return step


def main():
    end = True
    hello()
    symbol = vopros()
    if symbol == "X":
        man = "X"
        comp = "O"
        human = True
    else:
        man = "O"
        comp = "X"
        human = False

    while end:
        if human == True: # ход человека
            symbol = man
            step = step_human()

        else:
            print("Ход Искуственного Интеллекта!")
            symbol = comp
            step = step_comp()


        if step != "":
            step_board(step, symbol)  # записываем ход в указанную ячейку
            steps = available_moves(board) # обновляем список доступных для хода полей
            board_draw(board)  # рисуем доску
            win = checking_win(board)  # определяем победителя

            if win != "":
                end = False
            else:
                end = True
        else:
            print("Ничья!")
            end = False
            win = "ничья"

        human = not (human)

    print("Выиграл: ", win)
    exit = input("Для выхода нажмите любую клавишу: ")
    if exit:
        print("Good bay!")

main()