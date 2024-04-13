board = list(range(1, 10))

board_size = 3

name_1 = input('Введите имя первого игрока: ')
name_2 = input('Введите имя второго игрока: ')
player_1 = 'X'
player_2 = '0'

def display_board():
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('---+---+-----'))

def game(position, char):
    if position > 9 or position < 1 or board[position - 1] in ('X', '0'):
        return False
    board[position - 1] = char

    return True

def check_win():
    win = False

    win_comb = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )

    for comb in win_comb:
        if board[comb[0]] == board[comb[1]] and board[comb[1]] == board[comb[2]]:
            win = board[comb[0]]

    return win


def play_game():
    current_name = name_1
    current_player = player_1
    step = 1
    display_board()

    while step < 10 and check_win() == False:
        position = int(input('Ход игрока ' + current_name + '. Введите номер ячейки от 1 до 9: '))

        if position == 0:
            print('Выход из игры!')
            break

        if game(position, current_player):
            print('Отличный ход!')

            if check_win():
                print('Выиграл игрок ' + current_name)
                break

            if current_player == player_1 and current_name == name_1:
                current_player, current_name = player_2, name_2
            else:
                current_player, current_name = player_1, name_1

            display_board()
            step += 1
        else:
            print('Ход не верный! Попробуй снова')

    if step == 10:
        print('Ничья!')

play_game()