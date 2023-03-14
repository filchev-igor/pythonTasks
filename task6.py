numbers1 = [1, 2, 3, 4, 5]
numbers2 = [5, 2, 5, 1, 5, 1]


def start_task_6():
    compare(numbers1, numbers2)


def compare(*numbers):
    def overlap():
        overlap = []

        if len(numbers[0]) > len(numbers[1]):
            new_numbers1 = numbers[0]
            new_numbers2 = numbers[1]
        else:
            new_numbers1 = numbers[1]
            new_numbers2 = numbers[0]

        for number in new_numbers1:
            if number in new_numbers2 and number not in overlap:
                overlap.append(number)

        print(overlap)

    def different():
        difference = []

        if len(numbers[0]) > len(numbers[1]):
            new_numbers1 = numbers[1]
            new_numbers2 = numbers[0]
        else:
            new_numbers1 = numbers[0]
            new_numbers2 = numbers[1]

        for number in new_numbers1:
            if number not in new_numbers2 and number not in difference:
                difference.append(number)

        print(difference)

    overlap()
    different()
