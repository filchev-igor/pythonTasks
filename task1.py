def start_task_1():
    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

    print_board(board)

    while True:
        action = input("Enter 'a' to add a number. Type 'd' to delete a number. Enter '0' to stop programme ")

        if action == '0':
            break

        if action[0] == 'a':
            add_number(board, action[1])
        elif action[0] == 'd':
            remove_number(board, action[1])

        print_board(board)


def print_board(board):
    print(' ---  ---  ---')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print(' ---  ---  ---')


def add_number(board, num):
    for row in board:
        if num in row:
            row[row.index(num)] = 'X'
            break


def remove_number(board, num):
    for row in board:
        if num in row:
            row[row.index(num)] = num
            break