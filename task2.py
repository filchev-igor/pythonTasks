import numpy as numpy


def start_task_2():
    while True:
        action = input("Enter size as 2,2. Max option is 6,6. Press 0 to stop programme ")

        if action == '0':
            break

        rows = int(action[0])
        columns = int(action[2])

        generate_board(rows, columns)


def generate_board(rows, columns):
    length = rows * columns
    j = 1

    for i in range(columns):
        print(' ---', end='')

    print(end='\n')

    for row in range(rows):
        print('| ' + ' | '.join(str(k) for k in range(j, columns + j, 1)) + ' |')

        for i in range(columns):
            print(' ---', end='')

        print(end='\n')

        j += columns
