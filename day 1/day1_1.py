def count_increases(arr):
    increased_count = 0
    for index, number in enumerate(arr):
        if (prev_index := index - 1) < 0: continue
        prev_number = arr[prev_index]
        if number > prev_number:
            increased_count += 1
    return increased_count

with open('day1_input.txt') as f:
    lines = f.readlines()
    arr = [int(line) for line in lines]
    print(count_increases(arr))