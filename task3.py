def start_task_3():
    processor_1_load = [4, 9, 7]
    processor_2_load = [5, 2, 1]

    print('PROC1     |PROC2     |')

    for value in processor_1_load:
        index = processor_1_load.index(value)
        print('*' * value + ' ' * (10 - value - 1) + ' |', end='')
        print('*' * processor_2_load[index] + ' ' * (10 - processor_2_load[index] - 1) + ' |', end='')

        if (value + processor_2_load[index]) >= 10:
            print('x')

        print(end='\n')