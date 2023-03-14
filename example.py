def print_hi(name):
    a = "anupras - 1, simas - 2000, petras - 30"

    pairs = a.split(', ')
    words = [i.split(' - ')[0] for i in pairs]

    # print(words)

    b = 'Oil price <input type = "text" value = "100">'

    parts = b.split('"')

    html1 = f'<div>{int(parts[3])} USD </div>'
    html2 = f'<div>{float(parts[3]) * 1.1} EUR </div>'

    print(html1)
    print(html2)

    d = "anupras - 1, simas - 2000, petras - 30"

    stuff = d.split(', ')
    initial_stuff_data = [i.split(' - ') for i in stuff]

    salary = 0
    output = ''

    # stuff_data = (...initial_stuff_data).sort(key=lambda l: int(l[1]), reverse=True)

    # print(stuff_data[0][1])