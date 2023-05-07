# ИТОГОВОЕ ЗАДАНИЕ 5.6.1 (HW-02)


def welcome():
    """ intro, rules"""
    print("""
             |--------------------------------------------------|
             |**************************************************|
             |************ Добро пожаловать в игру *************|
             |*************    КРЕСТИКИ НОЛИКИ    **************|
             |**************************************************|
             |**************    Правила игры: ******************|
             |**************************************************|
             |1) Играют  два  игрока, один использует крестики, |
             |   другой нолики.                                 |
             |2) Игровое поле  представляет собой  квадрат 3х3, |
             |   разделенный на 9  клеток.  Каждая клетка имеет |
             |   свои  координаты, по  вертикле и  горизонтале. |
             |3) Игроки ходят по очереди,  ставя свой  символ в |
             |   любую   свободную   клетку с   помощью   ввода |
             |   координат.                                     |
             |4) Побеждает тот Игрок, который сформирует        |
             |   линию из своих трех элементов в горизонтальном,| 
             |   вертикальном или диагональном направлении.     |
             |5) Если все клетки игрового поля заполнены, но ни |
             |   один игрок не смог сформировать выигрышную     |
             |   комбинацию, объявляется 'Ничья!'               |
             |**************************************************|
             |**************************************************|
             |--------------------------------------------------|
            """)


field = [[' '] * 3 for i in range(3)]


def playing_field():
    """ displays the playing field"""
    print()
    print()
    print('                        | 1 | 2 | 3 |')
    print('                    -----------------')
    for i, row in enumerate(field):
        row_str = f"| {i + 1} | {' | '.join(row)} |"
        print('                   ', row_str)
        print('                    -----------------')


def player_move():
    """ input from the user with error checking"""
    while True:
        coord = input('Введите координаты Вашего символа: ').split()
        if len(coord) != 2:
            print('Необходимо вводить два значения!')
            continue
        x, y = coord
        if not (x.isdigit()) or not (y.isdigit()):
            print('Координаты должны быть цифрами!')
            continue
        x, y = int(x), int(y)
        if x < 1 or y < 1 or x > 3 or y > 3:
            print('Неверный диапозон координат')
            continue
        if field[x - 1][y - 1] != ' ':
            print('Клетка занята!')
            continue
        else:
            return x, y


def player_turn(sign):
    """ inserts the corresponding sign into the cell"""
    player = str
    if sign == 'X':
        player = 'КРЕСТИК'
    elif sign == 'O':
        player = 'НОЛИК'
    print('Поставте {} на игровое поле'.format(player))
    x, y = player_move()
    field[x - 1][y - 1] = sign


def is_victory(sign):
    """ checking the winning combination"""
    if (field[0][0] == field[0][1] == field[0][2] == sign) or \
            (field[1][0] == field[1][1] == field[1][2] == sign) or \
            (field[2][0] == field[2][1] == field[2][2] == sign) or \
            (field[0][0] == field[0][1] == field[0][2] == sign) or \
            (field[1][0] == field[1][1] == field[1][2] == sign) or \
            (field[2][0] == field[2][1] == field[2][2] == sign) or \
            (field[0][0] == field[1][1] == field[2][2] == sign) or \
            (field[0][2] == field[1][1] == field[2][0] == sign):
        return True
    else:
        return False


move_counter = 0


def is_draw():
    """ checking the draw"""
    if move_counter == 9:
        return True
    else:
        return False


welcome()
while True:
    playing_field()
    player_turn('X')
    move_counter += 1
    print('ход:', move_counter)
    if is_victory('X'):
        print('                ПОБЕДА ЗА КРЕСТИКОМ!')
        playing_field()
        break
    if is_draw():
        print('                НИЧЬЯ!')
        playing_field()
        break
    playing_field()
    player_turn('O')
    move_counter += 1
    print('ход:', move_counter)
    if is_victory('O'):
        print('                ПОБЕДА ЗА НОЛИКОМ!')
        playing_field()
        break
    if is_draw():
        print('                НИЧЬЯ!')
        playing_field()
        break
