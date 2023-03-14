def start_task_5():
    table = 'nafta - 50EUR, bendzinas - 100EUR, dujos - 60EUR, auksas - 110EUR'

    list = table.split(', ')

    print('<div display="flex" style="border: 1px solid gray;">')

    for row in list:
        values = row.split(' - ')

        for value in values:
            print(f'    <div>{value}</div>')

    print('</div>')
